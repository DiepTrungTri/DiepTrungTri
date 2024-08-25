# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:46:27 2024

@author: abc
"""

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
