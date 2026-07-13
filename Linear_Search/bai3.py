"""
Bài 3. Đếm số phép so sánh
Dựa vào mảng số đã cho ở bài trước, chúng ta tiến hành đếm số lần phải thực hiện 
phép so sánh bằng giữa phần tử trong mảng với số cần tìm cho từng trường hợp[cite: 17, 18]:

- Câu a: Khi tìm x bằng 7, do số 7 nằm ngay vị trí đầu tiên của mảng nên thuật toán 
  chỉ cần thực hiện đúng 1 phép so sánh là tìm thấy ngay.
- Câu b: Khi tìm x bằng 1, vì số 1 nằm ở tận cùng của mảng nên thuật toán phải 
  kiểm tra qua tất cả các số và tốn tổng cộng 7 phép so sánh.
- Câu c: Khi tìm x bằng 100, do số này không hề có mặt trong mảng nên thuật toán 
  buộc phải quét từ đầu đến cuối dãy số rồi mới kết luận, số phép so sánh phải 
  chạy là 7 lần.

Nhận xét rút ra là số lần phải so sánh phụ thuộc hoàn toàn vào vị trí của phần tử 
đang nằm trong mảng. Nếu số cần tìm nằm ở những vị trí đầu tiên, thời 
gian xử lý sẽ cực kỳ nhanh vì tốn ít phép so sánh. Ngược lại, nếu số đó nằm ở cuối 
dãy hoặc không tồn tại thì thuật toán phải chạy hết công suất và tốn nhiều phép 
toán nhất.
"""