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

def roll_dice(keep_dice):
    
    # Catch global variable
    global dice_bag
    
    # Variables
    picked_face = []
    draw = []
    
    # Add kept dice to the draw
    draw.extend(keep_dice)    
    
    # While we dont draw 3 dices...
    while len(draw) < 3:
        # Check if bag is empty
        if len(dice_bag) == 0:
            print("\nRegenerating the bag...")
            dice_bag = generate_dice_bag()
        
        # Shuffling bag
        random.shuffle(dice_bag)
        
        # Pick a dice randomly
        picked_dice = random.choice(dice_bag)
        
        # Store the result
        draw.append(picked_dice)
        
        # Delete the dice from the list dice_bag
        dice_bag.remove(picked_dice)
        
    print("\nYou drew the following dice :")
    for dice in draw:
        # Show dice color
        print(f"- {dice[0]}")   
        # Roll the dice and store result
        picked_face.append(random.choice(dice[1]))  
    
    print("\nYou rolling the dice and you obtains the following dice :")
    for face in picked_face:
        print(f"- {face}")
    
    print(f"\nThe bag now contains {len(dice_bag)} dices")
    
    
    
    # Ask the user if they want to reroll
    while True:
        user_input = input("\nDo you want to roll dice? Yes / No: ").strip().lower()
        
        if user_input == "yes":
            
            # Check if each dice is a "step" to add it in the reroll
            for index in range(len(draw)):
                if picked_face[index] == "Step":
                    keep_dice.append(draw[index])
            
            if len(keep_dice) > 0:
                print("\n You keep the following 'Step' dice to reroll:")
                for dice in keep_dice:
                    print(f"- {dice[0]}")
                    
            input("\nPress any key to continue...")
            
            roll_dice(keep_dice)
            
        elif user_input == "no":
            print("Exiting the game. Goodbye !")
            sys.exit(0)
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")


if __name__ == "__main__":
    keep_dice = []
    roll_dice(keep_dice)
    