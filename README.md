# **Zompydice 🧟‍♂️🎲**  

A Python rewrite of the Zombiedice tabletop game.

---
## **Table of Contents**  
1. [Overview](#overview)  
2. [Features](#features)  
3. [Planned Updates](#planned-updates)  
4. [Installation](#installation)  
5. [Quick Rules](#quick-rules)  
6. [About Dice](#about-dice)  
7. [Handmade with love using...](#handmade-with-love-using)  
8. [License](#license)  
9. [Contributing](#contributing)  
10. [Contact](#contact)
---

## **Overview**  
Zompydice is a personal project designed to practice and enhance my Python programming skills. The project goes beyond the foundations I learned during my career transition at Holberton School.

The game implements the core mechanics of Zombiedice, allowing players to roll dice, track scores, and manage health points. While this version focuses on replicating the original gameplay, future updates may add new features or improvements.  

For the original Zombiedice rules, visit the official site: [Zombiedice Rules](https://www.sjgames.com/dice/zombiedice/).

This project was started during my training, so I'm still learning, and some parts can certainly be improved. I haven't seen all the relevant concepts yet, so thank you for your indulgence.

## **Features**  
- Single-player mode with score and health tracking.  
- Dice rolling mechanics inspired by the original game.  
- Debugging tools to monitor gameplay (optional).  
- Designed for terminal-based play.  

## **Planned Updates**  
- Support for two players
- Improved visuals with ASCII art for dice.  
- Enhanced user interface with color-coded text.  

## **Installation**  
1. Clone this repository:  
   ```bash
   git clone https://github.com/OursBlanc42/zompydice
   ```
2. Navigate to the project folder:  
   ```bash
   cd zompydice
   ```
3. Run the game:  
   ```bash
   python3 menu.py
   ```

## **Quick rules*
- **Objective:** Survive the zombie apocalypse by collecting as many 🧠 (brains) as possible without losing all your ❤️ (HP).
- **Gameplay:**
  1. Roll 3 dice per turn.
  2. Dice results can be:
     - **🧠 Brain:** You successfully eat a brain.
     - **👣 Step:** The victim escapes; reroll this dice if you decide to continue.
     - **💥 Bite:** You get bitten! Lose 1 HP.
  3. You can reroll the dice showing 👣, but beware—pushing your luck might cost you!
- **Win condition:**
  - Collect the highest number of 🧠 before running out of ❤️.
- **Lose condition:**
  - Lose all your ❤️, and the zombies win! 🧟‍♂️

## **About Dice** 🎲  
There are three types of dice in the game, each with different probabilities:

- **Green Dice (x6):** 🧠 🧠 🧠 👣 👣 💥 — The safest dice with more brains.
- **Yellow Dice (x4):** 🧠 🧠 👣 👣 💥 💥 — A balanced mix of results.
- **Red Dice (x3):** 🧠 👣 👣 💥 💥 💥 — The riskiest dice with more bites.

The color of the dice determines how risky it is to roll them, adding a strategic element to the game.


## ** Handmade with love with... **
- Python 3.10.12
- Spyder6
- Linux Mint 21.3 x86_64 / Kernel: 5.15.0-130-generic 

## **License**  
This project is licensed under the [CC BY-NC 4.0 License](http://creativecommons.org/licenses/by-nc/4.0/).

## **Contributing**  
Rather than accepting direct contributions, this project is primarily a training exercise for me to learn and grow. I deeply appreciate feedback or guidance to help me improve. Instead of submitting pull requests with perfectly polished code, please consider sharing suggestions or pointing me in the right direction.

## **Contact**  
For questions or feedback, feel free to reach out via GitHub.


