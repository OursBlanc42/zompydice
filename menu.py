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
        zompydice.roll_dice()
    elif menu_choice == "no":
        print("Exiting.")
        sys.exit(0)
    else:
        print("Invalid input. Please answer 'yes' or 'no'.")