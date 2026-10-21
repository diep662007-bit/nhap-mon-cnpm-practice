danh_sach_sinh_vien = []
so_luong_sinh_vien = 5
print(f"Vui lòng nhập tên của {so_luong_sinh_vien} sinh viên:")
for i in range(so_luong_sinh_vien):
        ten = input(f"Nhập tên sinh viên thứ {i + 1}: ")
        danh_sach_sinh_vien.append(ten)
        danh_sach_sinh_vien.sort()
print(f"Danh sách sinh viên theo thứ tự tên tăng dần (ABC):")
print(" ")