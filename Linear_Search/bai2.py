"""

Bài 2. Mô phỏng từng bước


Giả sử chúng ta có mảng A gồm các số 7, 3, 9, 12, 5, 8, 1 và cần tìm số x bằng 5. 
Quá trình chạy của thuật toán được mô phỏng chi tiết qua từng bước như sau:

- Bước 0: Xét vị trí đầu tiên có chỉ số i bằng 0, giá trị tương ứng là 7. So 
  sánh 7 với 5 thấy không trùng khớp, thuật toán tiếp tục tăng i lên 1.
- Bước 1: Xét vị trí có chỉ số i bằng 1, giá trị lúc này là 3. So sánh 3 với 
  5 thấy không bằng nhau, thuật toán tiếp tục tăng i lên 1.
- Bước 2: Xét vị trí có chỉ số i bằng 2, giá trị nhận được là 9. So sánh 9 
  với 5 thấy không thỏa mãn, thuật toán tiếp tục tăng i lên 1.
- Bước 3: Xét vị trí có chỉ số i bằng 3, giá trị tại đây là 12. So sánh 12 
  với 5 vẫn không khớp, thuật toán tiếp tục tăng i lên 1.
- Bước 4: Xét vị trí có chỉ số i bằng 4, giá trị tìm được là 5. Thực hiện so 
  sánh 5 với 5 thấy hoàn toàn trùng khớp. Thuật toán tìm thấy kết quả, dừng 
  quá trình tìm kiếm tại đây và trả về giá trị bằng 4.
"""

