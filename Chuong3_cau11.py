while True:
    n = int(input("Nhập số nguyên dương: "))
    if n < 2:
        print(n, "không phải số nguyên tố")
    else:
        prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prime = False
                break
        if prime:
            print(n, "là số nguyên tố")
        else:
            print(n, "không phải số nguyên tố")
    
    hoi = input("Bạn có muốn tiếp tục? (c/k): ")
    if hoi == "k":
        break