# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:26 2024

@author: abc
"""

# Bài 18
gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
gio1 = int(input("Nhập giờ:  "))
phut1= int(input("Nhập phút: "))
giay1 = int(input("Nhập giây: "))
Gio = gio + gio1
Phut = phut + phut1
Giay = giay + giay1
if Phut >= 60:
    Gio = Gio + 1 
    Phut = Phut - 60
if Giay >= 60:
    Phut = Phut + 1
    Giay = Giay - 60
print("{}giờ,{}phút,{}giây".format(Gio,Phut,Giay))