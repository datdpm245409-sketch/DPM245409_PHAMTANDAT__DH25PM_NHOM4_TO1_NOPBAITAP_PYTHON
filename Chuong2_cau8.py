#Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python.
"""
Các loại lỗi phổ biến trong Python
a. Lỗi cú pháp (Syntax Error)

Là lỗi do sai về mặt cú pháp của ngôn ngữ, ví dụ thiếu dấu ngoặc, dấu hai chấm, lỗi indent (thụt lề)...

Python không thể chạy chương trình khi có lỗi này.

b. Lỗi ngoại lệ (Exception/Error)

Là lỗi xảy ra trong quá trình chạy chương trình (runtime error), khiến chương trình bị dừng đột ngột nếu không xử lý.

2. Cách bắt lỗi (xử lý ngoại lệ) trong Python

Python cung cấp cấu trúc try-except để xử lý lỗi, giúp chương trình không bị dừng đột ngột mà có thể xử lý hoặc thông báo lỗi theo ý muốn.

Cấu trúc cơ bản:
try:
    # Đoạn mã có thể gây lỗi
    ...
except SomeError:
    # Xử lý lỗi khi SomeError xảy ra
    ...

3. Một số lưu ý khi xử lý lỗi

Nên bắt lỗi cụ thể để xử lý đúng nguyên nhân, tránh bỏ sót lỗi tiềm ẩn.

Dùng finally để dọn dẹp tài nguyên (đóng file, kết nối cơ sở dữ liệu).

Có thể dùng raise để ném lại lỗi nếu không thể xử lý.

Viết ghi chú và thông báo lỗi rõ ràng để dễ debug.
"""