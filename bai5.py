# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:46:27 2024

@author: abc
"""

# Bài 5 
import time
Nam_sinh = int(input("Nhập vào năm sinh: "))
nam_hien_tai = time.localtime().tm_year  
if Nam_sinh <= nam_hien_tai:
    tuoi = nam_hien_tai - Nam_sinh
    print("Số tuổi của bạn là: ",tuoi)
else:
    print("Lỗi!")