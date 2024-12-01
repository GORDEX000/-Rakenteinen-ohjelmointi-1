import math


print("Choose one:\n1. sum between 2 numbers\n2. difference between 2 numbers\n3. multiplication between 2 numbers\n4. division between 2 numbers\n5. between at least 2 numbers\n6. between no more than 2 numbers\n7. 1st degree equation\n8. 2nd degree equation\n")
userChoice = input()

if(userChoice == "1"):
    firstNum = int(input("Give me the first Number: "))
    secondNum = int(input("Give me the first Number: "))
    print("The result is: ",firstNum + secondNum)
elif(userChoice == "2"):
    firstNum = int(input("Give me the first Number: "))
    secondNum = int(input("Give me the first Number: "))
    print("The result is: ",firstNum - secondNum)
elif(userChoice == "3"):
    firstNum = int(input("Give me the first Number: "))
    secondNum = int(input("Give me the first Number: "))
    print("The result is: ",firstNum * secondNum)
elif(userChoice == "4"):
    firstNum = int(input("Give me the first Number: "))
    secondNum = int(input("Give me the first Number: "))
    print("The result is: ",firstNum / secondNum)
elif(userChoice == "5"):
    firstNum = int(input("Give me the first Number: "))
    secondNum = int(input("Give me the first Number: "))
    if(firstNum < secondNum):
        print(firstNum)
    else:
        print(secondNum)
    print("The result is: ",firstNum - secondNum)
elif(userChoice == "6"):
    firstNum = int(input("Give me the first Number: "))
    secondNum = int(input("Give me the first Number: "))
    if(firstNum > secondNum):
        print(secondNum)
    else:
        print(firstNum)
    print("The result is: ",firstNum - secondNum)
elif(userChoice == "7"):
    firstNum = int(input("Give me the first Number: "))

    secondNum = int(input("Give me the first Number: "))
    
    ab = -int(secondNum) / int(firstNum)
    print("The result is: ", ab)
elif(userChoice == "8"):
    a = float(input("give me first: "))

    b = float(input("give me second: "))

    c = float(input("give me therd: "))

    d = b * b - 4 * a * c

    if(d < 0):
        print("has no result: ")
    elif(d == 0):
        print("has 1 solution which is: ", -b / 2 * a)
    else:
        firstX = (-b + math.sqrt(d)) / 2 * a
        secX = (-b - math.sqrt(d)) / 2 * a
        print("has 2 solutions which are: ",firstX, "and", secX)

        firstEc = a * firstX * firstX + b * firstX + c

        print("The calculated equation with first x: ", firstEc)
        print("The calculated equation with second x: ", a * secX * secX + b * secX + c)
else:
    print("invalide Choise: ")