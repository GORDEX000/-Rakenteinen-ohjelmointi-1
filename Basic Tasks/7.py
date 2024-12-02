""" 
Task 7:

Calculate the solutions to a 2nd degree mathematical equation where the user has entered three known values.

ax 2 + bx + c = 0

https://www.mathsisfun.com/quadratic-equation-solver.html

define three variables named  a ,  b ,  and  c , and set them to the desired values.
define a variable called  d that gets  b 2  - 4ac.
check if  d  is less than 0 then the problem has no real solution.
check if  d  is 0 then the problem has 1 solution which is  -b / 2a .
check if  d  is more than 0, then the problem has 2 solutions which are  fraction numerator negative b plus square root of d over denominator 2 cross times a end fraction and  fraction numerator negative b minus square root of d over denominator 2 cross times a end fraction. See  Math.sqrt(n)  js function that solves  square root of n .
shows  a ,  b ,  c  and the solution in Terminal with beautiful text. """

import math


print("give me first: ")
a = float(input())
print("give me second: ")
b = float(input())
print("give me therd: ")
c = float(input())

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
