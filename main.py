print("Hello")
hi = input("Hello! ")
print(hi)

#Okay.. Chatbot project. I need to give the user some stuff to do.abs
# For now, it's probably fine to use print functions and stuff. I don't need a fancy UI

# Welcome the user
print("Welcome to the chatbot!")

Collect the user’s name and age
name = input("What is your name? ")
print(f"Hello, {name}!")
# Ask the user how it can help them
while option != 1 and option != 2 and option != 3:
  option = input("How can I assist you today? (1)Chat, (2)Math, (3) Exit:")  
# Allow the user to choose from a menu/list of options on how they can continue the conversation
if (option==1):
  print("You chose Chat.")
elif (option ==2):
  print("You chose Math.")
elif (option ==3):
  print("You chose Exit.")
  print(f"Goodbye, {name}!")