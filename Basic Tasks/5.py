"""
Task 5:

Type the program that will print maximised between the two figures provided by the user. """

print("give me an number")
input1 = input()
print("give me an second number")
input2 = input()

if(input1 < input2):
    print(input2)
elif(input1 > input2):
    print(input1)
else: print("egual")