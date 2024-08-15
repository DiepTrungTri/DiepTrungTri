# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 06:18:06 2024

@author: abc
"""

# Nhập điểm GPA
GPA = float(input("Nhập điểm GPA: "))
if GPA < 3.5:
    print("Học lực Kém")
elif 5.0 <= GPA < 5.0:
    print("Học lực Yếu")
elif 5.0 <= GPA < 7.0:
    print("Học lực Trung bình")
elif 7.0 <= GPA < 8.0:
    print("Học lực Khá")
elif 8.0 <= GPA < 9.0:
    print("Học lực Giỏi")
elif 9.0 <= GPA <= 10:
    print("Học lực Xuất sắc")
else:
    print("Không hợp lệ")