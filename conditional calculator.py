"""
Filename: conditional_calculator.py
Author: <Francisco, Audrey>
Created: <09/25/2026>
Instuctor: Burgess
"""
print("Welcome to the Four-Function Calculator!")
print("This program will take two whole numbers and calculate one of the four basic arithmetic operations,\n"
      "addition, subtraction, multiplication, OR division.")
w1=input("Enter your first whole number, like 4 or 8, not 4.2 or 8.7. ")
num1=int(w1)
print("Please enter your desired operation.")
print("For addition please input: +")
print("For subtraction please input: -")
print("For multiplication please input: *")
print("For division please input: /")
operator = input()
w2=input("Enter your second whole number, like 4 or 8, not 4.2 or 8.7. ")
num2=int(w2)
if operator == "+":
    print("Addition:")
    print(num1, "+", num2, "=", num1 + num2)

elif operator == "-":
    print("Subtraction:")
    print(num1, "-", num2, "=", num1 - num2)

elif operator == "*":
    print("Multiplication:")
    print(num1, "*", num2, "=", num1 * num2)

elif operator == "/":
    print("Division:")
    print(num1, "/", num2, "=", num1 / num2)
else:
    print(f"\n{operator} is not a supported operation. Please try again.")
print("\nThank you for using this program, Goodbye!")