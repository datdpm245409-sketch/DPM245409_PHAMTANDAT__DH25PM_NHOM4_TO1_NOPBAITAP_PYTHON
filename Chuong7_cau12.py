#Câu 12: Xử lý CSV File - Viết phần mềm Quản Lý Nhân Viên
print("\n===== CHƯƠNG 7 - CÂU 12 =====")
import csv, random
path = "data.csv"
with open(path, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    for _ in range(10):
        row = [random.randint(-50, 50) for _ in range(10)]
        writer.writerow(row)
with open(path, 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for i, row in enumerate(reader, 1):
        numbers = list(map(int, row))
        print(f"Dòng {i}: {numbers} → Tổng = {sum(numbers)}")