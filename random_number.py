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
>>>>>>> d34d2e1851e884132d3976e1f4c8a00cc10ed3ec

print("Congrats! You guessed the number! It was", number)