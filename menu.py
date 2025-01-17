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
menu_choice = input("Do you want to roll dice ? Yes / No ")
if menu_choice == "yes":
    zompydice.roll_dice()
else:
    print("Exiting")
    sys.exit(0)

