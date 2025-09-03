# Asks the user how many dice to roll
import random

dice_count = int(input("How many dice to roll: "))
total = 0

for i in range(dice_count):
    roll = random.randint(1, 6)
    total += roll

print("Sum of the dice:", total)