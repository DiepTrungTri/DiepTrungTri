# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:23 2024

@author: abc
"""

# Bài 4"
sn_2cs = int(input("Nhập vào số nguyên có 2 chữ số: "))
if 10 <= sn_2cs <= 99:
    hc = sn_2cs // 10
    hdv = sn_2cs % 10
    tong = hc + hdv
    print(tong)
else:
    print("Lỗi!")