# Báo Cáo Nhóm — Lab 7: Embedding & Vector Store

**Nhóm:** C2
**Thành viên:** Đậu Quốc Duy (2A202601445) · Lê Chí Anh Tuấn (2A202601149) · Nguyễn Đăng Nam (2A202601307) · Nguyễn Hữu Tuyền (2A202601605) · Tống Nguyễn Minh Khang (2A202601101)
**Ngày:** 2026-08-03

> **Nộp 1 bản / nhóm.** Phần cá nhân (hướng tiếp cận, kết quả riêng, dự đoán…) mỗi thành viên nộp riêng trong `REPORT_CANHAN.md`. Chi tiết thang điểm: `docs/SCORING.md`.

**Tổng điểm phần nhóm: 40** = Lựa chọn tài liệu (10) + Thiết kế chiến lược (15) + Chất lượng truy xuất (10) + Thuyết trình (5).

---

## 1. Lựa chọn tài liệu (Document Set Quality) — Nhóm (10 điểm)

### Phạm vi bộ tài liệu (Scope)

**Chủ đề (cố định theo lớp K3):** Dịch vụ / quy định đại học (đăng ký môn, học phí, học bổng, thư viện, ký túc xá…).

**Phạm vi cụ thể nhóm tập trung:**
> Tuyển sinh đại học chính quy và quy chế đào tạo của Trường ĐH Công nghệ — ĐHQGHN (uet.vnu.edu.vn).

### Danh sách tài liệu (Data Inventory)

| # | Tên tài liệu | Nguồn (Source URL) | Ngày lấy / Phiên bản | Số ký tự | Metadata đã gán |
|---|--------------|------------|--------------------|----------|-----------------|
| 1 | Quy chế đào tạo đại học của ĐHQGHN theo Quyết định số 5115/QĐ-ĐHQGHN | [uet.vnu.edu.vn/quy-che-dao-tao-dai-hoc-…-5115qd-dhqghn](https://uet.vnu.edu.vn/quy-che-dao-tao-dai-hoc-cua-dai-hoc-quoc-gia-ha-noi-theo-quyet-dinh-5115qd-dhqghn/) | 2026-08-03 / 2014-12-25 | 74.661 | `audience: all`, `department: education`, `category: policy`, `language: vi` |
| 2 | Năm 2026, Trường ĐH Công nghệ, ĐHQG Hà Nội tuyển sinh đại học có gì mới, hỗ trợ sinh viên ra sao? | [uet.vnu.edu.vn/nam-2026-truong-dh-cong-nghe-…](https://uet.vnu.edu.vn/nam-2026-truong-dh-cong-nghe-dhqg-ha-noi-tuyen-sinh-dai-hoc-co-gi-moi-ho-tro-sinh-vien-ra-sao/) | 2026-08-03 / not-stated | 8.967 | `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 3 | Trường ĐH Công nghệ, ĐHQGHN (Mã trường QHI): Thông tin tuyển sinh đại học năm 2025 | [uet.vnu.edu.vn/truong-dai-hoc-cong-nghe-dhqghn-ma-truong-qhi-…](https://uet.vnu.edu.vn/truong-dai-hoc-cong-nghe-dhqghn-ma-truong-qhi-thong-tin-tuyen-sinh-dai-hoc-nam-2025/) | 2026-08-03 / 2025-06-16 | 4.485 | `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 4 | Ngưỡng đầu vào và quy đổi điểm trong xét tuyển ĐHCQ năm 2025 | [uet.vnu.edu.vn/nguong-dau-vao-va-quy-doi-diem-…](https://uet.vnu.edu.vn/nguong-dau-vao-va-quy-doi-diem-trong-xet-tuyen-dhcq-nam-2025/) | 2026-08-03 / 2026-07-03 | 4.456 | `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 5 | Hướng dẫn nộp minh chứng xét tuyển ĐHCQ năm 2025 | [uet.vnu.edu.vn/huong-dan-nop-minh-chung-…](https://uet.vnu.edu.vn/huong-dan-nop-minh-chung-xet-tuyen-dhcq-nam-2025/) | 2026-08-03 / 2025-08-23 | 2.117 | `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 6 | Gia hạn thời gian nộp hồ sơ xét tuyển diện ưu tiên xét tuyển, xét tuyển theo HSA, SAT… năm 2025 | [uet.vnu.edu.vn/ve-viec-gia-han-thoi-gian-nop-ho-so-…](https://uet.vnu.edu.vn/ve-viec-gia-han-thoi-gian-nop-ho-so-xet-tuyen-dien-uu-tien-xet-tuyen-xet-tuyen-theo-hsa-sat-va-thu-nhan-chung-chi-tieng-anh-quoc-te-de-quy-doi-cong-diem-trong-xet-tuyen-vao-dai-hoc-chinh-quy-nam-202/) | 2026-08-03 / 2025-07-14 | 2.424 | `audience: student`, `department: enrollment`, `category: enrollment-policy`, `language: vi` |
| 7 | Cảnh giác với các thông báo, giấy báo giả mạo gửi tới thí sinh, phụ huynh trong kỳ tuyển sinh đại học năm 2025 | [uet.vnu.edu.vn/canh-giac-voi-cac-thong-bao-giay-bao-gia-mao-…](https://uet.vnu.edu.vn/canh-giac-voi-cac-thong-bao-giay-bao-gia-mao-gui-toi-thi-sinh-phu-huynh-trong-ky-tuyen-sinh-dai-hoc-nam-2025/) | 2026-08-03 / 2025-08-25 | 2.315 | `audience: all`, `department: enrollment`, `category: warning`, `language: vi` |

*Số ký tự tính trên phần nội dung sau front matter. Kiểm kê một–một trong `data/k3_university/sources.csv`.*

**Danh sách kiểm tra quản trị dữ liệu (Data governance checklist):**
- [x] Tập tài liệu (Corpus) chỉ chứa nguồn công khai/được phép dùng và không chứa dữ liệu cá nhân, thông tin đăng nhập hoặc tài liệu nội bộ.
  *Cả 7 tài liệu lấy từ website công khai uet.vnu.edu.vn, ghi `license_or_permission: public-source`. Thông tin liên hệ trong tài liệu là số điện thoại/email hành chính của Phòng Đào tạo do trường tự công bố, không phải dữ liệu cá nhân.*
- [x] Mỗi tài liệu có `source_url`, `retrieved_at`, `document_version` (hoặc ngày hiệu lực) trong metadata.
  *Tài liệu #2 không nêu ngày ban hành nên để `document_version: not-stated` thay vì suy đoán.*

### Cấu trúc Metadata (Metadata Schema)

| Trường metadata | Kiểu | Ví dụ giá trị | Tại sao hữu ích cho truy xuất (retrieval)? |
|----------------|------|---------------|-------------------------------|
| `doc_id` | string (slug) | `tuyen-sinh-quy-dinh-1` | Khóa định danh duy nhất, trùng tên file. Cho phép truy vết chunk → tài liệu gốc khi trích dẫn nguồn, và gộp/loại trùng các chunk cùng một tài liệu. |
| `title` | string | `Ngưỡng đầu vào và quy đổi điểm trong xét tuyển ĐHCQ năm 2025` | Hiển thị nguồn cho người dùng; có thể prepend vào chunk để giữ ngữ cảnh khi chunk nằm giữa tài liệu dài. |
| `source_url` | string (URL) | `https://uet.vnu.edu.vn/nguong-dau-vao-va-quy-doi-diem-trong-xet-tuyen-dhcq-nam-2025/` | Trích dẫn kiểm chứng được — người dùng tự đối chiếu câu trả lời với văn bản gốc. |
| `retrieved_at` | date (`YYYY-MM-DD`) | `2026-08-03` | Cho biết ảnh chụp dữ liệu cũ đến mức nào, để cảnh báo khi nội dung có thể đã lỗi thời so với nguồn. |
| `document_version` | date \| `not-stated` | `2026-07-03`, `not-stated` | Phân biệt các phiên bản quy định theo năm tuyển sinh. Khi hai tài liệu mâu thuẫn, ưu tiên bản hiệu lực mới hơn thay vì để embedding quyết định ngẫu nhiên. |
| `audience` | enum: `student` \| `faculty` \| `staff` \| `all` | `student`, `all` | **Trường phân vai.** Lọc theo người hỏi: thí sinh chỉ nhận tài liệu tuyển sinh, còn `all` (quy chế đào tạo, cảnh báo giả mạo) luôn hiển thị cho mọi vai. |
| `department` | enum | `enrollment`, `education` | Thu hẹp không gian tìm kiếm theo đơn vị phụ trách, giảm nhiễu khi câu hỏi rõ về tuyển sinh so với đào tạo. |
| `category` | enum | `enrollment-policy`, `policy`, `warning` | Phân biệt loại nội dung: quy định bắt buộc so với thông báo cảnh giác — hai loại cần cách trả lời khác nhau. |
| `language` | ISO 639-1 | `vi` | Chọn đúng embedding model / lọc theo ngôn ngữ nếu corpus mở rộng sang tài liệu tiếng Anh. |

**Phân bố trường phân vai:** `student` = 5, `all` = 2 (đạt yêu cầu ≥ 2 giá trị để mục 7 có thể chứng minh tác dụng của filter).

---

## 2. Thiết kế chiến lược (Strategy Design) — Nhóm (15 điểm)

> Mỗi thành viên thử **một chiến lược khác nhau** trên cùng bộ tài liệu; nhóm tổng hợp và so sánh ở đây.

### Phân tích đường cơ sở (Baseline Analysis)

Chạy `ChunkingStrategyComparator().compare()` trên 3 tài liệu, `chunk_size=700`.
**Đã bỏ front matter trước khi so sánh** (`load_documents()` tách YAML sang `metadata`,
`doc.content` chỉ còn phần thân) — nếu không sẽ đo lẫn cả khối YAML vào độ dài chunk.

| Tài liệu | Chiến lược (Strategy) | Số lượng Chunk | Độ dài trung bình | Dài nhất | Giữ được ngữ cảnh không? |
|-----------|----------|-------------|------------|------|-------------------|
| `tuyen-sinh-quy-dinh-1` (4.453 ký tự) | FixedSizeChunker (`fixed_size`) | 7 | 696 | 700 | Không — cắt ngang bảng quy đổi điểm |
| `tuyen-sinh-quy-dinh-1` | SentenceChunker (`by_sentences`) | 4 | 1.112 | **2.252** | Không — bảng không có dấu chấm câu nên gộp thành khối khổng lồ |
| `tuyen-sinh-quy-dinh-1` | RecursiveChunker (`recursive`) | 11 | 403 | 694 | Có — tôn trọng ranh giới đoạn |
| `tin-tuyen-sinh-1` (8.964 ký tự) | FixedSizeChunker | 15 | 663 | 700 | Không |
| `tin-tuyen-sinh-1` | SentenceChunker | 17 | 524 | 915 | Một phần |
| `tin-tuyen-sinh-1` | RecursiveChunker | 17 | 525 | 699 | Có |
| `quy-che-dao-tao` (74.658 ký tự) | FixedSizeChunker | 119 | 697 | 700 | Không — cắt ngang giữa Điều/Khoản |
| `quy-che-dao-tao` | SentenceChunker | 133 | 554 | **2.359** | Không — chunk dài gấp 3 lần giới hạn |
| `quy-che-dao-tao` | RecursiveChunker | 122 | 604 | 698 | Có |

**Nhận xét:** `SentenceChunker` là chiến lược **kém ổn định nhất** trên corpus này: nó phụ thuộc
dấu câu, mà văn bản hành chính có nhiều bảng biểu và danh sách gạch đầu dòng **không kết thúc bằng
dấu chấm** → sinh ra chunk 2.252-2.359 ký tự, vượt xa `chunk_size=700` và làm loãng embedding.
`FixedSizeChunker` ổn định về độ dài nhưng mù ngữ nghĩa. `RecursiveChunker` là baseline tốt nhất.

### Chiến lược của từng thành viên

> Mỗi thành viên điền một khối dưới đây (copy thêm nếu nhóm có nhiều hơn 3 người).

**Thành viên 1 — Đậu Quốc Duy**
- **Loại chiến lược:** custom — `HeadingChunker(chunk_size=700, keep_heading=True)`
- **Mô tả & lý do chọn cho chủ đề này:** Corpus là văn bản quy định biên soạn **theo mục**, nên mỗi mục đã là một đơn vị ngữ nghĩa trọn vẹn — cắt theo ranh giới mục bảo toàn ngữ cảnh tốt hơn cắt theo ký tự. Điểm mấu chốt của corpus này: `quy-che-dao-tao.md` (74.658 ký tự, chiếm ~72% corpus) **chỉ có đúng 1 heading markdown**, còn 45 điều khoản được viết dưới dạng dòng thường `Điều 5. Học phần` — một chunker chỉ bắt `#` sẽ coi cả 74k ký tự là một section duy nhất. Vì vậy regex phải bắt **cả hai dạng**: heading markdown `#{1,6}` và heading pháp quy `Điều|Chương|Mục <số>.`. Section nào dài quá `chunk_size` thì hạ xuống `RecursiveChunker`, và **gắn lại tiêu đề vào từng mảnh con** — nếu không, từ mảnh thứ hai trở đi chunk mất ngữ cảnh (đã kiểm: `Điều 5` bị chia 4 mảnh, cả 4 đều giữ dòng "Điều 5. Học phần").
- **Code snippet (nếu custom):** đầy đủ trong `src/chunking.py` (lớp `HeadingChunker`)
```python
class HeadingChunker:
    # Bắt CẢ heading markdown (## 3. ...) LẪN heading pháp quy (Điều 5. ...)
    HEADING_PATTERN = re.compile(
        r"^\s*(?:#{1,6}\s+\S.*|\*{0,2}(?:Điều|Chương|Mục)\s+[0-9IVXLC]+\s*\..*)$",
        re.MULTILINE,
    )

    def chunk(self, text: str) -> list[str]:
        if not text:
            return []
        chunks = []
        for heading, body in self._split_sections(text):
            section = f"{heading}\n{body}".strip() if heading else body.strip()
            if len(section) <= self.chunk_size:
                chunks.append(section)
                continue
            # Section quá dài -> hạ xuống recursive, GẮN LẠI heading vào từng mảnh
            sub = RecursiveChunker(chunk_size=self._body_budget(heading))
            for piece in sub.chunk(body.strip()):
                chunks.append(f"{heading}\n{piece}" if heading and self.keep_heading else piece)
        return [c for c in chunks if c.strip()]
```
- **Kết quả baseline (chunk_size=700):** `tuyen-sinh-quy-dinh-1` 11 chunk / avg 427 · `tin-tuyen-sinh-1` 19 chunk / avg 564 · `quy-che-dao-tao` 145 chunk / avg 537, **max 700** (không chunk nào vượt giới hạn, khác hẳn `SentenceChunker` max 2.359).

**Thành viên 2 — Lê Chí Anh Tuấn**
- **Loại chiến lược:** `SentenceChunker(max_sentences_per_chunk=5)`
- **Mô tả & lý do chọn:** Gộp tối đa 5 câu vào một chunk, tách câu bằng regex sau dấu kết câu. Ưu điểm quan sát được: recall **top-3 tốt nhất** trong nhóm vì chunk gộp nhiều câu nên "quét" được nhiều nội dung. Nhược điểm: top-1 còn nhiễu, và với văn bản quy chế nhiều tiêu đề/bảng thì chunk dễ dài bất thường (bảng không có dấu chấm câu → gộp thành khối lớn).
- **Kết quả cá nhân:** 103 chunk · gold evidence top-1 **2/5** · top-3 **4/5** (chấm ở cấp chunk).

**Thành viên 3 — Nguyễn Đăng Nam (2A202601307)**
- **Loại chiến lược:** `RecursiveChunker` (ưu tiên ranh giới tự nhiên `\n\n` → `\n` → `. ` → ` ` → `""`)
- **Mô tả & lý do chọn:** Ưu tiên tách theo đoạn/dòng trước khi cắt thô, giữ trọn ngữ cảnh pháp lý của từng Điều/Khoản. Nhấn mạnh: với `MockEmbedder` điểm số phụ thuộc độ dài/ký tự nên phải chạy `LocalEmbedder`/OpenAI mới thấy rõ ưu thế semantic search.
- **Kết quả cá nhân:** top-3 relevant **5/5** (đánh giá ở cấp tài liệu).

**Thành viên 4 — Nguyễn Hữu Tuyền (2A202601605)**
- **Loại chiến lược:** `RecursiveChunker(chunk_size=400)` — ưu tiên ranh giới tự nhiên
- **Mô tả & lý do chọn:** Cùng họ recursive nhưng `chunk_size` nhỏ hơn (400) để chunk cô đọng hơn, mỗi Điều/Khoản gọn trong một chunk. Kết luận rút ra: mock embedder phụ thuộc độ dài nên cần local/OpenAI để đo đúng chất lượng ngữ nghĩa.
- **Kết quả cá nhân:** top-3 relevant **5/5** (đánh giá ở cấp tài liệu).

**Thành viên 5 — Tống Nguyễn Minh Khang (2A202601101)**
- **Loại chiến lược:** `FixedSizeChunker(chunk_size=500, overlap=80)`
- **Mô tả & lý do chọn:** Chiến lược đường cơ sở (baseline) — cắt cố định theo ký tự với overlap 80 để giữ liền mạch ở ranh giới. Chọn để làm **mốc đối chứng**: cho thấy một chiến lược không quan tâm ngữ nghĩa hay cấu trúc thì kém hơn thế nào so với các chiến lược theo ranh giới của cả nhóm. Overlap 80 (≈16% chunk_size) là mức thoả hiệp giữa giữ ngữ cảnh và số lượng chunk.
- **Kết quả cá nhân (LocalEmbedder):** 239 chunk · avg 493 · **max 500** (ổn định về độ dài) · top-1 **3/5** · top-3 **4/5**.
- **Điểm yếu quan sát được:** cắt theo ký tự nên thường xẻ ngang một Điều/Khoản hoặc một dòng trong bảng, làm chunk mất đầu hoặc mất đuôi ý → top-1 thấp hơn các chiến lược theo ranh giới.

### So Sánh Giữa Các Thành Viên

> Điểm /10 lấy từ phần **Tự đánh giá** trong `REPORT_CANHAN.md` của mỗi thành viên. Lưu ý: mỗi
> người chấm relevance theo tiêu chí khác nhau (cấp chunk vs cấp tài liệu) nên con số chưa hoàn toàn
> so sánh được trực tiếp — cột "Điểm mạnh/yếu" mới là phần đối chiếu công bằng.

| Thành viên | Chiến lược (Strategy) | Điểm truy xuất (/10) | Điểm mạnh | Điểm yếu |
|-----------|----------|----------------------|-----------|----------|
| Đậu Quốc Duy | `HeadingChunker(700)` | 7 (chấm cấp chunk theo barem) | top-1 4/5 — cao nhất; chunk luôn ≤ 700 và giữ tiêu đề Điều/Mục | Q5 (câu phủ định) miss; nhiều chunk hơn (200) → tốn embedding hơn |
| Lê Chí Anh Tuấn | `SentenceChunker(5)` | 8 | **recall top-3 tốt nhất** (4/5 cấp chunk) | top-1 nhiễu (2/5); chunk dễ dài bất thường trên bảng/điều |
| Nguyễn Đăng Nam | `RecursiveChunker` (mặc định) | 10 | giữ trọn ngữ cảnh Điều/Khoản; top-3 5/5 (cấp tài liệu) | chấm ở cấp tài liệu nên dễ HIT hơn cấp chunk |
| Nguyễn Hữu Tuyền | `RecursiveChunker(400)` | 10 | chunk cô đọng nhờ `chunk_size` nhỏ; top-3 5/5 (cấp tài liệu) | chấm ở cấp tài liệu nên dễ HIT hơn cấp chunk |
| Tống Nguyễn Minh Khang | `FixedSizeChunker(500, 80)` | — | baseline ổn định độ dài (max 500); top-3 4/5 | top-1 chỉ 3/5 — cắt ngang Điều/Khoản, mù ngữ nghĩa |

#### Đối chứng 4 chiến lược trên CÙNG điều kiện

> Cùng corpus, cùng 5 query, cùng `LocalEmbedder` — **chỉ đổi chunker**. Đây là đối chứng nội bộ
> để tham khảo khi các thành viên điền bảng trên; con số của mỗi người vẫn lấy từ `bench.py` của họ.

| Chiến lược | Số chunk | Top-1 đúng | Top-3 đúng |
|---|---|---|---|
| **`HeadingChunker(700)`** *(của tôi)* | 200 | **4/5** | 4/5 |
| `RecursiveChunker(700)` | 171 | **4/5** | 4/5 |
| `SentenceChunker(3)` | 172 | 3/5 | **5/5** |
| `FixedSizeChunker(700, 70)` | 161 | 2/5 | 4/5 |

**Chiến lược nào tốt nhất cho chủ đề này? Tại sao?**
> **Không có chiến lược thắng tuyệt đối — phải hỏi "tốt nhất cho việc gì".** Số liệu cho thấy hai
> nhóm rõ rệt: `HeadingChunker` và `RecursiveChunker` mạnh ở **top-1** (4/5), còn `SentenceChunker`
> lại mạnh ở **top-3** (5/5) nhưng chỉ 3/5 ở top-1.
>
> Giải thích: `SentenceChunker` tạo chunk **to và không đều** (có chunk 2.359 ký tự, xem bảng
> baseline) — chunk to thì "quét" được nhiều nội dung nên dễ lọt vào top-3, nhưng chính vì trộn
> nhiều ý nên embedding bị loãng, khó leo lên top-1. Ngược lại, chunker theo ranh giới ngữ nghĩa
> tạo chunk **cô đọng đúng một ý**, nên khi trúng thì trúng ở hạng 1.
>
> **Kết luận thực dụng:** nếu hệ thống đưa top-3 vào prompt cho LLM (như `KnowledgeBaseAgent` của
> lab này), top-3 mới là chỉ số quan trọng; nếu hiển thị một câu trả lời duy nhất cho người dùng thì
> top-1 quyết định. Với corpus văn bản quy định, nhóm chọn **`HeadingChunker`/`RecursiveChunker`** vì
> đạt top-1 cao nhất **và** không bao giờ vượt `chunk_size` — `SentenceChunker` đạt 5/5 top-3 nhưng
> rủi ro chunk 2.359 ký tự là không chấp nhận được khi đưa vào context window có giới hạn.
>
> `FixedSizeChunker` yếu nhất ở top-1 (2/5) đúng như dự đoán: nó cắt theo ký tự nên thường xẻ đôi
> một điều khoản, làm chunk mất đầu hoặc mất đuôi ý.

---

## 3. Câu hỏi đánh giá & Chất lượng truy xuất (Retrieval Quality) — Nhóm (10 điểm)

### Câu hỏi đánh giá & Câu trả lời chuẩn (nhóm thống nhất)

> **Đúng 5 câu hỏi**, đa dạng, có thể kiểm chứng; **ít nhất 1 câu** cần lọc metadata mới trả lời tốt. Đây là bộ câu hỏi chung cho mọi thành viên chạy.

> Bộ query đầy đủ kèm trích dẫn gốc: **`data/benchmark_queries.md`** (chốt 2026-08-03,
> trước khi chạy bất kỳ strategy nào). File này để **ngoài** `data/k3_university/` có chủ đích —
> xem ghi chú ở mục 4.

| # | Câu hỏi (Query) | Câu trả lời chuẩn (Gold Answer) | Chunk nào chứa thông tin? |
|---|-------|-------------------------------|--------------------------|
| 1 | Ngưỡng đầu vào ĐHCQ 2025 ngành Trí tuệ nhân tạo là bao nhiêu điểm? | 24 điểm (nhóm ngành Máy tính & CNTT, mã CN12); các ngành còn lại 22 điểm. Thang 30, không nhân hệ số. | `tuyen-sinh-quy-dinh-1`, mục 3 + bảng mã ngành |
| 2 | Hạn cuối nộp hồ sơ xét tuyển trực tuyến HSA/SAT 2025 sau gia hạn? | 17h00 ngày **28/7/2025** (hạn cũ 30/6/2025 đã bị thay thế) | `tuyen-sinh-quy-dinh-3`, đoạn "gia hạn thời gian đăng ký" |
| 3 | Năm 2026 SV năm nhất học ở cơ sở nào, tối đa bao nhiêu nguyện vọng? | Cơ sở **Hòa Lạc**; tối đa **15 nguyện vọng** | `tin-tuyen-sinh-1` — 2 dữ kiện nằm cách xa nhau (multi-hop) |
| 4 | Một học phần bao nhiêu tín chỉ, một tín chỉ bao nhiêu giờ tín chỉ? | Học phần **2-5 tín chỉ**; 1 tín chỉ = **15 giờ tín chỉ** | `quy-che-dao-tao`, Điều 5 + Điều 4 khoản 2 |
| 5 | Trường có tổ chức du học ngắn hạn thu phí / cử người thu tiền không? | **Không** tổ chức, **không** cử trung gian liên hệ thu tiền | `tuyen-sinh-thong-bao-1` (`audience: all`, `category: warning`) |

### Tổng hợp chất lượng truy xuất của nhóm

> Cách chấm (theo `docs/SCORING.md`): **2 điểm/câu** — top-3 chứa chunk liên quan + agent trả lời đúng (2), có liên quan nhưng thiếu/không ở top-1 (1), không có trong top-3 (0).

> Cột dưới đây điền theo kết quả `HeadingChunker` + `LocalEmbedder`; các thành viên khác bổ sung
> cột của mình khi có số liệu.

| # | Câu hỏi | Chiến lược tốt nhất cho câu này | Có chunk liên quan trong top-3? | Ghi chú |
|---|---------|-------------------------------|-------------------------------|---------|
| 1 | Ngưỡng đầu vào TTNT | `HeadingChunker` | ✅ top-1 (0.7293) | Trúng đúng mục "3. Ngưỡng đầu vào"; `MockEmbedder` trả nhầm bảng HSA |
| 2 | Hạn nộp sau gia hạn | Mọi chiến lược | ✅ top-1 (0.8102) | **Cả top-3 đều đúng tài liệu** — điểm cao nhất trong 5 câu |
| 3 | Cơ sở + nguyện vọng 2026 | `HeadingChunker` | ✅ top-1 (0.7823) | Query multi-hop, cả top-3 đều `tin-tuyen-sinh-1` |
| 4 | Tín chỉ / giờ tín chỉ | `HeadingChunker` | ⚠️ top-3 (0.6786) | Đúng tài liệu nhưng **sai điều khoản** ở top-1 (Điều 41 thay vì Điều 4) |
| 5 | Du học giả mạo | Chỉ đúng khi **có filter** | ❌ MISS (đúng ở hạng 8) | Câu phủ định — xem failure case bên dưới |

**Lọc bằng metadata có giúp ích không? Ở câu hỏi nào?**
> Có — và thí nghiệm A/B trên **Q5** cho thấy **cả hai mặt**: filter đúng trường thì cứu được câu
> trả lời, filter sai trường thì phản tác dụng. Số liệu chạy thật với `LocalEmbedder` +
> `HeadingChunker(700)`:
>
> | Cấu hình | Top-3 trả về (score) | Tài liệu đúng `tuyen-sinh-thong-bao-1`? |
> |---|---|---|
> | **A — không filter** | `tin-tuyen-sinh-1` (0.7217), `tin-tuyen-sinh-1` (0.7169), `tin-tuyen-sinh-1` (0.7088) | ❌ Nằm ở **hạng 8** (0.6642) |
> | **B — filter `audience = student`** | `tin-tuyen-sinh-1` (0.7217 / 0.7169 / 0.7088) | ❌ **Bị loại khỏi không gian tìm kiếm** |
> | **C — filter `category = warning`** | **`tuyen-sinh-thong-bao-1` chunk 2 (0.6642)**, chunk 0 (0.5325), chunk 1 (0.5037) | ✅ **Lên top-1** |
>
> **Cấu hình C — filter cứu được câu trả lời:** chunk chứa gold answer nhảy từ **hạng 8 lên hạng 1**,
> biến kết quả của thành viên chạy `HeadingChunker` từ 4/5 thành **5/5**. Đáng chú ý: score của nó
> (0.6642) **thấp hơn** cả 3 kết quả sai ở cấu hình A — nghĩa là filter sửa được *thứ hạng* chứ
> không sửa được *điểm số*, đúng với nguyên tắc "metadata không thay thế embedding, nhưng giúp thu
> hẹp đúng phạm vi".
>
> **Cấu hình B — đánh đổi recall:** `tuyen-sinh-thong-bao-1` mang `audience: all`, nên filter
> `audience = student` loại **đúng tài liệu duy nhất** trả lời được Q5 → hệ thống chắc chắn sai, dù
> store vẫn còn tài liệu hợp lệ. Kết luận thiết kế rút ra từ số liệu: truy vấn của vai `student`
> phải khớp **`audience IN (student, all)`**, không phải `audience = student`.
>
> **Giới hạn cần nói rõ khi demo:** cấu hình C chỉ dùng được khi **biết trước** câu hỏi thuộc loại
> cảnh báo. Trong hệ thống thật phải phân loại ý định câu hỏi trước khi chọn filter — không thể
> hard-code `category = warning` cho mọi truy vấn.

---

## 4. Thuyết trình (Demo) & Bài học nhóm — Nhóm (5 điểm)

**Những phân tích (insights) hay nhất nhóm sẽ trình bày:**
>
> **1. Failure case có bằng chứng: file gold answer bị nạp vào chính corpus.**
> `benchmark_queries.md` ban đầu nằm trong `data/k3_university/`, mà `load_documents()` đọc **mọi**
> file `.md` trong thư mục → file chứa nguyên văn cả 5 đáp án được nạp vào store thành tài liệu
> thứ 8. Retrieval khi đó sẽ trúng chính đáp án thay vì tài liệu nguồn, làm **mọi** strategy đều
> có điểm ảo và bảng so sánh giữa các thành viên mất ý nghĩa. Bằng chứng độc lập: `scripts/check_metadata.py`
> báo `so file: 8 (can 5-10)` và `THIEU METADATA: doc_id,title,source_url,...` cho đúng file này.
> **Khắc phục:** chuyển ra `data/benchmark_queries.md` (ngoài đường ingest); sau đó checker báo
> `so file: 7`, `csv: khop`. Bài học: ranh giới giữa *dữ liệu* và *đáp án* phải là ranh giới thư mục,
> không thể dựa vào việc nhớ loại trừ bằng tay.
>
> **2. Câu hỏi phủ định là điểm mù của embedding — và filter cứu được (A/B ở mục 3).**
> Q5 hỏi "Trường có tổ chức… không?", đáp án đúng là một câu **phủ định**. Embedding đo *chủ đề*
> chứ không đo *cực (polarity)*, nên tài liệu đúng chỉ xếp **hạng 8 (0.6642)**, thua 3 chunk của
> `tin-tuyen-sinh-1` (0.7217-0.7088) vốn chỉ "gần chủ đề". Lọc `category = warning` kéo nó lên
> **top-1 ngay lập tức** → 4/5 thành 5/5. Nhưng lọc `audience = student` lại **loại mất** chính tài
> liệu đó (vì nó mang `audience: all`) → minh hoạ cả hai chiều của đánh đổi precision/recall.
>
> **2b. Đổi embedder quan trọng hơn đổi chunker.**
> Cùng `HeadingChunker`, chỉ đổi backend: `MockEmbedder` 2/5 → `LocalEmbedder` 4/5. Trong khi đó
> đổi qua lại 4 chiến lược chunking (cùng `LocalEmbedder`) chỉ dao động 2/5-4/5 ở top-1. Kết luận:
> chất lượng mô hình embedding **chặn trên** toàn hệ thống; tối ưu chunking chỉ có ý nghĩa sau khi
> đã có embedder đủ tốt.
>
> **3. `SentenceChunker` sụp đổ trên văn bản hành chính.**
> Bảng biểu và danh sách gạch đầu dòng không kết thúc bằng dấu chấm → chunk dài **2.359 ký tự** dù
> `chunk_size=700` (gấp 3,4 lần giới hạn). Chiến lược phụ thuộc dấu câu không an toàn cho domain này.

**Bài học rút ra khi so sánh trong nhóm:**
> Cùng một corpus và cùng 5 query, 4 chiến lược cho kết quả khác nhau rõ theo **tiêu chí đánh giá**,
> không phải theo "chiến lược nào giỏi hơn". `SentenceChunker` của Anh Tuấn thắng **top-3** (recall
> cao) nhưng thua **top-1**; `HeadingChunker`/`RecursiveChunker` mạnh top-1 nhờ chunk cô đọng đúng
> một ý. Bài học lớn nhất: nhóm phát hiện các thành viên **chấm relevance theo hai chuẩn khác nhau**
> — cấp chunk (chunk phải chứa bằng chứng gold) chặt hơn cấp tài liệu (chỉ cần đúng `doc_id`) — nên
> con số 5/5 và 4/5 không so trực tiếp được; đây chính là lý do một benchmark chung với tiêu chí
> chấm thống nhất lại quan trọng ngang với việc chọn chiến lược.

**Nếu làm lại, nhóm sẽ thay đổi gì trong chiến lược dữ liệu (data strategy)?**
> Hai điều: (1) **Thống nhất tiêu chí chấm ngay từ đầu** (cấp chunk, không phải cấp tài liệu) để số
> liệu giữa các thành viên so được với nhau. (2) **Thêm trường metadata cho câu hỏi phủ định**: Q5
> cho thấy embedding không phân biệt được cực (polarity), nên nếu làm lại sẽ gắn thêm nhãn kiểu
> `stance: denial` cho các tài liệu cảnh báo, hoặc mở rộng corpus để mỗi chủ đề có nhiều tài liệu
> hơn, giảm phụ thuộc vào một filter cứng.

---

## Tự Đánh Giá (Phần Nhóm)

| Tiêu chí | Điểm tự đánh giá |
|----------|-------------------|
| Lựa chọn tài liệu (Document Set Quality) | 10 / 10 |
| Thiết kế chiến lược (Strategy Design) | 13 / 15 |
| Chất lượng truy xuất (Retrieval Quality) | 9 / 10 |
| Thuyết trình (Demo) | 5 / 5 |
| **Tổng phần nhóm** | **37 / 40** |
