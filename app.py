"""
app.py — Lightweight Python HTTP Server cho UET K3 RAG Intelligence Web UI.
Sử dụng thư viện chuẩn của Python (http.server), không cần cài thêm pip package.
"""
from __future__ import annotations

import json
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

# Import RAG Core modules from lab
from ingest import build_knowledge_base
from main import _select_embedder, demo_llm
from src.agent import KnowledgeBaseAgent
from src.chunking import RecursiveChunker

PORT = int(os.getenv("PORT", "8000"))
DATA_DIR = os.getenv("LAB_DATA_DIR", "data/k3_university")
UI_DIR = Path(__file__).parent / "ui"

print("=" * 65)
print("🚀 ĐANG KHỞI TẠO KNOWLEDGE BASE (K3 UNIVERSITY RAG)...")
print("=" * 65)

embedder = _select_embedder()
chunker = RecursiveChunker(chunk_size=400)
store = build_knowledge_base(DATA_DIR, embedding_fn=embedder, chunker=chunker)
agent = KnowledgeBaseAgent(store=store, llm_fn=demo_llm)

TOTAL_CHUNKS = store.get_collection_size()
print(f"✅ Đã nạp thành công {TOTAL_CHUNKS} chunks từ {DATA_DIR}")
print(f"📌 Chiến lược Chunking: {chunker.__class__.__name__}(chunk_size={chunker.chunk_size})")
print("=" * 65)


class RAGHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(UI_DIR), **kwargs)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/status":
            self.send_json_response(
                200,
                {
                    "status": "online",
                    "total_chunks": TOTAL_CHUNKS,
                    "strategy": f"{chunker.__class__.__name__}(chunk_size={chunker.chunk_size})",
                    "data_dir": DATA_DIR,
                },
            )
            return

        # Fallback to index.html for root path
        if parsed.path in ("/", ""):
            self.path = "/index.html"

        super().do_GET()

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/rag":
            try:
                content_length = int(self.headers.get("Content-Length", 0))
                body_bytes = self.rfile.read(content_length)
                payload = json.loads(body_bytes.decode("utf-8"))

                query = str(payload.get("query", "")).strip()
                meta_filter = payload.get("filter")
                top_k = int(payload.get("top_k", 3))

                if not query:
                    self.send_json_response(400, {"error": "Query cannot be empty"})
                    return

                # Perform Search with or without Filter
                if meta_filter and isinstance(meta_filter, dict) and meta_filter:
                    results = store.search_with_filter(query, top_k=top_k, metadata_filter=meta_filter)
                else:
                    results = store.search(query, top_k=top_k)

                # Generate Answer via KnowledgeBaseAgent
                answer = agent.answer(query, top_k=top_k)

                self.send_json_response(
                    200,
                    {
                        "query": query,
                        "filter": meta_filter,
                        "top_k": top_k,
                        "results": results,
                        "answer": answer,
                    },
                )
            except Exception as exc:
                self.send_json_response(500, {"error": str(exc)})
            return

        self.send_error(404, "Endpoint not found")

    def send_json_response(self, status_code: int, data: dict[str, Any]) -> None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format: str, *args: Any) -> None:
        # Custom concise console log
        sys.stderr.write(f"[{self.log_date_time_string()}] {self.address_string()} - {format % args}\n")


def run_server(port: int = PORT) -> None:
    server_address = ("0.0.0.0", port)
    httpd = HTTPServer(server_address, RAGHTTPRequestHandler)
    print(f"🌟 Web UI Server đang chạy tại: http://localhost:{port}")
    print("👉 Bấm Ctrl+C để dừng máy chủ.")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Đang dừng máy chủ RAG...")
        httpd.server_close()


def test_server_logic() -> int:
    """Tự động kiểm tra logic RAG backend không cần mở cổng mạng."""
    print("===> Đang chạy test-mode tự kiểm tra backend RAG...")
    assert TOTAL_CHUNKS > 0, "Không nạp được chunk từ corpus"

    test_q = "Ngưỡng đầu vào đại học ngành Trí tuệ nhân tạo là bao nhiêu điểm?"
    results = store.search(test_q, top_k=3)
    assert len(results) > 0, "Search không trả về kết quả"
    assert "score" in results[0] and "content" in results[0], f"Sai format: {results[0]}"

    ans = agent.answer(test_q, top_k=3)
    assert isinstance(ans, str) and len(ans) > 0, "Agent không sinh được câu trả lời"

    print("===> TEST-MODE PASS! Toàn bộ API logic hoạt động hoàn hảo.")
    return 0


if __name__ == "__main__":
    if "--test-mode" in sys.argv:
        raise SystemExit(test_server_logic())
    run_server()
