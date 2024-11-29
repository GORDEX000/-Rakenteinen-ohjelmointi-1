import operations
print("Hello!")
userChoise = input("Choose one:\n1. sum between 2 numbers\n2. difference between 2 numbers\n3. multiplication between 2 numbers\n4. division between 2 numbers\n5. between at least 2 numbers\n6. between no more than 2 numbers\n7. 1st degree equation\n8. 2nd degree equation\n")

if (userChoise == "1"):
    operations.sum()
elif (userChoise == "2"):
    operations.minus()
elif (userChoise == "3"):
    operations.multi()
elif (userChoise == "4"):
    operations.division()
elif (userChoise == "7"):
    operations.firstDegreeEguation()
elif (userChoise == "8"):
    operations.secondDegreeEguation()
