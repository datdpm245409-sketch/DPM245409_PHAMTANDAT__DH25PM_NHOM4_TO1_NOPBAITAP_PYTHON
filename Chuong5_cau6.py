#Câu 6: Trích lọc số âm trong chuỗi 
import re   

def NegativeNumberInStrings(s):
    # Biểu thức chính quy để tìm các số nguyên âm
    # (?<!-) đảm bảo dấu '-' không nằm sau một dấu '-' khác (loại bỏ trường hợp '--')
    # -\d+ nghĩa là dấu trừ và ít nhất một chữ số
    numbers = re.findall(r'(?<!-)-\d+', s)

    
    nums = [int(x) for x in numbers]

    
    print("Các số nguyên âm tìm thấy:", nums)
    return nums


chuoi = "abc-5xyz-12k9l--p"
NegativeNumberInStrings(chuoi)