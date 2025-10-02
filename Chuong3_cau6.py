n = int(input("Nhập số (0-99): "))

hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi",
             "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
hang_donvi = ["", "một", "hai", "ba", "bốn", "năm",
              "sáu", "bảy", "tám", "chín"]

if n < 10:
    print(hang_donvi[n])
else:
    chuc = n // 10
    donvi = n % 10
    print(hang_chuc[chuc], hang_donvi[donvi])