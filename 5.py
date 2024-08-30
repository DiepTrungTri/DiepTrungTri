# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:23 2024

@author: abc
"""

# Bài 5
gio = float(input("Nhập giờ: "))
phut = float(input("Nhập phút: "))
giay = float(input("Nhập giây: "))
print(f"{gio}giờ/{phut}phút/{giay}giây")
if 0 < gio <= 24 and 0 < phut <= 60 and 0 < giay <= 60:    
    tong = gio * 3600 + phut * 60 + giay
    print(f"Tổng số giây là {tong}")
else:
    print("Lỗi!")