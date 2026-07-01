"""
- Bất biến: Sau khi kết thúc lượt quét thứ i (vòng lặp ngoài), đoạn mảng con 
  arr[0..i] luôn chứa đúng i+1 phần tử nhỏ nhất của toàn bộ mảng và chúng đã 
  được sắp xếp hoàn toàn theo thứ tự tăng dần.

- Khởi tạo: Với i = 0, thuật toán duyệt qua toàn bộ mảng để tìm ra phần tử 
  nhỏ nhất tuyệt đối, sau đó hoán đổi về vị trí đầu tiên arr[0]. Mảng con 
  arr[0] lúc này hiển nhiên đúng thuộc tính.

- Duy trì: Giả sử bất biến đúng đến lượt thứ i-1. Tại lượt lặp thứ i, thuật toán 
  tiếp tục tìm kiếm giá trị nhỏ nhất trong vùng chưa sắp xếp còn lại arr[i..n-1] 
  và hoán đổi nó lên đầu vùng đó (chính là vị trí arr[i]). Do giá trị mới chèn này 
  luôn lớn hơn hoặc bằng arr[i-1] và nhỏ hơn toàn bộ phần còn lại, đoạn arr[0..i] 
  được mở rộng một cách hợp lệ.

- Kết thúc: Vòng lặp ngoài chạy hết n-1 lượt. Lúc này mảng con arr[0..n-2] đã 
  được sắp xếp đúng chỗ. Phần tử duy nhất còn sót lại ở cuối mảng arr[n-1] 
  bắt buộc phải là giá trị lớn nhất tuyệt đối. Toàn bộ mảng được sắp xếp thành công.
"""

