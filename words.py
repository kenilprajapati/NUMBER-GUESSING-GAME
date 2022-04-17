  

import random

print("Number Guessing Game")

# randint function to generate the random number between 1 to 9
number = random.randint(1,9)

# number of chances to be given to the user to guess the number
# or it is the inputs given by user into input box here number of chances are 5
chances = 0

print("Guess a number (between 1 and 9):")

# While loop to count the number of chances
while chances < 5 :

    # Enter a number between 1 to 9 
    guess = int(input("Enter your guess:-"))



    if guess == number:



        print("Congratulation You Won!!")
        break


    elif guess < number:
        print("You guess was too low: Guess a number higher then",guess)


    else:
        print("Your guess was too high : Guess a number lower then", guess)

        chances += 1