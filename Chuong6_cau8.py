# -------- Câu 8 --------
print("\n===== CHƯƠNG 6 - CÂU 8 =====")
n = int(input("Nhập số lượng phần tử: "))
M = [float(input(f"M[{i}] = ")) for i in range(n)]
M.sort(reverse=True)
print("Dãy sau khi sắp xếp giảm dần:", M)