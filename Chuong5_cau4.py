#Câu 4: Các hàm quan trọng trong xử lý chuỗi của Python 
len(s)	Trả về độ dài chuỗi	
str()	Chuyển kiểu dữ liệu khác sang chuỗi
s.upper()	Chuyển tất cả ký tự sang chữ hoa	
s.lower()	Chuyển tất cả ký tự sang chữ thường	
s.capitalize()	Viết hoa chữ cái đầu tiên	
s.title()	Viết hoa chữ cái đầu mỗi từ	
s.swapcase()	Đảo ngược hoa ↔ thường
s.strip()	Xóa khoảng trắng ở đầu và cuối chuỗi	
s.lstrip()	Xóa khoảng trắng bên trái	
s.rstrip()	Xóa khoảng trắng bên phải
s.find(sub)	Trả về vị trí đầu tiên của chuỗi con sub, hoặc -1 nếu không có	
s.rfind(sub)	Tìm từ phải sang trái	
s.index(sub)	Giống find(), nhưng báo lỗi nếu không tìm thấy	
s.replace(old, new)	Thay thế chuỗi con old bằng new
s.startswith(sub)	Kiểm tra chuỗi bắt đầu bằng sub	
s.endswith(sub)	Kiểm tra chuỗi kết thúc bằng sub	
s.isalpha()	Kiểm tra chỉ chứa chữ cái	
s.isdigit()	Kiểm tra chỉ chứa chữ số	
s.isalnum()	Kiểm tra chỉ chứa chữ và số	
s.isspace()	Kiểm tra chỉ chứa khoảng trắng
s.split(sep)	Cắt chuỗi thành danh sách dựa trên sep	
s.rsplit(sep)	Cắt từ phải sang trái	
sep.join(list)	Nối danh sách thành chuỗi, chèn sep giữa các phần tử
s.center(width, fillchar)	Căn giữa trong khung độ rộng width	
s.ljust(width, fillchar)	Căn trái	
s.rjust(width, fillchar)	Căn phải
% formatting	
str.format()	
f-string (Python 3.6+)