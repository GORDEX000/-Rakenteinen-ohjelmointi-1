lst = []

i = 0


userInput = int(input("Give some random number: "))

def first(userInput):
    while(i < userInput):
        ipt = int(input())
        if(ipt > 0):
            lst.append(ipt)

    print(lst)

def second(userInput):
    for i in range(0, userInput):
        ipt = int(input())
        if(ipt > 0):
            lst.append(ipt)

    print(lst)

    lst = []


if()