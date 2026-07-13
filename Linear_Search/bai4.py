"""
Bài 4. Phân tích độ phức tạp

Xét một mảng tổng quát có n phần tử, số lần thực hiện phép so sánh sẽ thay đổi 
theo các kịch bản sau:

- Trường hợp tốt nhất xảy ra khi phần tử cần tìm nằm ngay đầu mảng, lúc này chúng 
  ta chỉ tốn đúng 1 phép so sánh duy nhất.
- Trường hợp xấu nhất diễn ra khi phần tử đó nằm ở cuối mảng hoặc không nằm trong 
  danh sách dữ liệu, buộc thuật toán phải thực hiện tối đa n phép so sánh.
- Trường hợp trung bình khi biết chắc chắn phần tử có trong mảng và phân bố đều 
  ở các vị trí, số phép so sánh trung bình tính được bằng công thức lấy tổng của 
  n chia cho 2, tương đương với n cộng 1 rồi chia cho 2.

Từ kịch bản xấu nhất, khi lượng dữ liệu n ngày càng lớn thì số phép tính cũng tăng 
lên theo tỷ lệ thuận tuyến tính. Do đó, độ phức tạp thời gian của thuật toán tìm 
kiếm tuyến tính theo ký hiệu O lớn được xác định là O của n.
"""