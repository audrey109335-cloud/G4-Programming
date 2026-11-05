"""
Filename: <>
Author: <Francisco, Audrey>
Created: <10/22/2026>
Instructor: Burgess
"""
print("Welcome to the average calculator!\n")
print("You will be asked repeatedly to input numbers.\n")
print("After each number, your sum, the amount of numbers you've entered,")
print("and the average will be displayed.\n")
print("The program will then ask if you would like to enter more numbers.\n")

total_sum = 0
count = 0
user_choice = "yes"
while user_choice == "yes":
    number = float(input("Enter a number: "))
    total_sum = total_sum + number
    count = count + 1
    average = total_sum / count

    print(f"Your current sum is {total_sum}.")
    print(f"Your current number entries is {count}.")
    print(f"Your current average is {average}.\n")
    user_choice=input("Do you want to enter another number?")