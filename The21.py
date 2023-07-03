#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

while True:
    current_number = 0
    current_player = random.choice(["human", "computer"])

    while current_number <= 21:
        print("Số hiện tại:", current_number)

        if current_player == "human":
            player_choice = input("Nhập số bạn muốn chọn (1-3): ")
            while player_choice not in ['1', '2', '3']:
                player_choice = input("Nhập số bạn muốn chọn (1-3): ")
            player_choice = int(player_choice)

            current_number += player_choice

            if current_number >= 21:
                print("Số hiện tại:", current_number)
                print("Bạn đã thua!")
                break

            current_player = "computer"

        elif current_player == "computer":
            computer_choice = random.randint(1, 3)
            print("Máy tính chọn:", computer_choice)

            current_number += computer_choice

            if current_number >= 21:
                print("Số hiện tại:", current_number)
                print("Bạn đã thắng!")
                break

            current_player = "human"

    play_again = input("Bạn có muốn chơi lại không? (y/n): ")

    if play_again.lower() != "y":
        break

