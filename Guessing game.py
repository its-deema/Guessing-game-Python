import random

# first we will assign random number for the computer 
computer_guess = random.randint(1, 15)

print("Let's play Guessing game ! What's your name ? ")
user_name = input()

# now we will ask the user to guess the number 
user_guess = int(input("Hi " + user_name + ", enter a number from 1 to 15 :"))

# start the loop until user guess the right number 
while user_guess != computer_guess:
  if user_guess > computer_guess:
    print("Too high!")
    print("Enter number again: ")
    user_guess = int(input())
  elif user_guess < computer_guess:
    print("Too low!")
    user_guess = int(input("Enter number again: "))

print("congratulations , you guessed it right!!")

