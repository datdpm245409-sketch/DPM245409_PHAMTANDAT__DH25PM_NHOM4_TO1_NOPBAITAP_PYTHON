#Câu 9: Xử lý Text File - Viết phần mềm Quản Lý sản phẩm
print("\n===== CHƯƠNG 7 - CÂU 9 =====")
def luu_file(path, data):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(data + "\n")

def doc_file(path):
    arr = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            arr.append(line.strip().split(';'))
    return arr

def xuat_sp(ds):
    for sp in ds:
        print('\t'.join(sp))
path = "sanpham.txt"
masp = input("Mã SP: ")
tensp = input("Tên SP: ")
dongia = input("Đơn giá: ")
luu_file(path, f"{masp};{tensp};{dongia}")
ds = doc_file(path)
ds.sort(key=lambda x: float(x[2]), reverse=True)
print("Danh sách sản phẩm sắp xếp theo giá giảm dần:")
xuat_sp(ds)
