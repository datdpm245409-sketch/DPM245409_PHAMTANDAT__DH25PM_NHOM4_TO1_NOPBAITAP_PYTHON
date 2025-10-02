month = int(input("Nhập tháng (1-12): "))

if 1 <= month <= 3:
    print("Quý 1")
elif 4 <= month <= 6:
    print("Quý 2")
elif 7 <= month <= 9:
    print("Quý 3")
elif 10 <= month <= 12:
    print("Quý 4")
else:
    print("Tháng không hợp lệ")