"""
Filename: simple_calculator.py
Author: <Francisco, Audrey>
Created: <03/06/2026>
Instructor: Burgess
"""
import time
from time import sleep

print("Welcome to the Four-Function Calculator!")
print("This program will take two whole numbers and calculate the sum, difference, product, and quotient.")
w1=input("Enter your first whole number, like 4 or 8, not 4.2 or 8.7. ")
num1=int(w1)
w2=input("Enter your second whole number, like 4 or 8, not 4.2 or 8.7. ")
num2=int(w2)
sum=num1+num2
difference=num1-num2
product=num1*num2
quotient=num1/num2
print(w1,"+",w2, "=", sum)
print(w1,"-",w2, "=", difference)
print(w1,"*",w2, "=", product)
print(w1,"/",w2, "=", quotient)
print("Thank you for using this program, Goodbye!")
sleep(5)