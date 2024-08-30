# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:27 2024

@author: abc
"""

# Bài 24
gio = float(input("Nhập giờ: "))
phut = float(input("Nhập phút: "))
giay = float(input("Nhập giây: "))
if 0 < gio <= 24 and 0 < phut <= 60 and 0 < giay < 60:
    print("{} giờ,{} phút,{} giây".format(gio, phut, giay))
else:
    print("Lỗi!")