a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
op = input("Nhập phép toán (+ - * /): ")

if op == "+":
    print("Kết quả:", a + b)
elif op == "-":
    print("Kết quả:", a - b)
elif op == "*":
    print("Kết quả:", a * b)
elif op == "/":
    if b == 0:
        print("Lỗi chia cho 0")
    else:
        print("Kết quả:", a / b)
else:
    print("Phép toán không hợp lệ")