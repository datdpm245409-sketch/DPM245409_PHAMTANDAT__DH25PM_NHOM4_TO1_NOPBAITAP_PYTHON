#Câu 5: Xử lý chuỗi với các hàm cơ bản
chuoi = input("Nhập vào một chuỗi: ")


dem_hoa = dem_thuong = dem_so = dem_ktdb = dem_space = 0
dem_nguyen_am = dem_phu_am = 0


nguyen_am = "aeiouAEIOU"


for ch in chuoi:
    if ch.isupper():       # Ký tự in hoa
        dem_hoa += 1
    elif ch.islower():     # Ký tự in thường
        dem_thuong += 1
    elif ch.isdigit():     # Ký tự là số
        dem_so += 1
    elif ch.isspace():     # Ký tự là khoảng trắng
        dem_space += 1
    else:                  # Ký tự đặc biệt
        dem_ktdb += 1

    
    if ch.isalpha():  # Chỉ xét các ký tự chữ cái
        if ch in nguyen_am:
            dem_nguyen_am += 1
        else:
            dem_phu_am += 1


print("-" * 40)
print("Số chữ IN HOA       :", dem_hoa)
print("Số chữ in thường    :", dem_thuong)
print("Số chữ là chữ số    :", dem_so)
print("Số ký tự đặc biệt   :", dem_ktdb)
print("Số ký tự khoảng trắng:", dem_space)
print("Số chữ Nguyên Âm    :", dem_nguyen_am)
print("Số chữ Phụ Âm       :", dem_phu_am)
print("-" * 40)