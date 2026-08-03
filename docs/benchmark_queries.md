# Benchmark Queries — K3 University (UET/ĐHQGHN)

**Vai trò:** Benchmark owner
**Corpus:** `data/k3_university/` (7 tài liệu, xem `sources.csv`)
**Chốt ngày:** 2026-08-03

> **Quy tắc:** Bộ query này được chốt **trước** khi chạy bất kỳ chiến lược chunking nào.
> Không sửa query, gold answer hay `expected_doc_id` sau khi đã xem kết quả retrieval.
> Nếu phát hiện query sai/mơ hồ, ghi chú ở mục "Nhật ký thay đổi" kèm lý do, không sửa lặng lẽ.

Mỗi gold answer dưới đây đều trích dẫn được từ tài liệu trong corpus — cột "Trích dẫn gốc" là căn cứ đối chiếu.

---

## Q1 — Ngưỡng đầu vào theo nhóm ngành

**Query:** `Ngưỡng đầu vào đại học chính quy năm 2025 của ngành Trí tuệ nhân tạo là bao nhiêu điểm?`

| Mục | Nội dung |
|---|---|
| **Gold answer** | 24 điểm. Các ngành thuộc nhóm ngành Máy tính và Công nghệ thông tin (gồm Trí tuệ nhân tạo, mã CN12) có ngưỡng đầu vào 24 điểm; các ngành còn lại 22 điểm. Tính theo thang 30, không nhân hệ số, không tính điểm cộng, đã bao gồm điểm ưu tiên khu vực/đối tượng. |
| **`expected_doc_id`** | `tuyen-sinh-quy-dinh-1` |
| **Trích dẫn gốc** | Mục 3: *"Đối với các ngành thuộc nhóm ngành Máy tính và Công nghệ thông tin: 24 điểm; Đối với các ngành còn lại: 22 điểm."* + bảng chi tiết dòng `CN12 \| Trí tuệ nhân tạo \| 24`. |
| **Kiểm tra retrieval** | Chunk trúng phải chứa **cả** ngưỡng 24 **và** ràng buộc "thang điểm 30, không nhân hệ số". Nếu chỉ trả về con số 24 rời khỏi điều kiện áp dụng → chunk quá nhỏ, mất ngữ cảnh. |
| **Vì sao chọn** | Có bảng dài 20 dòng — phân biệt rõ chiến lược giữ được bảng và chiến lược cắt vụn giữa bảng. |

---

## Q2 — Hạn nộp hồ sơ sau gia hạn

**Query:** `Hạn cuối nộp hồ sơ xét tuyển trực tuyến theo HSA và SAT năm 2025 sau khi gia hạn là khi nào?`

| Mục | Nội dung |
|---|---|
| **Gold answer** | 17h00 ngày 28/7/2025, nộp trên hệ thống trực tuyến của Trường tại https://tuyensinh.uet.vnu.edu.vn (mục "Đăng ký xét tuyển"). Hạn cũ trước khi gia hạn là 17h00 ngày 30/6/2025. |
| **`expected_doc_id`** | `tuyen-sinh-quy-dinh-3` |
| **Trích dẫn gốc** | *"gia hạn thời gian đăng ký, chỉnh sửa và nộp hồ sơ trực tuyến ... đến 17h00 ngày 28/7/2025"*; hạn cũ: *"trước thời hạn quy định (17h00 ngày 30/6/2025)"*. |
| **Kiểm tra retrieval** | **Bẫy có chủ đích:** tài liệu chứa hai mốc thời gian. Trả lời đúng phải là 28/7/2025 (hạn mới), không phải 30/6/2025 (hạn cũ đã bị thay thế). Nếu hệ thống trả 30/6 → chunk bị tách khỏi ngữ cảnh "gia hạn". |
| **Vì sao chọn** | Đo khả năng phân biệt thông tin bị thay thế (superseded) — lỗi thường gặp và nguy hiểm nhất trong RAG văn bản hành chính. |

---

## Q3 — Điểm mới tuyển sinh 2026

**Query:** `Năm 2026 sinh viên năm thứ nhất Trường ĐH Công nghệ học ở cơ sở nào và được đăng ký tối đa bao nhiêu nguyện vọng?`

| Mục | Nội dung |
|---|---|
| **Gold answer** | Toàn bộ sinh viên năm thứ nhất từ khóa tuyển sinh 2026 học tập tại **cơ sở Hòa Lạc**. Quy chế năm 2026 giới hạn tối đa **15 nguyện vọng**. |
| **`expected_doc_id`** | `tin-tuyen-sinh-1` |
| **Trích dẫn gốc** | *"từ khóa tuyển sinh năm 2026, toàn bộ sinh viên năm thứ nhất sẽ được học tập tại cơ sở Hòa Lạc"*; *"điểm mới của quy chế năm 2026 là giới hạn tối đa 15 nguyện vọng"*. |
| **Kiểm tra retrieval** | Query **đa phần (multi-hop)**: hai dữ kiện nằm cách xa nhau trong cùng tài liệu. Chiến lược chunk tốt phải trả về đủ cả hai; chunk quá nhỏ thường chỉ trúng một. |
| **Vì sao chọn** | Đây là tài liệu duy nhất có `document_version: not-stated` — kiểm tra hệ thống vẫn trích dẫn được nguồn dù thiếu ngày ban hành. |

---

## Q4 — Quy định tín chỉ (audience: all)

**Query:** `Một học phần có khối lượng bao nhiêu tín chỉ và một tín chỉ tương ứng bao nhiêu giờ tín chỉ?`

| Mục | Nội dung |
|---|---|
| **Gold answer** | Mỗi học phần có khối lượng từ **2 đến 5 tín chỉ**, tổ chức giảng dạy trọn vẹn trong một học kỳ. Một tín chỉ là khối lượng kiến thức, kỹ năng sinh viên tích lũy được từ học phần trong **15 giờ tín chỉ**. |
| **`expected_doc_id`** | `quy-che-dao-tao` |
| **Trích dẫn gốc** | Điều 5: *"mỗi học phần có khối lượng kiến thức từ 2 đến 5 tín chỉ"*; Điều 4 khoản 2: *"Tín chỉ là đại lượng ... tích lũy được từ học phần trong 15 giờ tín chỉ."* |
| **Kiểm tra retrieval** | Tài liệu này dài ~74.661 ký tự (gấp ~8 lần các file còn lại) và có cấu trúc Điều/Khoản. Đo trực tiếp khả năng định vị trong văn bản dài — nơi `FixedSizeChunker` dễ cắt ngang giữa điều khoản. |
| **Vì sao chọn** | Phủ `audience: all`, và là tài liệu duy nhất có cấu trúc pháp quy phân cấp → lợi thế rõ cho `RecursiveChunker`. |

---

## Q5 — Cảnh báo giả mạo (kiểm tra metadata filter)

**Query:** `Trường ĐH Công nghệ có tổ chức chương trình du học ngắn hạn thu phí và cử người liên hệ thí sinh thu tiền không?`

| Mục | Nội dung |
|---|---|
| **Gold answer** | Không. Trường khẳng định **không** tổ chức các chương trình du học ngắn hạn thu phí như trong các thông báo giả mạo, và **không** cử bất kỳ cá nhân/đơn vị trung gian nào liên hệ trực tiếp với thí sinh để thu hồ sơ hay yêu cầu chuyển tiền. Thông tin chính thức chỉ công bố tại https://tuyensinh.uet.vnu.edu.vn và https://uet.vnu.edu.vn. |
| **`expected_doc_id`** | `tuyen-sinh-thong-bao-1` |
| **Trích dẫn gốc** | *"Trường không tổ chức các chương trình du học ngắn hạn thu phí như các thông báo nêu trên."*; *"Nhà trường không cử bất kỳ cá nhân, đơn vị trung gian nào liên hệ trực tiếp với thí sinh để thu hồ sơ hay yêu cầu chuyển tiền."* |
| **Kiểm tra retrieval** | Câu hỏi phủ định — hệ thống phải trả về khẳng định **phủ nhận**, không được trả về chunk mô tả nội dung giả mạo rồi hiểu ngược thành trường có tổ chức. |
| **Vì sao chọn** | Là tài liệu `category: warning` duy nhất và `audience: all` — dùng cho thí nghiệm filter ở mục 7. |

---

## Phủ sóng corpus

| `doc_id` | `audience` | Query phủ |
|---|---|---|
| `tuyen-sinh-quy-dinh-1` | student | Q1 |
| `tuyen-sinh-quy-dinh-3` | student | Q2 |
| `tin-tuyen-sinh-1` | student | Q3 |
| `quy-che-dao-tao` | all | Q4 |
| `tuyen-sinh-thong-bao-1` | all | Q5 |
| `tin-tuyen-sinh-2` | student | — (nhiễu) |
| `tuyen-sinh-quy-dinh-2` | student | — (nhiễu) |

5 query trải trên 5 tài liệu khác nhau, phủ **cả hai** giá trị `audience` (3× `student`, 2× `all`).
Hai tài liệu không có query đóng vai trò **nhiễu (distractor)** — cùng chủ đề tuyển sinh nên
dễ bị retrieve nhầm, giúp bài đo phân biệt được chiến lược tốt và chiến lược may mắn.

## Gợi ý thí nghiệm metadata filter (mục 7)

Q5 dùng để chứng minh giá trị của trường phân vai:

- **Không filter:** truy vấn Q5 trên toàn bộ 7 tài liệu.
- **Có filter `audience = student`:** `tuyen-sinh-thong-bao-1` (`audience: all`) bị loại khỏi
  không gian tìm kiếm → hệ thống **không** trả lời được Q5.

Kết quả kỳ vọng: filter quá hẹp làm mất tài liệu đúng. Đây là bằng chứng cho thấy truy vấn của
vai `student` cần khớp `audience IN (student, all)` chứ không phải `audience = student` —
một kết luận thiết kế rút ra từ số liệu, không phải suy đoán.

## Nhật ký thay đổi

| Ngày | Thay đổi | Lý do |
|---|---|---|
| 2026-08-03 | Chốt bộ 5 query đầu tiên | Trước khi chạy benchmark |
