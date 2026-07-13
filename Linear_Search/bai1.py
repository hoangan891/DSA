"""

Bài 1. Trình bày ý tưởng


Ý tưởng cốt lõi của thuật toán tìm kiếm tuyến tính là chúng ta sẽ đi duyệt qua 
từng phần tử của dãy số một cách tuần tự, bắt đầu từ vị trí đầu tiên có chỉ số 
bằng 0. Tại mỗi bước, thuật toán lấy giá trị của phần tử hiện tại đem so 
sánh với số x cần tìm. Quá trình này cứ lặp đi lặp lại liên tục cho đến khi 
tìm thấy giá trị mong muốn hoặc đã kiểm tra hết toàn bộ danh sách mà không có 
kết quả.

Dữ liệu đầu vào của thuật toán bao gồm một mảng A chứa n phần tử và một giá trị 
x cần tìm kiếm. Dữ liệu đầu ra trả về sẽ là vị trí đầu tiên mà x xuất hiện 
trong mảng, trường hợp kiểm tra hết mảng mà không thấy x thì hệ thống trả về 
giá trị bằng -1.

Thuật toán này sẽ dừng lại trong hai trường hợp cụ thể:
- Trường hợp thứ nhất là tìm thấy phần tử thỏa mãn điều kiện bằng x, lúc này máy 
  sẽ dừng ngay lập tức và trả về chỉ số của vị trí đó.
- Trường hợp thứ hai là khi chỉ số duyệt vượt quá số lượng phần tử của mảng, nghĩa 
  là chúng ta đã tìm kiếm khắp nơi nhưng không thấy, thuật toán sẽ dừng và báo 
  về -1.
"""

