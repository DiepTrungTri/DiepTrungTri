# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 03:44:17 2024

@author: abc
"""

import random

# Lựa chọn của người chơi
player_choice = input("Chọn kéo, búa, hoặc bao: ").lower()

# Kiểm tra lựa chọn có hợp lệ hay không
if player_choice not in ["kéo", "búa", "bao"]:
    print("Lựa chọn không hợp lệ. Vui lòng chọn kéo, búa, hoặc bao.")
else:
    # Lựa chọn ngẫu nhiên của máy
    choices = ["kéo", "búa", "bao"]
    computer_choice = random.choice(choices)
    print(f"Máy chọn: {computer_choice}")

    # So sánh kết quả
    if player_choice == computer_choice:
        print("Kết quả: Hòa!")
    elif (player_choice == "kéo" and computer_choice == "bao") or \
         (player_choice == "búa" and computer_choice == "kéo") or \
         (player_choice == "bao" and computer_choice == "búa"):
        print("Kết quả: Người thắng!")
    else:
        print("Kết quả: Máy thắng!")