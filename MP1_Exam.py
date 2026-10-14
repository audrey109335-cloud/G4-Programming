"""
<Francisco,Audrey>
MP1_Exam
"""
ts1=input("What is your test score?: ")
num1=int(ts1)

if (num1>=90 and num1<=100):
    print(f"Your test score is an (A) {ts1}!, Awesome job!")

elif (num1>=80 and num1<=89):
    print(f"Your test score is an (B) {ts1}!, Awesome job!")

elif (num1>=70 and num1<=79):
    print(f"Your test score is an (C) {ts1}!, Keep Practicing!")

elif (num1>=60 and num1<=69):
    print(f"Your test score is an (D) {ts1}!, Keep Practicing!")

elif num1<0:
    print("Are you for real...")

else:
    print(f"Your test score is an (F) {ts1}!, Keep Practicing!")