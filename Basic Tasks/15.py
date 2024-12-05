lst = []


userInput = int(input("Give some random number: "))

i = 0

while(i < userInput):
    ipt = int(input())
    if(ipt > 0):
        lst.append(ipt)
    i += 1
print(lst)

"""
for i in range(0, userInput):
    ipt = int(input())
    if(ipt > 0):
        lst.append(ipt)

print(lst)
"""