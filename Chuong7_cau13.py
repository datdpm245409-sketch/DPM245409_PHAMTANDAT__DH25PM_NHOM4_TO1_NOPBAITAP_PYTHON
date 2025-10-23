#Câu 13: Xử lý XML File - Viết phần mềm Quản Lý Thiết Bị
print("\n===== CHƯƠNG 7 - CÂU 13 =====")
from xml.dom.minidom import parse
nhom_tree = parse("nhomthietbi.xml")
nhoms = nhom_tree.getElementsByTagName("nhom")
print("Danh sách nhóm:")
for n in nhoms:
    ma = n.getElementsByTagName("ma")[0].firstChild.data
    ten = n.getElementsByTagName("ten")[0].firstChild.data
    print(ma, "-", ten)

tb_tree = parse("thietbi.xml")
thietbis = tb_tree.getElementsByTagName("thietbi")
ds = []
for tb in thietbis:
    manhom = tb.getAttribute("manhom")
    ma = tb.getElementsByTagName("ma")[0].firstChild.data
    ten = tb.getElementsByTagName("ten")[0].firstChild.data
    ds.append((manhom, ma, ten))

print("\nToàn bộ thiết bị:")
for t in ds:
    print(t)

chon = input("Nhập mã nhóm cần lọc: ")
loc = [t for t in ds if t[0] == chon]
print("Thiết bị thuộc nhóm", chon, ":", loc)

from collections import Counter
dem = Counter(t[0] for t in ds)
max_nhom = max(dem, key=dem.get)
print("Nhóm có nhiều thiết bị nhất:", max_nhom, "với", dem[max_nhom], "thiết bị")