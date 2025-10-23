#Câu 7: Tối ưu chuỗi danh từ
def ToiUuChuoiDanhTu(chuoi):
    
    chuoi = chuoi.strip()
    
    
    tu = chuoi.split()
    
    
    tu_chuan = [t.capitalize() for t in tu]
    
    
    chuoi_toi_uu = " ".join(tu_chuan)
    
    return chuoi_toi_uu


chuoi_nhap = "    TRần    duY    thAnH   "
ket_qua = ToiUuChuoiDanhTu(chuoi_nhap)

print("Chuỗi gốc: ", repr(chuoi_nhap))
print("Chuỗi tối ưu:", repr(ket_qua))
