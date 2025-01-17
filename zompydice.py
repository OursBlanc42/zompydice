#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:21:23 2025

@author: oursblanc
"""

import sys
import random

def roll_dice():
    # Dice definition
    green = ('Green', ['Brain', 'Brain', 'Brain', 'Step', 'Step', 'Bite'])
    yellow = ('Yellow', ['Brain', 'Brain', 'Step', 'Step', 'Bite', 'Bite'])
    red = ('Red', ['Brain', 'Step', 'Step', 'Bite', 'Bite', 'Bite'])
    
    # Dice bag generation
    dice_bag = [green, green, green, yellow, yellow, red]
    
    random.shuffle(dice_bag)
    
    # Pick a random dice
    picked_dice = random.choice(dice_bag)
    
    # Extract the name and faces
    dice_color, dice_face = picked_dice
    
    # Roll the dice
    picked_face = random.choice(dice_face)
    
    print(f"\nI'm shuffling the dice bag and picked a {dice_color} die with these faces :")
    for item in dice_face:
        print(item, end=", ")
    
    print(f"\n\nI'm shuffling this {dice_color} die and picked this face: {picked_face}")
    
    while True:
        reroll_choice = input("\nDo you want to reroll dice ? Yes / No ").strip().lower()
    
        if reroll_choice == "yes":
            roll_dice()
        elif reroll_choice == "no":
            print("Exiting.")
            sys.exit(0)
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")
        
        
if __name__ == "__main__":
    roll_dice()
    
    