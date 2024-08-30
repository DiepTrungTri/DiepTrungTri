# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:24 2024

@author: abc
"""

# Bài 8
chieucao = float(input("Nhập chiều cao: "))
cannang = float(input("Nhập cân nặng: "))
bmi = cannang / (chieucao**2)
if bmi <= 18.5:
    print("Bạn thiếu cân")
elif 18.5 <= bmi <= 24.9:
    print("Bạn có cân nặng bình thường")
else:
    print("Bạn thừa cân")