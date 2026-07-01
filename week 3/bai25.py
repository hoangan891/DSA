"""
Chung minh bang Bat bien vong lap (Loop Invariant):

- Bat bien: Truoc moi luot lap i, day con tu vi tri n-i den n-1 da duoc 
  sap xep dung cho va chua cac phan tu lon nhat cua mang.

- Khoi tao: Khi i = 0, day con o cuoi mang dang rong nen bat bien hien nhien dung.

- Duy tri: Qua moi luot quet cac cap ke nhau, phan tu lon nhat trong phan 
  chua sap xep se bi day ve cuoi dãy. Khi i tang len, day con da sap xep 
  duoc noi dai them 1 phan tu lon nhat ke tiep. Bat bien luon duoc giu vung.

- Ket thuc: Vong lap dung khi i = n-1. Luc nay n-1 phan tu lon nhat da nam 
  dung vi tri, suy ra phan tu duy nhat con lai o dau mang cung da dung cho. 

=> Thuat toan dung va luon dung.
"""