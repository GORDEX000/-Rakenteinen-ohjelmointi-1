import operations
print("Hello!")
userChoise = input("Choose one:\n1. sum between 2 numbers\n2. difference between 2 numbers\n3. multiplication between 2 numbers\n4. division between 2 numbers\n5. minimum between 2 numbers\n6. maximum between 2 numbers\n7. 1st degree equation\n8. 2nd degree equation\n9. for Mathematics studies calculation for avg\n")


firstNum = int(input("Give me a Number:"))
secondNum = int(input("Give me a second Number:"))
if (userChoise == "1"):
    operations.sum(firstNum, secondNum)
elif (userChoise == "2"):
    operations.minus(firstNum, secondNum)
elif (userChoise == "3"):
    operations.multi(firstNum, secondNum)
elif (userChoise == "4"):
    operations.division(firstNum, secondNum)
elif (userChoise == "5"):
    operations.minimum(firstNum, secondNum)
elif (userChoise == "6"):
    operations.minimum(firstNum, secondNum)
elif (userChoise == "7"):
    operations.firstDegreeEguation(firstNum, secondNum)
elif (userChoise == "8"):
    thirdNum = int(input("Give me a third Number:"))
    operations.secondDegreeEguation(firstNum, secondNum, thirdNum)
elif(userChoise == "9"):
    thirdNum = int(input("Give me a third Number:"))
    operations.MathematicsStudies(firstNum, secondNum, thirdNum)