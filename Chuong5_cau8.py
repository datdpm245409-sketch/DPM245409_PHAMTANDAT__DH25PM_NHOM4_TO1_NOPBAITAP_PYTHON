#Câu 8: Tách lấy tên bài hát
import os


def LayTenFile(day_duong_dan):
    ten_file = os.path.basename(day_duong_dan)
    return ten_file


def LayTenKhongPhanMoRong(day_duong_dan):
    ten_khong_mo_rong = os.path.splitext(os.path.basename(day_duong_dan))[0]
    return ten_khong_mo_rong


duong_dan = r"d:\music\muabui.mp3"

print("Đường dẫn:", duong_dan)
print("Tên file có phần mở rộng:", LayTenFile(duong_dan))
print("Tên file không có phần mở rộng:", LayTenKhongPhanMoRong(duong_dan))