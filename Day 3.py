# draw such pictures with the help of ASCII art 
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('You are at a cross road. Where do you want to go? Type "left" or "right"?\n')
print("\n")
if (choice1.lower() == "left") :
  choice2 = input('You arrived at a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across.\n')
  print("\n")
  if(choice2.lower() == "wait") : 
    choice3 = input("You arrived at the island unharmed. In the middle of the island, there is a house with three doors. One red, one yellow and one blue. Which one do you choose?\n")
    print("\n")
    if (choice3.lower() == "red") :
      print("You were burnt to death by fire. Game over!")
    elif (choice3.lower() == "blue") :
      print("You were eaten by a giant beast. Game over!")
    elif(choice3.lower() == "yellow") :
      print("Congratulations! You found the treasure. You're gonna be rich for the next of your life.")
    else :
      print("No-one likes a smart-ass. Game over.")
  else :
    print("You were attacked by a hover of trouts. Game over!")
else : 
  print("You fell into a pothole. Game over!")
