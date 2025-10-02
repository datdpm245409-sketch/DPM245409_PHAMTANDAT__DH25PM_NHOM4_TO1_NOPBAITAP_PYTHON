d, m, y = map(int, input("Nhập ngày/tháng/năm: ").split("/"))

days_in_month = [31, 29 if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0) else 28,
                 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d += 1
if d > days_in_month[m-1]:
    d = 1
    m += 1
    if m > 12:
        m = 1
        y += 1

print(f"Ngày kế tiếp: {d}/{m}/{y}")