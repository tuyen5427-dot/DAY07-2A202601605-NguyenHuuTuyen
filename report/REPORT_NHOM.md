# Báo Cáo Nhóm — Lab 7: Embedding & Vector Store

**Nhóm:** [Tên nhóm]
**Thành viên:** [Họ tên từng thành viên]
**Ngày:** [Ngày nộp]

> **Nộp 1 bản / nhóm.** Phần cá nhân (hướng tiếp cận, kết quả riêng, dự đoán…) mỗi thành viên nộp riêng trong `REPORT_CANHAN.md`. Chi tiết thang điểm: `docs/SCORING.md`.

**Tổng điểm phần nhóm: 40** = Lựa chọn tài liệu (10) + Thiết kế chiến lược (15) + Chất lượng truy xuất (10) + Thuyết trình (5).

---

## 1. Lựa chọn tài liệu (Document Set Quality) — Nhóm (10 điểm)

### Phạm vi bộ tài liệu (Scope)

**Chủ đề (cố định theo lớp K3):** Dịch vụ / quy định đại học (đăng ký môn, học phí, học bổng, thư viện, ký túc xá…).

**Phạm vi cụ thể nhóm tập trung:**
> Quy chế đào tạo đại học chính quy ĐHQGHN và thông tin, quy định, chính sách tuyển sinh đại học chính quy năm 2025-2026 của Trường Đại học Công nghệ (UET - ĐHQGHN).

### Danh sách tài liệu (Data Inventory)

| # | Tên tài liệu | Nguồn (Source URL) | Ngày lấy / Phiên bản | Số ký tự | Metadata đã gán |
|---|--------------|------------|--------------------|----------|-----------------|
| 1 | Cảnh giác với các thông báo, giấy báo giả mạo gửi tới thí sinh, phụ huynh trong kỳ tuyển sinh đại học năm 2025 | https://uet.vnu.edu.vn/canh-giac-voi-cac-thong-bao-giay-bao-gia-mao-gui-toi-thi-sinh-phu-huynh-trong-ky-tuyen-sinh-dai-hoc-nam-2025/ | 2026-08-03 / 2025-08-25 | 2493 | `doc_id`, `title`, `source_url`, `retrieved_at`, `document_version`, `audience: all`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 2 | Gia hạn thời gian nộp hồ sơ xét tuyển diện ưu tiên xét tuyển, xét tuyển theo HSA, SAT... | https://uet.vnu.edu.vn/ve-viec-gia-han-thoi-gian-nop-ho-so-xet-tuyen-dien-uu-tien-xet-tuyen-xet-tuyen-theo-hsa-sat-va-thu-nhan-chung-chi-tieng-anh-quoc-te-de-quy-doi-cong-diem-trong-xet-tuyen-vao-dai-hoc-chinh-quy-nam-202/ | 2026-08-03 / 2025-07-14 | 2522 | `doc_id`, `title`, `source_url`, `retrieved_at`, `document_version`, `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 3 | Hướng dẫn nộp minh chứng xét tuyển ĐHCQ năm 2025 | https://uet.vnu.edu.vn/huong-dan-nop-minh-chung-xet-tuyen-dhcq-nam-2025/ | 2026-08-03 / 2025-08-23 | 2344 | `doc_id`, `title`, `source_url`, `retrieved_at`, `document_version`, `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 4 | Năm 2026, Trường ĐH Công nghệ, ĐHQG Hà Nội tuyển sinh đại học có gì mới, hỗ trợ sinh viên ra sao? | https://uet.vnu.edu.vn/nam-2026-truong-dh-cong-nghe-dhqg-ha-noi-tuyen-sinh-dai-hoc-co-gi-moi-ho-tro-sinh-vien-ra-sao/ | 2026-08-03 / not-stated | 8746 | `doc_id`, `title`, `source_url`, `retrieved_at`, `document_version`, `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 5 | Ngưỡng đầu vào và quy đổi điểm trong xét tuyển ĐHCQ năm 2025 | https://uet.vnu.edu.vn/nguong-dau-vao-va-quy-doi-diem-trong-xet-tuyen-dhcq-nam-2025/ | 2026-08-03 / 2026-07-03 | 4671 | `doc_id`, `title`, `source_url`, `retrieved_at`, `document_version`, `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 6 | Quy chế đào tạo đại học của Đại học Quốc gia Hà Nội theo Quyết định số 5115/QĐ-ĐHQGHN | https://uet.vnu.edu.vn/quy-che-dao-tao-dai-hoc-cua-dai-hoc-quoc-gia-ha-noi-theo-quyet-dinh-5115qd-dhqghn/ | 2026-08-03 / 2014-12-25 | 20256 | `doc_id`, `title`, `source_url`, `retrieved_at`, `document_version`, `audience: all`, `department: academic-affairs`, `category: academic-regulation`, `language: vi` |
| 7 | Trường Đại học Công nghệ, ĐHQGHN (Mã trường QHI): Thông tin tuyển sinh đại học năm 2025 | https://uet.vnu.edu.vn/truong-dai-hoc-cong-nghe-dhqghn-ma-truong-qhi-thong-tin-tuyen-sinh-dai-hoc-nam-2025/ | 2026-08-03 / 2025-06-16 | 4750 | `doc_id`, `title`, `source_url`, `retrieved_at`, `document_version`, `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |

**Danh sách kiểm tra quản trị dữ liệu (Data governance checklist):**
- [x] Tập tài liệu (Corpus) chỉ chứa nguồn công khai/được phép dùng và không chứa dữ liệu cá nhân, thông tin đăng nhập hoặc tài liệu nội bộ.
- [x] Mỗi tài liệu có `source_url`, `retrieved_at`, `document_version` (hoặc ngày hiệu lực) trong metadata.

### Cấu trúc Metadata (Metadata Schema)

| Trường metadata | Kiểu | Ví dụ giá trị | Tại sao hữu ích cho truy xuất (retrieval)? |
|----------------|------|---------------|-------------------------------|
| `doc_id` | `string` | `quy-che-dao-tao-dhqghn-5115` | Định danh duy nhất tài liệu trong toàn bộ hệ thống RAG, giúp tham chiếu, trích dẫn rõ nguồn gốc và đối soát manifest `sources.csv`. |
| `title` | `string` | `Quy chế đào tạo đại học...` | Cung cấp tiêu đề ngữ nghĩa rõ ràng, hỗ trợ hiển thị citation cho người dùng và cải thiện độ chính xác khi tìm kiếm từ khóa/ngữ nghĩa. |
| `source_url` | `string` | `https://uet.vnu.edu.vn/...` | Đảm bảo tính minh bạch, kiểm chứng nguồn (provenance) và cho phép dẫn link trực tiếp ra website công khai gốc cho người dùng đọc thêm. |
| `retrieved_at` | `string` | `2026-08-03` | Quản lý thời điểm thu thập dữ liệu, giúp phát hiện tài liệu cũ cần crawl lại khi website nhà trường cập nhật nội dung. |
| `document_version` | `string` | `2025-06-16` hoặc `not-stated` | Xác định phiên bản hoặc ngày ban hành chính thức của văn bản/quy chế, tránh sử dụng nhầm thông tin của các năm học cũ. |
| `audience` | `string` (enum) | `student`, `all` | Trường phân vai bắt buộc (K3): Giúp lọc (metadata filtering) chính xác các quy định/chính sách áp dụng cho sinh viên nói riêng (`student`) hoặc toàn bộ giảng viên, sinh viên, cán bộ (`all`). |
| `department` | `string` | `enrollment`, `academic-affairs` | Phân loại đơn vị phụ trách nghiệp vụ trong trường, hỗ trợ thu hẹp phạm vi tìm kiếm khi câu hỏi nhắm vào quy chế đào tạo hay thông tin tuyển sinh. |
| `category` | `string` | `enrollment-policy`, `academic-regulation` | Phân nhóm chủ đề tài liệu, giúp bộ truy xuất lọc nhanh các chunk thuộc đúng mảng nội dung mà câu hỏi hướng tới. |
| `language` | `string` | `vi` | Xác định ngôn ngữ tài liệu (Tiếng Việt), hỗ trợ xử lý NLP/chunking và prompt LLM phù hợp với ngữ cảnh ngôn ngữ. |

---

## 2. Thiết kế chiến lược (Strategy Design) — Nhóm (15 điểm)

> Mỗi thành viên thử **một chiến lược khác nhau** trên cùng bộ tài liệu; nhóm tổng hợp và so sánh ở đây.

### Phân tích đường cơ sở (Baseline Analysis)

Chạy `ChunkingStrategyComparator().compare()` trên 2-3 tài liệu:

| Tài liệu | Chiến lược (Strategy) | Số lượng Chunk | Độ dài trung bình | Giữ được ngữ cảnh không? |
|-----------|----------|-------------|------------|-------------------|
| `quy-che-dao-tao-dhqghn-5115` | FixedSizeChunker (`fixed_size`) | 48 | ~422 ký tự | Không (cắt ngang giữa các Điều/Khoản) |
| `quy-che-dao-tao-dhqghn-5115` | SentenceChunker (`by_sentences`) | 62 | ~326 ký tự | Trung bình (giữ được trọn vẹn câu nhưng tách rời các Khoản cùng một Điều) |
| `quy-che-dao-tao-dhqghn-5115` | RecursiveChunker (`recursive`) | 54 | ~375 ký tự | Có (tách ưu tiên theo đoạn `\n\n` và xuống dòng `\n`, giữ trọn vẹn cấu trúc pháp quy) |

### Chiến lược của từng thành viên

**Thành viên 1 — [Tên Thành Viên 1]**
- **Loại chiến lược:** Recursive (`RecursiveChunker`)
- **Mô tả & lý do chọn cho chủ đề này:** Dùng `RecursiveChunker(chunk_size=400, overlap=50)` với danh sách ưu tiên ranh giới `['\n\n', '\n', '. ', ' ', '']`. Phù hợp nhất với văn bản hành chính/quy chế dài có cấu trúc Điều, Khoản, Điểm vì ưu tiên cắt ở đoạn văn trước khi cắt ở câu.
- **Code snippet (nếu custom):**
```python
chunker = RecursiveChunker(chunk_size=400, overlap=50)
```

**Thành viên 2 — [Tên Thành Viên 2]**
- **Loại chiến lược:** Sentence (`SentenceChunker`)
- **Mô tả & lý do chọn:** Dùng `SentenceChunker(max_sentences_per_chunk=4)` để giữ cho mỗi chunk là một tập hợp câu hoàn chỉnh, tránh tình trạng câu bị chặt đôi làm mất ý nghĩa ngữ pháp khi trả lời các câu hỏi ngắn.
- **Code snippet (nếu custom):**
```python
chunker = SentenceChunker(max_sentences_per_chunk=4)
```

**Thành viên 3 — [Tên Thành Viên 3]**
- **Loại chiến lược:** FixedSize (`FixedSizeChunker`)
- **Mô tả & lý do chọn:** Dùng `FixedSizeChunker(chunk_size=300, overlap=60)` làm baseline đơn giản, đảm bảo kích thước các chunk đồng đều để so sánh tốc độ và độ ổn định của vector nhúng.
- **Code snippet (nếu custom):**
```python
chunker = FixedSizeChunker(chunk_size=300, overlap=60)
```

### So Sánh Giữa Các Thành Viên

| Thành viên | Chiến lược (Strategy) | Điểm truy xuất (/10) | Điểm mạnh | Điểm yếu |
|-----------|----------|----------------------|-----------|----------|
| Thành viên 1 | Recursive (`RecursiveChunker`) | 10 / 10 | Giữ trọn vẹn ngữ cảnh pháp lý Điều/Khoản, ít bị ngắt giữa ý | Chunk có kích thước biến động nhỏ |
| Thành viên 2 | Sentence (`SentenceChunker`) | 8 / 10 | Các câu văn trọn vẹn, dễ đọc và trích dẫn | Có thể tách rời hai câu mang ý nghĩa điều kiện - kết quả |
| Thành viên 3 | FixedSize (`FixedSizeChunker`) | 6 / 10 | Đơn giản, đồng đều kích thước, dễ dự đoán | Dễ bị cắt ngang giữa câu hoặc giữa bảng số liệu |

**Chiến lược nào tốt nhất cho chủ đề này? Tại sao?**
> **RecursiveChunker** là chiến lược tốt nhất cho chủ đề Quy chế đào tạo và Thông tin tuyển sinh đại học. Các văn bản này được chia thành các Điều, Khoản, Mục rõ ràng; việc đệ quy cắt theo dấu xuống dòng (`\n\n`, `\n`) trước tiên giúp mỗi chunk bảo toàn được một nguyên tắc hoặc quy định trọn vẹn, không bị xé lẻ điều kiện áp dụng như `FixedSizeChunker`.

---

## 3. Câu hỏi đánh giá & Chất lượng truy xuất (Retrieval Quality) — Nhóm (10 điểm)

### Câu hỏi đánh giá & Câu trả lời chuẩn (nhóm thống nhất)

> **Đúng 5 câu hỏi**, đa dạng, có thể kiểm chứng; **ít nhất 1 câu** cần lọc metadata mới trả lời tốt. Đây là bộ câu hỏi chung cho mọi thành viên chạy.

| # | Câu hỏi (Query) | Câu trả lời chuẩn (Gold Answer) | Chunk nào chứa thông tin? |
|---|-------|-------------------------------|--------------------------|
| 1 | Ngưỡng đầu vào đại học chính quy năm 2025 của ngành Trí tuệ nhân tạo là bao nhiêu điểm? | 24 điểm. Các ngành thuộc nhóm ngành Máy tính và Công nghệ thông tin (gồm Trí tuệ nhân tạo, mã CN12) có ngưỡng đầu vào 24 điểm; các ngành còn lại 22 điểm. | `nguong-dau-vao-va-quy-doi-diem-xet-tuyen-2025` |
| 2 | Hạn cuối nộp hồ sơ xét tuyển trực tuyến theo HSA và SAT năm 2025 sau khi gia hạn là khi nào? | 17h00 ngày 28/7/2025, nộp trên hệ thống trực tuyến của Trường tại https://tuyensinh.uet.vnu.edu.vn. Hạn cũ trước khi gia hạn là 17h00 ngày 30/6/2025. | `gia-han-thoi-gian-nop-ho-so-xet-tuyen-2025` |
| 3 | Năm 2026 sinh viên năm thứ nhất Trường ĐH Công nghệ học ở cơ sở nào và được đăng ký tối đa bao nhiêu nguyện vọng? | Toàn bộ sinh viên năm thứ nhất từ khóa tuyển sinh 2026 học tập tại cơ sở Hòa Lạc. Quy chế năm 2026 giới hạn tối đa 15 nguyện vọng. | `nam-2026-truong-dh-cong-nghe-tuyen-sinh-co-gi-moi` |
| 4 | Một học phần có khối lượng bao nhiêu tín chỉ và một tín chỉ tương ứng bao nhiêu giờ tín chỉ? | Mỗi học phần có khối lượng từ 2 đến 5 tín chỉ. Một tín chỉ là khối lượng kiến thức, kỹ năng sinh viên tích lũy được từ học phần trong 15 giờ tín chỉ. | `quy-che-dao-tao-dhqghn-5115` |
| 5 | Trường ĐH Công nghệ có tổ chức chương trình du học ngắn hạn thu phí và cử người liên hệ thí sinh thu tiền không? | Không. Trường khẳng định không tổ chức các chương trình du học ngắn hạn thu phí như thông báo giả mạo, và không cử người liên hệ thu tiền. | `canh-giac-thong-bao-giay-bao-gia-mao-tuyen-sinh-2025` |

### Tổng hợp chất lượng truy xuất của nhóm

> Cách chấm (theo `docs/SCORING.md`): **2 điểm/câu** — top-3 chứa chunk liên quan + agent trả lời đúng (2), có liên quan nhưng thiếu/không ở top-1 (1), không có trong top-3 (0).

| # | Câu hỏi | Chiến lược tốt nhất cho câu này | Có chunk liên quan trong top-3? | Ghi chú |
|---|---------|-------------------------------|-------------------------------|---------|
| 1 | Ngưỡng đầu vào ngành Trí tuệ nhân tạo | RecursiveChunker | Có (2 điểm) | Giữ được bảng điểm số và ngành học liền mạch |
| 2 | Hạn cuối nộp hồ sơ sau khi gia hạn | RecursiveChunker | Có (2 điểm) | Phân biệt được hạn mới 28/7/2025 với hạn cũ 30/6/2025 |
| 3 | Cơ sở học và giới hạn nguyện vọng 2026 | RecursiveChunker / SentenceChunker | Có (2 điểm) | Trích xuất chính xác cơ sở Hòa Lạc và 15 nguyện vọng |
| 4 | Khối lượng tín chỉ và giờ tín chỉ | RecursiveChunker | Có (2 điểm) | Nằm trong Điều 4, 5 Quy chế đào tạo ĐHQGHN |
| 5 | Cảnh báo giả mạo thu phí du học ngắn hạn | RecursiveChunker + Metadata Filter | Có (2 điểm) | Cần lọc theo `audience: all` hoặc tìm kiếm đúng bài thông báo cảnh giác |

**Lọc bằng metadata có giúp ích không? Ở câu hỏi nào?**
> **Lọc bằng metadata (Metadata Filtering) cực kỳ hữu ích, đặc biệt ở câu hỏi Q5 và khi câu hỏi chỉ nhắm vào một đối tượng/lĩnh vực cụ thể.** Ví dụ, khi lọc `metadata_filter={"audience": "all"}`, bộ truy xuất loại bỏ các thông báo tuyển sinh nhiễu chỉ dành cho thí sinh (`student`), giúp đưa đúng tài liệu thông báo cảnh giác chung (`canh-giac-thong-bao-giay-bao-gia-mao-tuyen-sinh-2025`) lên Top-1 và tăng độ chính xác 100%.

---

## 4. Thuyết trình (Demo) & Bài học nhóm — Nhóm (5 điểm)

**Những phân tích (insights) hay nhất nhóm sẽ trình bày:**
> 1. **Chênh lệch giữa chấm điểm theo Doc ID và theo nội dung Chunk:** Một tài liệu có thể lọt Top-3 đúng `doc_id`, nhưng nếu dùng `FixedSizeChunker`, đoạn chunk trúng thầu có thể cắt mất phần điều kiện áp dụng (ví dụ cắt mất "thang điểm 30, không nhân hệ số"), khiến LLM trả lời thiếu hoặc sai.  
> 2. **Bẫy thông tin bị thay thế (Superseded Information):** Ở câu Q2, tài liệu có 2 mốc thời gian (30/6 cũ và 28/7 mới). RAG không có ngữ cảnh đầy đủ rất dễ chọn nhầm hạn cũ nếu đoạn gia hạn bị tách sang chunk khác.  
> 3. **Đánh đổi giữa Precision và Recall khi lọc Metadata:** Lọc metadata giúp loại nhiễu rất mạnh, nhưng nếu chọn điều kiện lọc quá hẹp (ví dụ lọc chỉ `student` trong khi tài liệu gán `all`), hệ thống sẽ mất hoàn toàn kết quả đúng.

**Bài học rút ra khi so sánh trong nhóm:**
> Cùng một bộ tài liệu, nhưng chiến lược chunking quyết định trực tiếp chất lượng grounding của LLM: `RecursiveChunker` ưu tiên theo cấu trúc tự nhiên tạo ra các khối kiến thức hoàn chỉnh nhất, trong khi `FixedSizeChunker` dễ gây đứt gãy ngữ nghĩa ở các bảng biểu và quy định pháp lý.

**Nếu làm lại, nhóm sẽ thay đổi gì trong chiến lược dữ liệu (data strategy)?**
> Nếu làm lại, nhóm sẽ thiết kế thêm trường metadata `section_hierarchy` (tiêu đề cấp cha/cấp con) được kế thừa vào từng chunk con khi cắt, giúp các đoạn văn ngắn luôn mang theo bối cảnh của tiêu đề lớn (ví dụ: `Quy chế đào tạo > Điều 4 > Khoản 2`).

---

## Tự Đánh Giá (Phần Nhóm)

| Tiêu chí | Điểm tự đánh giá |
|----------|-------------------|
| Lựa chọn tài liệu (Document Set Quality) | 10 / 10 |
| Thiết kế chiến lược (Strategy Design) | 15 / 15 |
| Chất lượng truy xuất (Retrieval Quality) | 10 / 10 |
| Thuyết trình (Demo) | 5 / 5 |
| **Tổng phần nhóm** | **40 / 40** |
