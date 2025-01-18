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

"""
Function to debug
switch the comment from pass to print to ignore the debug
"""
def debug(message):
    print(f"\t[DEBUG]\t{message}")
    # pass

def generate_dice_bag():
    
    # Dice definition
    green = ('Green', ['Brain', 'Brain', 'Brain', 'Step', 'Step', 'Bite'])
    yellow = ('Yellow', ['Brain', 'Brain', 'Step', 'Step', 'Bite', 'Bite'])
    red = ('Red', ['Brain', 'Step', 'Step', 'Bite', 'Bite', 'Bite'])
    
    # Return the dice bag with the correct distribution
    return 6 * [green] + 4 * [yellow] + 3 * [red]

def roll_dice(keep_dice,score,hp):
    
    # Catch global variable
    global dice_bag
    
    # Variables
    picked_face = []
    draw = []
    
    # Add kept dice to the draw
    draw.extend(keep_dice)    
    
    debug("HP before roll".ljust(30) + f"hp = {hp}")
    debug("Score before roll".ljust(30) + f"score = {score}")
    debug("Kept dice".ljust(30) + f"keep_dice = {[dice[0] for dice in keep_dice]}")
    debug("Dice added to draw".ljust(30) + f"draw = {[dice[0] for dice in draw]}")
    debug("Draw size before refill".ljust(30) + f"len(draw) = {len(draw)}")


    # While we dont draw 3 dices...
    while len(draw) < 3:
        
        # Check if bag is empty
        if len(dice_bag) == 0:
            print("\nGenerating the bag...")
            dice_bag = generate_dice_bag()
        
        # Shuffling bag
        random.shuffle(dice_bag)
        
        # Pick a dice randomly
        picked_dice = random.choice(dice_bag)
        
        # Store the result
        draw.append(picked_dice)
        
        # Delete the dice from the list dice_bag
        dice_bag.remove(picked_dice)
        
        debug("PICK A DIE FROM BAG AND STORE IN THE DRAW")
        debug("Dice picked".ljust(30) + f"picked_dice = {picked_dice[0]}")
        debug("Dice bag content".ljust(30) + f"dice_bag = {[dice[0] for dice in dice_bag]}")
        debug("Dice count in bag".ljust(30) + f"len(dice_bag) = {len(dice_bag)}")
        debug("Draw content".ljust(30) + f"draw = {[dice[0] for dice in draw]}")
        debug("Dice count in draw".ljust(30) + f"len(draw) = {len(draw)}")
        
    # Reset keep_dice after draw completion
    keep_dice = []
        
    print("\nYou drew the following dice :")
    for dice in draw:
        # Show dice color
        print(f"- {dice[0]}")   
        # Roll the dice and store result
        picked_face.append(random.choice(dice[1]))  
    
    print("\nYou rolled the dice and obtained the following faces :")
    for face in picked_face:
        print(f"- {face}")
        
        # Update HP and check if you can continue to play
        if face == "Bite":
            hp -= 1
        
        if hp <= 0:
            print(f"\nYou are dead (HP = {hp}). Here is your brain score: {score} !")
            input("\nPress any key to exit...")
            print("Exiting the game. Goodbye !")
            sys.exit(0)
            
        if face == "Brain":
            score += 1
            
    print(f"\nYou survived another round ! Your HP is {hp} and your brain score is {score} !")
    print(f"\nThe bag now contains {len(dice_bag)} dice")
    
    
    # Ask the user if they want to reroll
    while True:
        user_input = input("\nDo you want to roll the dice ? Yes / No: ").strip().lower()
        
        if user_input == "yes":
            
            # Check if each dice is a "step" to add it in the reroll
            for index in range(len(draw)):
                if picked_face[index] == "Step":
                    keep_dice.append(draw[index])
            
            if len(keep_dice) > 0:
                print("\nYou are keeping the following 'Step' dice to reroll :")
                for dice in keep_dice:
                    print(f"- {dice[0]}")
                    
            input("\nPress any key to continue...")
            
            roll_dice(keep_dice,score,hp)
            
        elif user_input == "no":
            print(f"\nYou fled cowardly. Here is your brain score: {score} !")
            input("\nPress any key to exit...")
            print("Exiting the game. Goodbye !")
            sys.exit(0)
        else:
            print("Invalid input. Please type 'Yes' or 'No'.")


if __name__ == "__main__":
    print("Please run from main.py")
    sys.exit(0)
    