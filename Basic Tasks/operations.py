import math

def sum(firstNum, secondNum):
    print("The result is: ", firstNum + secondNum)

def minus(firstNum, secondNum):
    print("The result is: ", firstNum - secondNum)

def multi(firstNum, secondNum):
    print("The result is: ", firstNum * secondNum)

def division(firstNum, secondNum):
    print("The result is: ", firstNum / secondNum)

def minimum(firstNum, secondNum):
    if(firstNum < secondNum):
        print(firstNum)
    else:
        print(secondNum)

def maximum(firstNum, secondNum):
    if(firstNum > secondNum):
        print(secondNum)
    else:
        print(firstNum)

def firstDegreeEguation(firstNum, secondNum):
    ab = -int(secondNum) / int(firstNum)
    print("x = ", ab)

def secondDegreeEguation(a, b, c):
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

def MathematicsStudies(arithmetic, geometry, percentage):

    result = (arithmetic * 5 + geometry * 3 + percentage * 2) / 10

    print("The average point is: ", result)
