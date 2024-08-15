# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:10:02 2024

@author: abc
"""

# Xét a,b,c là cạnh tam 
a, b, c = map(float,input("Nhập a, b, c: ").split())
# Điều kiện
if a + b > c and a + c > b and b + c > a:
   if a==b or a==c or b==c:
       loaitamgiac = "Cân"
   elif a==b and b==c:
       loaitamgiac = "Đều"
   elif a*a==b*b +c*c or b*b==a*a +c*c or c*c==a*a +b*b:
       loaitamgiac = "Vuông"
   print("{}, {}, {} là 3 cạnh của tam giác {}".format(a,b,c,loaitamgiac))
else:
   print("{}, {}, {} không là 3 cạnh của tam giác".format(a,b,c,))
       
   