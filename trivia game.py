"""
Filename: trivia_game.py
Author: <Francisco, Audrey>
Created: <09/29/2026>
Instructor: Burgess
"""
correct_answers_count = 0
total_score = 0
print("Welcome to the trivia game!")
print("In a sec, you will get a series of questions to answer.")
print("Please answer each question carefully.")
print("Once you've completed the quiz,\n"
      "you'll get your score for the amount of questions you've answered correctly!\n")
a1=input("What keyword is used to execute code only if a logical condition is true?\n")

if a1=="if":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

a2=input("What symbol is used to check if two values are equal in a condition?\n")

if a2=="==":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

a3=input("Python convention is to use how many spaces for indentation?\n")

if a3=="4":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

a4=input("What keyword is used to run a different set of instructions if the condition is false?\n")

if a4=="else":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

a5=input("What symbol means 'not equals' in Python logical conditions?\n")

if a5=="!=":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

a6=input("What keyword is used when a program chooses between more than two branches?\n")

if a6=="elif":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

a7=input("What symbol means 'greater than or equal to' in Python?\n")

if a7==">=":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

a8=input("What is used to define a code's structure and hierarchy in Python?\n")

if a8=="indentation":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

a9=input("What term describes a program choosing between two courses of action using if and else?\n")

if a9=="branching":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

a10=input("What symbol means 'less than or equal to' in Python?\n")

if a10=="-":
      total_score+=1
      correct_answers_count += 1
      print("Correct! You just got 2 points!\n")
else:
      if total_score>0:
            total_score-=1
            print("Incorrect. You just lost 1 point.\n")
      else:
            print("Inccorect. No points deducted because your score is 0\n")

print("Thank you for playing the Trivia Game!")
print(f"You answered {correct_answers_count}/10 questions correctly,")
print(f"and got a score of {total_score}/10!")
print("BYE!!!")




