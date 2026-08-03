"""
bench.py — Chạy benchmark 5 câu hỏi với chiến lược chunking riêng của cá nhân.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

from ingest import build_knowledge_base
from main import _select_embedder, demo_llm
from src.agent import KnowledgeBaseAgent
from src.chunking import RecursiveChunker

DEFAULT_DATA_DIR = "data/k3_university"

QUERIES = [
    {
        "id": "Q1",
        "question": "Ngưỡng đầu vào đại học chính quy năm 2025 của ngành Trí tuệ nhân tạo là bao nhiêu điểm?",
        "filter": None,
    },
    {
        "id": "Q2",
        "question": "Hạn cuối nộp hồ sơ xét tuyển trực tuyến theo HSA và SAT năm 2025 sau khi gia hạn là khi nào?",
        "filter": None,
    },
    {
        "id": "Q3",
        "question": "Năm 2026 sinh viên năm thứ nhất Trường ĐH Công nghệ học ở cơ sở nào và được đăng ký tối đa bao nhiêu nguyện vọng?",
        "filter": None,
    },
    {
        "id": "Q4",
        "question": "Một học phần có khối lượng bao nhiêu tín chỉ và một tín chỉ tương ứng bao nhiêu giờ tín chỉ?",
        "filter": None,
    },
    {
        "id": "Q5",
        "question": "Trường ĐH Công nghệ có tổ chức chương trình du học ngắn hạn thu phí và cử người liên hệ thí sinh thu tiền không?",
        "filter": None,
    },
]


def run_benchmark(data_dir: str = DEFAULT_DATA_DIR) -> int:
    print("=" * 70)
    print("BENCHMARK CHUNKING STRATEGY - K3 UNIVERSITY RAG")
    print("=" * 70)

    # 1. Chọn chunker của riêng bạn (chiến lược RecursiveChunker với chunk_size=400)
    chunker = RecursiveChunker(chunk_size=400)
    print(f"Chiến lược Chunking: {chunker.__class__.__name__}")
    print(f"Tham số: chunk_size={chunker.chunk_size}, separators={chunker.separators}")

    # 2. Nạp thư mục corpus
    embedder = _select_embedder()
    store = build_knowledge_base(data_dir, embedding_fn=embedder, chunker=chunker)
    total_chunks = store.get_collection_size()
    print(f"Thư mục dữ liệu: {data_dir}")
    print(f"Số chunk đã nạp vào EmbeddingStore: {total_chunks}")
    print("=" * 70)

    # 3. Chạy 5 query qua search() / search_with_filter()
    agent = KnowledgeBaseAgent(store=store, llm_fn=demo_llm)

    for item in QUERIES:
        qid = item["id"]
        question = item["question"]
        filter_dict = item["filter"]

        print(f"\n[{qid}] Query: {question}")
        if filter_dict:
            print(f"    Filter: {filter_dict}")
            results = store.search_with_filter(question, top_k=3, metadata_filter=filter_dict)
        else:
            results = store.search(question, top_k=3)

        print("    --- Top-3 Chunks Retrieved ---")
        for rank, res in enumerate(results, 1):
            score = res["score"]
            doc_id = res["metadata"].get("doc_id", res.get("id"))
            preview = res["content"][:100].replace("\n", " ").strip()
            print(f"    {rank}. score={score:.4f} | doc_id={doc_id}")
            print(f"       preview: {preview}...")

        print("    --- Agent Answer Preview ---")
        answer = agent.answer(question, top_k=3)
        print(f"    {answer}")
        print("-" * 70)

    return 0


if __name__ == "__main__":
    data_dir = os.getenv("LAB_DATA_DIR", DEFAULT_DATA_DIR)
    raise SystemExit(run_benchmark(data_dir))
