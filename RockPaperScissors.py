rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player = input("Type: rock, paper, or scissors? ")

print("\nYou pick") 

if player == "rock":
  num = 1
  print(rock)
elif player == "paper": 
  num = 2 
  print(paper)

elif player == "scissors": 
  num = 3
  print(scissors) 

print("Computer picks")

compNum = random.randint(1,3)

if compNum == 1:
  print(rock) 

elif compNum == 2:
  print(paper)

elif compNum == 3:
  print(scissors)


if num == compNum:
  print("Tie") 

elif num == 1 and compNum == 2:
  print("Computer wins!")

elif num == 1 and compNum == 3:
  print("Player wins!")

elif num == 2 and compNum == 1:
  print("Player wins!")

elif num == 2 and compNum == 3:
  print("Computer wins!")

elif num == 3 and compNum == 1:
  print("Player wins!")

elif num == 3 and compNum == 2:
  print("Player wins!")


 


