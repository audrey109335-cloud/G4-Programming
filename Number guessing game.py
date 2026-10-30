"""
Filename: <>
Author: <Francisco, Audrey>
Created: <10/30/2026>
Instructor: Burgess
"""
import random

print ("Welcome to the Number Guessing Game!")
print("In this game, a specific number will be chosen randomly between 0 and 100.")
print("Your goal is to guess the number")
print("You have many attempts, and once you guess the number, you WIN!!! ")
print("The game will also give you hints by telling you if the number is higher or lower")
print("GOOD LUCK!!!")

x = random.randint(1,100)
attempts = 0

while True:
    try:
        guess = int(input("Enter a number: "))
    except error:
        print("Please enter a NUMBER.")
        continue
attempts =+ 1
if guess < x:
    print("Too low, Try again.")
elif guess > x:
    print("Too high, Try again.")
else:
    print("Congratulations. You guessed the number correct in {attempts} attempts!
break
