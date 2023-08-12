import random
from random import randrange
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#accepting user input to determine the number needed from each list 
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?(0-51) \n")) 
nr_symbols = int(input(f"How many symbols would you like?(0-9) \n"))
nr_numbers = int(input(f"How many numbers would you like?(0-8) \n"))
 
password = ""

#generate a random number for random char selection. 
numb = random.randint(1, 101)

#determines the order in which the selected char in each list is printed. If the random number is < 35, print symbols, numbers, letters.
if numb < 35:
  for char in range(1, nr_symbols + 1):
    i = random.randrange(10)
    password += str(symbols[i])

  for char in range(1, nr_numbers + 1):
    i = random.randrange(10)
    password += str(numbers[i])

  for char in range(1, nr_letters + 1):
    i = random.randrange(26)
    password += str(letters[i])
    
elif numb > 50:
  for char in range(1, nr_numbers + 1):
    i = random.randrange(10)
    password += str(numbers[i])

  for char in range(1, nr_letters + 1):
    i = random.randrange(26)
    password += str(letters[i])

  for char in range(1, nr_symbols + 1):
    i = random.randrange(9)
    password += str(symbols[i])

else: 
  for char in range(1, nr_letters + 1):
    i = random.randrange(26)
    password += str(letters[i])
    
  for char in range(1, nr_symbols + 1):
    i = random.randrange(10)
    password += str(symbols[i])

  for char in range(1, nr_numbers + 1):
    i = random.randrange(10)
    password += str(numbers[i])
    
print(password)