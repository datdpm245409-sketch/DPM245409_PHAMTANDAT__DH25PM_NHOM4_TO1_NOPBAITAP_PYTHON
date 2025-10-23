# -------- Câu 7 --------
print("\n===== CHƯƠNG 6 - CÂU 7 =====")
lst = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    while True:
        x = float(input(f"Nhập phần tử thứ {i+1}: "))
        if i == 0 or x > lst[-1]:
            lst.append(x)
            break
        else:
            print("⚠️ Số nhập phải lớn hơn số trước đó! Nhập lại.")
print("Dãy số tăng dần:", lst)