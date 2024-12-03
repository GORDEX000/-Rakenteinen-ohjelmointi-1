lst = []


userInput = int(input("Give some random number: "))

"""
while(i < userInput):
    ipt = int(input())
    if(ipt > 0):
        lst.append(ipt)

print(lst)
"""

for i in range(0, userInput):
    ipt = int(input())
    if(ipt > 0):
        lst.append(ipt)

print(lst)
