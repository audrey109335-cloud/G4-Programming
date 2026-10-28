"""
Filename: <>
Author: <Francisco, Audrey>
Created: <10/22/2026>
Instructor: Burgess
"""
print("Welcome to the average calculator!")
print("You will be asked repeatedly to input numbers.")
print("After each number, your sum, the amount of numbers you've entered,")
print("and the average will be displayed.")
print("The program will then ask if you would like to enter more numbers.")

total_sum = 0
count = 0
user_choice = "y"
while user_choice == "y":
    number = float(input("Enter a number: "))
    total_sum = total_sum + number
    count = count + 1
    average = total_sum / count

    print(f"Your current sum is {total_sum}.")
    print(f"Your current number entries is {count}.")
    print(f"Your current average is {average}.")