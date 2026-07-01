# BAI 13: CHUNG MINH AMORTIZED O(1) CỦA HÀNG ĐỢI 2 STACK
"""
- Phương pháp kế toán (Accounting Method): Mỗi phần tử khi Enqueue được nạp sẵn 2 đồng tín dụng. 
  1 đồng chi trả cho thao tác push vào in_stack, 1 đồng dự phòng cho chu kỳ chuyển tiếp sang out_stack. 
  Vì từng phần tử chỉ dịch chuyển qua mỗi stack tối đa một lần duy nhất, chi phi amortized ổn định O(1).
"""
