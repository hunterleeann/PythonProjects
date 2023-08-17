import os

def add(n1, n2):
  """Adds two nums"""
  return n1 + n2

def subtract(n1, n2):
  """subtracts two nums"""
  return n1 - n2

def multiply(n1, n2):
  """multiplies two nums"""
  return n1 * n2

def divide(n1, n2):
  """divides two nums"""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  """Does calculations based on the selected operation""" 

  num1 = float(input("Enter the first number?: "))
  for symbol in operations:
    print(symbol)
  continue_calc = True
 
  while continue_calc:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = round(calculation_function(num1, num2), 4)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      continue_calc = False
      os.system("Clear")
      calculator()

calculator()
