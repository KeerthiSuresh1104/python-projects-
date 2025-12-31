print("WELCOME TO TREASURE HUNT ")
print("your session is to find the treasure")
choice_1 = input("you are at a cross road, where you want to go? Type 'left' or 'right'. \n")
if choice_1 == "left":
    choice_2 = input('you got a boat,\n'
                   "there is an island in front of you\n"
                   "type 'wait' to wait for a boat.\n"
                   "type 'swim' to swim onto you\n")
    if choice_2 == "wait":
         choice_3 = input("you got boat and you arrive at the island\n "
                   "there is a house with 3 doors :red, yellow, blue\n"
                   "which will you choice\n")
         if choice_3 == "red":
             print("it is full of fire. game over")
         elif choice_3 == "yellow":
             print("it is full of snakes. game over")
         elif choice_3 == "blue":
             print("YOU WON . you got the treasure")

    else:
         print("you got attacked by crocodile. game over")

else:
    print(" you fell into the hole ,game over! ")






