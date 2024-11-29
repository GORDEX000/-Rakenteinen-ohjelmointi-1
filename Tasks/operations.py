import math

def sum():
    firstNum = int(input("Give me a Number:"))
    secondNum = int(input("Give me a second Number:"))
    print("The result is: ", firstNum + secondNum)

def minus():
    firstNum = int(input("Give me a Number:"))
    secondNum = int(input("Give me a second Number:"))
    print("The result is: ", firstNum - secondNum)

def multi():
    firstNum = int(input("Give me a Number:"))
    secondNum = int(input("Give me a second Number:"))
    print("The result is: ", firstNum * secondNum)

def division():
    firstNum = int(input("Give me a Number:"))
    secondNum = int(input("Give me a second Number:"))
    print("The result is: ", firstNum / secondNum)

def firstDegreeEguation():
    firstNum = int(input("Give me a Number:"))
    secondNum = int(input("Give me a second Number:"))
    ab = -int(secondNum) / int(firstNum)
    print("x = ", ab)

def secondDegreeEguation():
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

        print(firstEc < 0, firstEc > -0.000000000000001)