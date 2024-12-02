""" 
Task 4:

Type the program that prints the two numbers that the user has entered minimum“. """

print("give me an number")
input1 = input()
print("give me an second number")
input2 = input()

if(input1 < input2):
    print(input1)

elif(input1 > input2):
    print(input2)
else:
    print("its egual")
