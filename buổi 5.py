# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 09:20:20 2024

@author: abc
"""

# Bài 1 
# Nhập vào
a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
c = int(input("Nhập vào c: "))
d = int(input("Nhập vào d: "))
# Công thức
T_B_C = (a + b + c + d ) / 4
print("Kết quả là: ",T_B_C)
# Bài 2
# Nhập vào
a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
# Tổng 
T = a + b 
print("Tổng là: ",T)
# Hiệu
H = a - b
print("Hiệu là:",H)
# Tích
T_i = a * b
print("Tích là:",T_i)
# Thương
T_g = a / b
print("Thương là: ",round(T_g,2))
# Chia lấy dư
C_l_d = a % b
print("Chia lấy dư là: ",round(C_l_d,2))
# Chia lấy nguyên
C_l_n = a // b
print("Chia lấy nguyên là: ",round(C_l_n,2))
# Bài 3 
# Nhập vào
N = int(input("Nhập vào số nguyên dương có 2 chữ số: "))
# Điều kiện
if N >= 10 <= 99:
    hang_chuc = N // 10
    hang_don_vi = N % 10
    tong = hang_chuc + hang_don_vi
    print(f"Tổng các chữ số {N} là: {hang_chuc} + {hang_don_vi} = {tong}")
else:
    print("Lỗi!")         
# Bài 4 
gio = int(input("Nhập vào giờ: "))
phut = int(input("Nhập vào phút: "))
giay = int(input("Nhập vào giây: "))
if  0 < gio <= 24:
    0 < phut <= 60
    0 < giay <= 60
    tong_giay = gio * 3600 + phut * 60 + giay
    print("Ta có giây là: ",tong_giay)
else:
    print("Lỗi!")
# Bài 5 
import time
Nam_sinh = int(input("Nhập vào năm sinh: "))
nam_hien_tai = time.localtime().tm_year  
if Nam_sinh <= nam_hien_tai:
    tuoi = nam_hien_tai - Nam_sinh
    print("Số tuổi của bạn là: ",tuoi)
else:
    print("Lỗi!")
# Bài 6
a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
c = int(input("Nhập vào c: "))
if a != 0:
   print(f"{a}X^2 + {b}X + {c} = 0")
else:
    print("Lối!")
# Bài 7 
print("=========== MENU ============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("==============================")
choice = input("Mời nhập lựa chọn: ")
print("==============================")
print(f"Lựa chọn bạn đã chọn: {choice}")
# Bài 8
A =float(32**0.2 - (1/64)**-0.25 + (8/27)**(1/3))
print("Kết quả là:",round(A,3))
# Bài 9 
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b:"))
sqrt_a = math.sqrt(a)
sqrt_b = math.sqrt(b)
sqrt_ab = math.sqrt(a * b)

fourth_root_a = a ** (1/4)
fourth_root_b = b ** (1/4)
fourth_root_ab = sqrt_ab ** (1/4)

# Biểu thức tính toán
result = ((sqrt_a - sqrt_b) / (fourth_root_a - fourth_root_b)) - ((sqrt_a + fourth_root_ab) / (fourth_root_a + fourth_root_b))
print(result)
# Bài 1 string
text1 = "Đại học Quốc gia"
words1 = text1.split()
text2 = "Khu phố 6"
words2= text2.split()
text3 = "P.Linh Trung"
words3= text3.split()
text4 = "Q.Thủ Đức"
words4= text4.split()
text5 = "Tp.Hồ Chí Minh"
words5= text5.split()
print(words1, "\n",words2, "\n", words3, "\n", words4, "\n", words5)
# 2 string 
texts = ["Đại học Quốc gia", "Khu phố 6", "Linh Trung", "Thủ Đức", "Hồ Chí Minh"]
for text in texts:
    words = text.split()
    print(words)
# Bài 2 chuyển chuỗi
a = "I'm a cat"
print(a.capitalize())
print(a.title())
print(a.upper())
a_transformed = a[0].lower() + a[1:3].upper() + a[3:5] + a[5:].upper()
print(a_transformed)
