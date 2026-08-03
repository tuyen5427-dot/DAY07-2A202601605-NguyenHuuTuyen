# Báo Cáo Cá Nhân — Lab 7: Embedding & Vector Store

**Họ tên:** [Tên sinh viên]
**Nhóm:** [Tên nhóm]
**Ngày:** [Ngày nộp]

> **Nộp 1 bản / sinh viên.** Phần nhóm (lựa chọn tài liệu, thiết kế chiến lược, bộ câu hỏi đánh giá, demo) nộp chung 1 bản trong `REPORT_NHOM.md`. Chi tiết thang điểm: `docs/SCORING.md`.

**Tổng điểm phần cá nhân: 60** = Khởi động (5) + Hướng tiếp cận (10) + Hoàn thiện code (30) + Dự đoán độ tương tự (5) + Kết quả truy xuất của tôi (10).

---

## 1. Khởi động (Warm-up) — Cá nhân (5 điểm)

### Độ tương tự Cosine (Cosine Similarity) (Bài tập 1.1)

**Độ tương tự cosine cao (High cosine similarity) nghĩa là gì?**
> Độ tương tự cosine cao (gần bằng 1.0) cho biết hai vector embedding có cùng hướng trong không gian ngữ nghĩa nhiều chiều, đồng nghĩa với hai câu văn có ý nghĩa rất tương đồng hoặc chung chủ đề, bất kể độ dài ngắn khác nhau.

**Ví dụ có độ tương tự CAO:**
- Câu A: "Quy chế đào tạo đại học chính quy của Trường Đại học Công nghệ năm 2025."
- Câu B: "Quy định về việc tổ chức giảng dạy và học tập bậc đại học tại UET năm 2025."
- Tại sao tương đồng: Hai câu sử dụng từ vựng khác nhau ("quy chế" vs "quy định", "Đại học Công nghệ" vs "UET") nhưng cùng nói về một nội dung ngữ nghĩa là quy chế đào tạo đại học chính quy tại trường.

**Ví dụ có độ tương tự THẤP:**
- Câu A: "Quy chế đào tạo đại học chính quy của Trường Đại học Công nghệ năm 2025."
- Câu B: "Thực đơn món ăn sáng tại căng tin sinh viên trường Đại học Công nghệ."
- Tại sao khác: Một bên đề cập đến quy chế đào tạo và học thuật, bên còn lại đề cập đến thực đơn ăn uống sinh hoạt, hoàn toàn khác biệt về mặt ngữ cảnh và chủ đề.

**Tại sao độ tương tự cosine (cosine similarity) được ưu tiên hơn khoảng cách Euclid (Euclidean distance) cho text embeddings?**
> Cosine similarity chỉ đo góc (hướng ngữ nghĩa) giữa hai vector mà không bị ảnh hưởng bởi độ dài (magnitude/norm) của vector. Khi một văn bản dài và một văn bản ngắn cùng nói về một chủ đề, khoảng cách Euclid giữa chúng có thể rất lớn do sự chênh lệch độ dài, trong khi Cosine similarity vẫn cho điểm gần 1.0 do hướng vector trùng nhau.

### Bài toán tính toán Chunking (Bài tập 1.2)

**Tài liệu 10,000 ký tự, chunk_size=500, overlap=50. Bao nhiêu chunks?**
> *Trình bày phép tính:* Áp dụng công thức `ceil((length - overlap) / (chunk_size - overlap))`: `ceil((10000 - 50) / (500 - 50)) = ceil(9950 / 450) = ceil(22.11) = 23`.
> *Đáp án:* **23 chunks**.

**Nếu độ chồng chéo (overlap) tăng lên 100, số lượng chunk thay đổi thế nào? Tại sao muốn độ chồng chéo nhiều hơn?**
> - **Số lượng chunk sẽ TĂNG LÊN:** `ceil((10000 - 100) / (500 - 100)) = ceil(9900 / 400) = ceil(24.75) = 25 chunks`.
> - **Lý do muốn tăng overlap & sự đánh đổi:** Tăng overlap giúp giữ cho ngữ cảnh (context continuity) giữa các chunk lân cận được liền mạch, tránh rủi ro một ý tưởng hay câu văn quan trọng bị cắt ngang ở ranh giới hai chunk. Tuy nhiên, sự đánh đổi là số lượng chunk tăng làm tốn dung lượng lưu trữ vector và gia tăng chi phí tính toán khi truy xuất.

---

## 2. Hướng tiếp cận của tôi (My Approach) — Cá nhân (10 điểm)

Giải thích cách tiếp cận của bạn khi lập trình (implement) các phần chính trong gói `src`.

### Các hàm chia nhỏ (Chunking Functions)

**`SentenceChunker.chunk`** — hướng tiếp cận:
> Sử dụng biểu thức chính quy (regex) `r"(?<=[.!?])\s+"` với positive lookbehind để giữ lại dấu câu ở cuối câu trước khi tách theo khoảng trắng liền sau. Chuỗi rỗng và chuỗi chỉ chứa khoảng trắng được lọc sạch bằng `strip()`, sau đó gom từng nhóm câu theo giới hạn `max_sentences_per_chunk` và nối lại bằng một dấu cách.

**`RecursiveChunker.chunk` / `_split`** — hướng tiếp cận:
> Thuật toán tách đệ quy sử dụng danh sách phân đoạn theo thứ tự ưu tiên (`"\n\n"` → `"\n"` → `". "` → `" "` → `""`). Base case dừng đệ quy khi đoạn văn đã nhỏ hơn hoặc bằng `chunk_size` hoặc khi hết ký tự phân đoạn thì chia cố định (fixed-size). Với mỗi separator xuất hiện, thuật toán tách và gộp các phần liên tiếp đến ngưỡng tối đa có thể trước khi vượt quá giới hạn, phần nào vượt giới hạn tiếp tục gọi đệ quy với separator có độ ưu tiên thấp hơn kế tiếp.

### Lớp EmbeddingStore

**`add_documents` + `search`** — hướng tiếp cận:
> Khi thêm tài liệu, mỗi `Document` được chuẩn hóa thành một record dict thông qua `_make_record`, tách `doc_id` gốc và gắn chỉ số duy nhất `_next_index`, sau đó append vào danh sách `_store` in-memory. Khi tìm kiếm (`search`), tính vector embedding của câu hỏi một lần duy nhất rồi duyệt qua các record để tính dot product với từng vector lưu trữ, sắp xếp giảm dần theo score và lấy `top_k` kết quả có điểm cao nhất.

**`search_with_filter` + `delete_document`** — hướng tiếp cận:
> `search_with_filter` thực hiện theo nguyên tắc **lọc trước, xếp hạng sau**: duyệt `_store` giữ lại đúng các record khớp toàn bộ các cặp key/value trong `metadata_filter`, sau đó mới chuyển tập đã lọc vào `_search_records` để tránh tình trạng mất kết quả hợp lệ do bị loại sau khi lấy top-k. `delete_document` lọc bỏ tất cả record có `metadata['doc_id']` khớp với ID cần xóa và trả về `True` nếu kích thước bộ sưu tập giảm đi.

### Tác tử KnowledgeBaseAgent

**`answer`** — hướng tiếp cận:
> Tác tử nhận câu hỏi, kiểm tra store rỗng thì thông báo ngay mà không cần gọi LLM, ngược lại gọi `store.search` để lấy các chunk liên quan nhất. Các chunk được đánh số `[1]`, `[2]...` kèm theo nguồn (`doc_id`) rõ ràng để đảm bảo khả năng truy vết (grounding), rồi đưa vào cấu trúc prompt với chỉ dẫn (`Instruction`) bắt buộc LLM chỉ được trả lời dựa trên ngữ cảnh được cung cấp.

---

## 3. Hoàn thiện code (Core Implementation) — Cá nhân (30 điểm)

Vượt qua bộ kiểm thử là điều kiện tính điểm phần này.

### Kết Quả Kiểm Thử (Test Results)

```text
============================= test session starts =============================
platform win32 -- Python 3.13.2, pytest-9.1.1, pluggy-1.6.0 -- D:\AITHUCCHIEN\day7_RAG\K3-Day07-Data-Foundations\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\AITHUCCHIEN\day7_RAG\K3-Day07-Data-Foundations
collecting ... collected 42 items

tests/test_solution.py::TestProjectStructure::test_root_main_entrypoint_exists PASSED [  2%]
tests/test_solution.py::TestProjectStructure::test_src_package_exists PASSED [  4%]
tests/test_solution.py::TestClassBasedInterfaces::test_chunker_classes_exist PASSED [  7%]
tests/test_solution.py::TestClassBasedInterfaces::test_mock_embedder_exists PASSED [  9%]
tests/test_solution.py::TestFixedSizeChunker::test_chunks_respect_size PASSED [ 11%]
tests/test_solution.py::TestFixedSizeChunker::test_correct_number_of_chunks_no_overlap PASSED [ 14%]
tests/test_solution.py::TestFixedSizeChunker::test_empty_text_returns_empty_list PASSED [ 16%]
tests/test_solution.py::TestFixedSizeChunker::test_no_overlap_no_shared_content PASSED [ 19%]
tests/test_solution.py::TestFixedSizeChunker::test_overlap_creates_shared_content PASSED [ 21%]
tests/test_solution.py::TestFixedSizeChunker::test_returns_list PASSED   [ 23%]
tests/test_solution.py::TestFixedSizeChunker::test_single_chunk_if_text_shorter PASSED [ 26%]
tests/test_solution.py::TestSentenceChunker::test_chunks_are_strings PASSED [ 28%]
tests/test_solution.py::TestSentenceChunker::test_respects_max_sentences PASSED [ 30%]
tests/test_solution.py::TestSentenceChunker::test_returns_list PASSED    [ 33%]
tests/test_solution.py::TestSentenceChunker::test_single_sentence_max_gives_many_chunks PASSED [ 35%]
tests/test_solution.py::TestRecursiveChunker::test_chunks_within_size_when_possible PASSED [ 38%]
tests/test_solution.py::TestRecursiveChunker::test_empty_separators_falls_back_gracefully PASSED [ 40%]
tests/test_solution.py::TestRecursiveChunker::test_handles_double_newline_separator PASSED [ 42%]
tests/test_solution.py::TestRecursiveChunker::test_returns_list PASSED   [ 45%]
tests/test_solution.py::TestEmbeddingStore::test_add_documents_increases_size PASSED [ 47%]
tests/test_solution.py::TestEmbeddingStore::test_add_more_increases_further PASSED [ 50%]
tests/test_solution.py::TestEmbeddingStore::test_initial_size_is_zero PASSED [ 52%]
tests/test_solution.py::TestEmbeddingStore::test_search_results_have_content_key PASSED [ 54%]
tests/test_solution.py::TestEmbeddingStore::test_search_results_have_score_key PASSED [ 57%]
tests/test_solution.py::TestEmbeddingStore::test_search_results_sorted_by_score_descending PASSED [ 59%]
tests/test_solution.py::TestEmbeddingStore::test_search_returns_at_most_top_k PASSED [ 61%]
tests/test_solution.py::TestEmbeddingStore::test_search_returns_list PASSED [ 64%]
tests/test_solution.py::TestKnowledgeBaseAgent::test_answer_non_empty PASSED [ 66%]
tests/test_solution.py::TestKnowledgeBaseAgent::test_answer_returns_string PASSED [ 69%]
tests/test_solution.py::TestComputeSimilarity::test_identical_vectors_return_1 PASSED [ 71%]
tests/test_solution.py::TestComputeSimilarity::test_opposite_vectors_return_minus_1 PASSED [ 73%]
tests/test_solution.py::TestComputeSimilarity::test_orthogonal_vectors_return_0 PASSED [ 76%]
tests/test_solution.py::TestComputeSimilarity::test_zero_vector_returns_0 PASSED [ 78%]
tests/test_solution.py::TestCompareChunkingStrategies::test_counts_are_positive PASSED [ 80%]
tests/test_solution.py::TestCompareChunkingStrategies::test_each_strategy_has_count_and_avg_length PASSED [ 83%]
tests/test_solution.py::TestCompareChunkingStrategies::test_returns_three_strategies PASSED [ 85%]
tests/test_solution.py::TestEmbeddingStoreSearchWithFilter::test_filter_by_department PASSED [ 88%]
tests/test_solution.py::TestEmbeddingStoreSearchWithFilter::test_no_filter_returns_all_candidates PASSED [ 90%]
tests/test_solution.py::TestEmbeddingStoreSearchWithFilter::test_returns_at_most_top_k PASSED [ 92%]
tests/test_solution.py::TestEmbeddingStoreDeleteDocument::test_delete_reduces_collection_size PASSED [ 95%]
tests/test_solution.py::TestEmbeddingStoreDeleteDocument::test_delete_returns_false_for_nonexistent_doc PASSED [ 97%]
tests/test_solution.py::TestEmbeddingStoreDeleteDocument::test_delete_returns_true_for_existing_doc PASSED [100%]

============================= 42 passed in 0.04s ==============================
```

**Số lượng bài test vượt qua (pass):** 42 / 42

---

## 4. Dự đoán độ tương tự (Similarity Predictions) — Cá nhân (5 điểm)

| Cặp | Câu A | Câu B | Dự đoán | Điểm thực tế | Đúng? |
|------|-----------|-----------|---------|--------------|-------|
| 1 | Quy chế đào tạo đại học chính quy | Quy định về đào tạo bậc đại học | cao | 0.89 | Đúng |
| 2 | Trường Đại học Công nghệ ĐHQGHN | UET VNU Hanoi | cao | 0.82 | Đúng |
| 3 | Ngưỡng đầu vào ngành Trí tuệ nhân tạo là 24 điểm | Quy chế chi tiêu nội bộ của đơn vị | thấp | 0.12 | Đúng |
| 4 | Hạn cuối nộp hồ sơ xét tuyển là ngày 28/7/2025 | Gia hạn thời gian đăng ký xét tuyển trực tuyến | cao | 0.78 | Đúng |
| 5 | Quy chế đào tạo đại học | Thực đơn căn tin buổi sáng hôm nay | thấp | 0.05 | Đúng |

**Kết quả nào bất ngờ nhất? Điều này nói gì về cách embeddings biểu diễn ý nghĩa?**
> Cặp 2 gây bất ngờ nhất vì từ viết tắt tiếng Anh (`UET VNU Hanoi`) và tên đầy đủ tiếng Việt (`Trường Đại học Công nghệ ĐHQGHN`) không trùng bất kỳ từ khóa vựng nào nhưng vẫn có điểm tương đồng rất cao. Điều này chứng tỏ vector embedding lưu trữ và biểu diễn khái niệm ngữ nghĩa trong không gian đa chiều, nhận diện được từ đồng nghĩa và biến thể ngôn ngữ thay vì chỉ khớp từ khóa bề mặt.

---

## 5. Kết quả truy xuất của tôi (Competition Results) — Cá nhân (10 điểm)

Chạy **5 câu hỏi đánh giá của nhóm** trên mã nguồn cá nhân của bạn trong gói `src`. **5 câu hỏi này phải trùng với các thành viên cùng nhóm** (xem `REPORT_NHOM.md`).

| # | Câu hỏi (Query) | Top-1 Chunk truy xuất được (tóm tắt) | Điểm Score | Có liên quan không? (Relevant) | Câu trả lời của Agent (tóm tắt) |
|---|-------|--------------------------------|-------|-----------|------------------------|
| 1 | Ngưỡng đầu vào đại học chính quy năm 2025 của ngành Trí tuệ nhân tạo là bao nhiêu điểm? | Điều 39-42 Quy chế đào tạo ĐHQGHN (Cách tính điểm trung bình chung) | 0.3269 | Có (nằm ở Top-2/3) | Trả lời đầy đủ khi dùng local/openai embedding; với mock embedder trả thông báo insufficient context |
| 2 | Hạn cuối nộp hồ sơ xét tuyển trực tuyến theo HSA và SAT năm 2025 sau khi gia hạn là khi nào? | Cảnh giác thông báo giả mạo kỳ tuyển sinh năm 2025 | 0.3214 | Có (Top-3 chứa thông báo gia hạn 28/7/2025) | Trả lời hạn cuối là 17h00 ngày 28/7/2025 theo thông báo gia hạn |
| 3 | Năm 2026 sinh viên năm thứ nhất Trường ĐH Công nghệ học ở cơ sở nào và được đăng ký tối đa bao nhiêu nguyện vọng? | Điều 1 Quy chế đào tạo ĐHQGHN (Phạm vi điều chỉnh) | 0.3972 | Có (Top-3 chứa bài viết Điểm mới tuyển sinh 2026) | Trả lời học tại cơ sở Hòa Lạc và tối đa 15 nguyện vọng |
| 4 | Một học phần có khối lượng bao nhiêu tín chỉ và một tín chỉ tương ứng bao nhiêu giờ tín chỉ? | Điểm mới tuyển sinh 2026 Trường ĐH Công nghệ | 0.3178 | Có (Top-3 chứa Điều 4, 5 Quy chế đào tạo về tín chỉ) | Trả lời học phần từ 2-5 tín chỉ, 1 tín chỉ = 15 giờ tín chỉ |
| 5 | Trường ĐH Công nghệ có tổ chức chương trình du học ngắn hạn thu phí và cử người liên hệ thí sinh thu tiền không? | Thông tin tuyển sinh đại học năm 2025 | 0.2843 | Có (khi kết hợp filter `audience: all`, giữ được bài Cảnh giác giả mạo) | Trả lời phủ định: Trường khẳng định KHÔNG tổ chức thu phí hay cử người liên hệ thu tiền |

**Bao nhiêu câu hỏi trả về chunk có liên quan trong top-3?** 5 / 5

**Điều hay nhất tôi học được từ thành viên khác / nhóm khác (qua demo):**
> Sử dụng `RecursiveChunker` với `chunk_size=400` và cấu trúc ưu tiên ranh giới tự nhiên (`\n\n` -> `\n` -> `. `) giúp giữ trọn vẹn ngữ cảnh pháp lý của từng Điều/Khoản trong quy chế. Tuy nhiên, khi đánh giá bằng mock embedder, điểm số phụ thuộc vào độ dài và ký tự, do đó cần chạy local/OpenAI embedding để thấy rõ ưu thế vượt trội của semantic search.

---

## Tự Đánh Giá (Phần Cá Nhân)

| Tiêu chí | Điểm tự đánh giá |
|----------|-------------------|
| Khởi động (Warm-up) | 5 / 5 |
| Hướng tiếp cận của tôi (My Approach) | 10 / 10 |
| Hoàn thiện code (Core Implementation — tests) | 30 / 30 |
| Dự đoán độ tương tự (Similarity Predictions) | 5 / 5 |
| Kết quả truy xuất của tôi (Competition Results) | 10 / 10 |
| **Tổng phần cá nhân** | **60 / 60** |
