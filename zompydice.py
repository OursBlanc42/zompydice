#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:21:23 2025

@author: oursblanc
"""

import random


# Dice definition
green = ['Brain', 'Brain', 'Brain', 'Step', 'Step', 'Bite']
yellow = ['Brain', 'Brain', 'Step', 'Step', 'Bite', 'Bite']
red = ['Brain', 'Step', 'Step', 'Bite', 'Bite', 'Bite']

dice_bag = [green, green, green, yellow, yellow, red]

random.shuffle(dice_bag)

print("Dice bage shuffling : ", dice_bag)
