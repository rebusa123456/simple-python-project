import random

number = random.randint(1, 10)
guess = 0

print("Number Guessing Game")
print("Guess a number from 1 to 10")

while guess != number:
    guess = int(input("Enter your guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
