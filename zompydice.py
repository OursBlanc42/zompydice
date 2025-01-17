#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:21:23 2025

@author: oursblanc
"""

# import librairies
import sys
import random

# declare global variable
dice_bag = []

def generate_dice_bag():
    
    # Dice definition
    green = ('Green', ['Brain', 'Brain', 'Brain', 'Step', 'Step', 'Bite'])
    yellow = ('Yellow', ['Brain', 'Brain', 'Step', 'Step', 'Bite', 'Bite'])
    red = ('Red', ['Brain', 'Step', 'Step', 'Bite', 'Bite', 'Bite'])
    
    # Return the dice bag with the correct distribution
    return 6 * [green] + 4 * [yellow] + 3 * [red]

def roll_dice():
    
    # Catch global variable
    global dice_bag
    
    # Dice bag generation if bag is empty
    if len(dice_bag) <= 0:
        print("\nRegenerating the bag...")
        dice_bag = generate_dice_bag()
    
    # Variables
    launch = 0
    draw = []
    
    while launch < 3:
        
        # Shuffling bag
        random.shuffle(dice_bag)
        
        # Pick a random dice
        picked_dice = random.choice(dice_bag)
        
        # Extract the name and faces
        dice_color, dice_face = picked_dice
        
        # Store the result
        draw.append(picked_dice)
        
        # Delete the dice from the list dice_bag
        dice_bag.remove(picked_dice)
        
        # Increment number
        launch += 1
          
    print("\nYou drew the following dice :")
    for D in draw:
        print(D[0]) 
    
    print("\nYou rolling the dices and you obtains the following faces :")
    for D in draw:
        picked_face = random.choice(dice_face)
        print(picked_face)

    print(f"The bag now contains {len(dice_bag)} dices")
    
    while True:
        user_input = input("\nDo you want to roll dice? Yes / No: ").strip().lower()
        
        if user_input == "yes":
            roll_dice()
        elif user_input == "no":
            print("Exiting the game. Goodbye !")
            sys.exit(0)
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")
    
if __name__ == "__main__":
    roll_dice()
    