# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:26 2024

@author: abc
"""

# Bài 16
gio = float(input("Nhập vào giờ: "))
phut = float(input("Nhập vào phút: "))
giay = float(input("Nhập vào giây: "))
tonggiay = gio * 3600 + phut * 60 + giay
print(tonggiay)