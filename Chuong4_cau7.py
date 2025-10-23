#Câu 7: Tính và xuất độ dài đoạn AB 
import math

xA = float(input("Nhap hoanh do xA: "))
yA = float(input("Nhap tung do yA: "))
xB = float(input("Nhap hoanh do xB: "))
yB = float(input("Nhap hoanh do yB: "))

AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Do dai doan AB la: ", AB)