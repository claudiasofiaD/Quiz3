import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

while guess != number:
    if guess < number:
        print("Too low!")
    else:
        print("Too high!")
<<<<<<< HEAD
    guess = int(input("Make another guess: "))
=======
    guess = int(input("Try again: "))
>>>>>>> 71dd1d518bb455621ff54fa26ed4067aacff353f

print("Congrats! You guessed the number! It was", number)
