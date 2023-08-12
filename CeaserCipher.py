alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

#function to determine if we are encoding or decoding the message
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if shift_amount > 26 and shift_amount % 26 != 0:
    shift_amount = shift_amount % 26    
  if cipher_direction == "decode":
    #adjust shift amount back based on the shift number
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]   
    else:
      end_text += char   
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#determines if the user would like to play again
def playAgain(): 
  again = input("Play again? ").lower()
  if again == "yes" or again == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    playAgain()
  elif again == "no" or again == "n":
    print("Game over")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#calling the functions 
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
playAgain()