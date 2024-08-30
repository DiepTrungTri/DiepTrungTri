# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:25 2024

@author: abc
"""

# Bài 13
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if 0 < ngay <= 31 and 0 < thang <= 12:
#a
    print(f"{ngay}/{thang}/{nam}")
    print(f"{nam}/{thang}/{ngay}")
#b
    print(f"{ngay}/{thang}/{str(nam)[-2:]}")
    print(f"{str(nam)[-2:]}/{thang}/{ngay}")
#c
    print(f"{nam}/{thang}/{ngay}")
    print(f"{ngay}/{thang}/{nam}")
else:
    print("Lỗi!")