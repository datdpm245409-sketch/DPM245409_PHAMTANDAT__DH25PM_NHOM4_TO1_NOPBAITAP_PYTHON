# -------- Câu 6 --------
print("\n===== CHƯƠNG 6 - CÂU 6 =====")
from random import sample
n = int(input("Nhập số phần tử: "))
lst = sample(range(0, 100), n)
print("Danh sách ngẫu nhiên không trùng:", lst)