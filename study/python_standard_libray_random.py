# python standard libray
from random import randint

pc_choice = randint(1, 50)  # import random module
while True:
  user_choice = int(input("Choose number : "))
  if user_choice == pc_choice:
    print("You won! Comuputer Choose", pc_choice)
    break
  elif user_choice > pc_choice:
    print("Lower!")
  elif user_choice < pc_choice:
    print("Higher!")
