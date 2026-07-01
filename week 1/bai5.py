"""
Bài 5. Điều kiện áp dụng

Thuật toán tìm kiếm tuyến tính hoàn toàn không đòi hỏi hay bắt buộc mảng dữ liệu 
phải được sắp xếp theo một trật tự nào từ trước. Lý do là vì giải 
thuật này hoạt động theo nguyên lý kiểm tra độc lập từng phần tử một cách lần lượt, 
nên dù mảng có lộn xộn thì kết quả tìm kiếm vẫn chính xác.

Khi so sánh ngắn gọn với tìm kiếm nhị phân, chúng ta thấy rõ sự khác biệt
- Về điều kiện áp dụng, tìm kiếm tuyến tính có thể chạy trên mọi loại mảng bất kỳ, 
  trong khi tìm kiếm nhị phân bắt buộc mảng đầu vào phải được sắp xếp tăng dần 
  hoặc giảm dần thì mới hoạt động được.
- Về độ phức tạp, tìm kiếm tuyến tính có độ phức tạp thời gian là O của n, chạy 
  chậm hơn so với tìm kiếm nhị phân có độ phức tạp là O của log cơ số 2 của n. 
  Tuy nhiên, nếu dùng nhị phân thì chúng ta lại phải tốn thêm một khoảng thời 
  gian và chi phí ban đầu để sắp xếp lại mảng dữ liệu.
"""