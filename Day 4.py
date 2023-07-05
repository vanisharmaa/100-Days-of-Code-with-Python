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

images = [rock, paper, scissors] #contains the images of all three

print("Welcome to my edition of Rock, Papers, Scissors.")
user_choice = input("What do you want to choose? Type 0 for Rock, 1 For Paper and 2 for Scissors!\n")

if user_choice == "0" :
  print("You chose Rock.\n" + images[0])
elif user_choice == "1" :
  print("You chose Paper.\n" + images[1])
elif user_choice == "2" :
  print("You chose scissors.\n" + images[2])
else :
  print("Please enter a valid input!")

if (user_choice == "0" or user_choice == "1" or user_choice == "2") :
  computers_choice = random.randint(0, 2);
  if (computers_choice == 0) :
    print("Computer chose Rock.\n" + images[0])
    if (user_choice == "0") :
      print("Match tied!")
    elif (user_choice == "1") :
      print("You Win.")
    else :
      print("You Lose.")
  elif computers_choice == 1 :
    print("Computer chose Paper.\n" + images[1])
    if (user_choice == "0") :
      print("You Lose.")
    elif (user_choice == "1") :
      print("Match tied!")
    else :
      print("You Win.")
  else :
    print("Computer chose Scissors.\n" + images[2])
    if (user_choice == "0") :
      print("You Win.")
    elif (user_choice == "1") :
      print("You Lose.")
    else :
      print("Match tied!")
