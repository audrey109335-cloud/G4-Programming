"""
Francisco_Audrey
MP1_Exam
"""

F = int(input("Enter the temperature in Fahrenheit: "))
c=(F-32)*5/9
print(c)
if c<=0:
    print("Freezing Alert!")
elif c>=35:
    print("Heat Warning!")
else:
    print("Normal Temperature")
