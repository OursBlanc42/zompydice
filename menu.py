#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:21:23 2025

@author: oursblanc
"""
# import librairies
import sys

# import other files
import zompydice

# Menu
while True:
    menu_choice = input("Do you want to play ? Yes / No: ").strip().lower()

    if menu_choice == "yes":
        score = 0
        hp = 3
        zompydice.roll_dice([], score, hp)
    elif menu_choice == "no":
        print("Exiting the game. Goodbye !")
        sys.exit(0)
    else:
        print("Invalid input. Please answer 'yes' or 'no'.")
