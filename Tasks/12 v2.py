import random

# 1. Rock
# 2. Paper
# 3. Scissors

list = ["Rock", "Paper", "Scissors"]


computer_Choise = random.choice(list)

userChoise = input("1. Rock\n2. Paper\n3. Scissors")

if (userChoise == computer_Choise):
    print("U choose: ", userChoise, "Computer Choose: ", computer_Choise)
    print("tie")
elif(userChoise == 1 and computer_Choise == 3 or userChoise == 2 and computer_Choise == 1 or userChoise == 3 and computer_Choise == 2):
    print("U choose: ", userChoise, "Computer Choose: ", computer_Choise)
    print("u won")
elif(computer_Choise == 1 and userChoise == 3 or computer_Choise == 2 and userChoise == 1 or computer_Choise == 3 and userChoise == 2):
    print("U choose: ", userChoise, "Computer Choose: ", computer_Choise)
    print("u lost")