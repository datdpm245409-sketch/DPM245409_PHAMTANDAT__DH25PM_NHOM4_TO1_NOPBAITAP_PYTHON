#Câu 8: Viết chương trình tính loga x 
import math 
a = float(input("Nhap co so a: "))
x = float(input("Nhap so x (>0): "))

if a > 0 and a != 1 and x > 0:
    logax = math.log(x) / math.log(a)
    print(f"log co so {a} cua {x} la: {logax}")
else
   print("Gia tri nhap khong hop le!")