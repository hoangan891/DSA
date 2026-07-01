"""
- Bất biến: Trước khi bước vào vòng lặp i (vòng ngoài), đoạn mảng từ arr[0] 
  đến arr[i-1] luôn chứa chính xác các phần tử ban đầu nhưng đã được sắp xếp tăng dần.

- Khởi tạo: Với i = 1, mảng con chỉ có duy nhất phần tử arr[0], nên thuộc tính 
  đã sắp xếp hiển nhiên đúng (mảng 1 phần tử luôn coi như đã sắp xếp).

- Duy trì: Khi xét đến phần tử kế tiếp arr[i], thuật toán tìm vị trí thích hợp 
  để chèn nó vào trong dãy arr[0..i-1] bằng cách dịch chuyển các phần tử lớn hơn 
  ra phía sau. Kết quả thu được là dãy arr[0..i] gồm i+1 phần tử được mo rộng và 
  sắp xếp hợp lệ. Bất biến tiếp tục được giữ vững.

- Kết thúc: Vòng lặp dừng lại khi biến i chạy đến n. Lúc này mảng con arr[0..n-1] 
  chứa đầy đủ tất cả các phần tử ban đầu và đã được sắp xếp hoàn toàn đúng vị trí.
"""

