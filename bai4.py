# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:46:27 2024

@author: abc
"""

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