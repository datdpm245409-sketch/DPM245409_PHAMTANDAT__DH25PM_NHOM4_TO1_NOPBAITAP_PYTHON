#Câu 10: Xử lý JSON File - Viết phần mềm Quản Lý Sinh Viên
print("\n===== CHƯƠNG 7 - CÂU 10 =====")
import json
path = "sinhvien.json"
lop = {
    "ma_lop": "CTK43",
    "ten_lop": "CNTT 43",
    "sinhvien": [
        {"ma": "sv1", "ten": "Nguyễn A", "namsinh": 2003},
        {"ma": "sv2", "ten": "Trần B", "namsinh": 2004},
        {"ma": "sv3", "ten": "Lê C", "namsinh": 2002}
    ]
}
with open(path, 'w', encoding='utf-8') as f:
    json.dump(lop, f, ensure_ascii=False, indent=4)
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
print("Danh sách sinh viên:")
for sv in data['sinhvien']:
    print(f"{sv['ma']}\t{sv['ten']}\t{sv['namsinh']}")