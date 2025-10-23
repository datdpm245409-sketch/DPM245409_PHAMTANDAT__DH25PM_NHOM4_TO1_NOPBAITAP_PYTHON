#Câu 13: Hàm kiểm tra số hoàn thiện, số thịnh vượng
def sum_of_divisors(n):
    tolal = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
        return total

def is_perfect(n)
 return sum_of_divisors(n) == n

def is_abundant(n):
    return sum_of_divisors(n) > n

num = int(input("Nhap so can kiem tra: "))

if is_perfect(num):
    print(f"{num} la so hoan thien")
elif is_abundant(num):
    print(f"{num} la so thinh vuong")
else
    print(f"{num} khong phai so hoan thien hoac thinh vuong")