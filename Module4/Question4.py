import random

# computer draws a random integer between 1 and 10
number = random.randint(1, 10)
guess = int(input("Guess a number (1, 10): "))

while guess != number:
    if guess > number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess a number (1, 10): "))

print("Correct")