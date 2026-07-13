"""
- Bất biến: Tại thời điểm bắt đầu mỗi bước của vòng lặp ngoài, với mọi đỉnh u 
  đã nằm trong tập chốt P (tức là P[u] == True), khoảng cách L[u] đã đạt giá trị 
  ngắn nhất tối ưu tuyệt đối xuất phát từ nguồn. Đồng thời, với mọi đỉnh v thuộc 
  vùng chưa chốt, L[v] lưu độ dài ngắn nhất của đường đi chỉ đi qua các đỉnh trung 
  chuyển đã chốt trong tập P.

- Khởi tạo: Ban đầu tập chốt P trống rỗng, chỉ có nguồn xuất phát L[s] = 0, 
  các đỉnh khác bằng vô cực (INF). Bất biến hiển nhiên đúng.

- Duy trì: Tại mỗi bước, thuật toán chọn ra đỉnh u chưa chốt có L[u] nhỏ nhất 
  để đưa vào tập P. Vì trọng số đồ thị không âm, đường đi vòng qua bất kỳ đỉnh 
  chưa chốt nào khác chắc chắn sẽ có tổng độ dài lớn hơn hoặc bằng L[u], đảm bảo 
  L[u] đã tối ưu tuyệt đối. Sau đó, thuật toán tiến hành nới lỏng (relax) cập nhật 
  cho các láng giềng của u, giúp duy trì chính xác tính chất cho các vòng lặp tiếp theo.

- Kết thúc: Vòng lặp ngoài dừng lại sau khi toàn bộ tất cả các đỉnh kết nối liên thông 
  đều đã được duyệt và đưa vào tập chốt P. Khi đó khoảng cách L thu được chính là 
  kết quả ngắn nhất tối ưu cần tìm. Thuật toán chứng minh đúng đắn hoàn toàn.
"""
