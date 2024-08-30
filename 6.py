# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 23:33:24 2024

@author: abc
"""

# Bài 6
import time
namsinh = int(input("Nhập vào năm sinh: "))
namhientai = time.localtime().tm_year
if namsinh <= namhientai:
    tuoi = namhientai - namsinh
    print(tuoi)
else:
    print("Lỗi!")