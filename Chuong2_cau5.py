#Câu 5: Trình bày các loại ghi chú trong Python. 
"""
Ghi chú đơn dòng (Single-line comments):

Dùng dấu # để tạo ghi chú cho một dòng. Mọi thứ sau dấu # sẽ bị Python bỏ qua.


2. Ghi chú đa dòng (Multi-line comments):

Python không có cú pháp ghi chú chính thức cho nhiều dòng, nhưng người ta thường sử dụng chuỗi đa dòng ('''...''' hoặc """...""") để tạo ghi chú dài hoặc nhiều dòng. Dù chuỗi này thường được dùng để định nghĩa chuỗi, nhưng nếu không được gán cho biến nào, nó sẽ được bỏ qua trong quá trình thực thi.

3. Ghi chú dùng cho tài liệu (Docstrings):

Là loại ghi chú đặc biệt được sử dụng để mô tả mục đích và cách thức hoạt động của một hàm, lớp, hoặc mô-đun.

Docstrings sử dụng dấu """...""" hoặc '''...''' và nên được đặt ngay dưới định nghĩa hàm hoặc lớp.

Docstrings sẽ được Python tự động lưu trữ trong thuộc tính __doc__ của hàm hoặc lớp, giúp người dùng có thể tra cứu thông tin mô tả.

4. Ghi chú tạm thời (TODO comments):

Loại ghi chú này được dùng để đánh dấu các phần mã cần hoàn thiện hoặc chỉnh sửa sau. Chúng thường bắt đầu bằng từ khóa TODO.
"""