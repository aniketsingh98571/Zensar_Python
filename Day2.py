#if statement
'''
THe if-else statement provides an else block combined
with the if statement which is executed in the false
case of condition.
if the condition is true then if block is executed
otherwise else block is executed.

input function is used to take input from
user. By default it takes string as input even if we
are entering numbers
'''
from typing import type_check_only
from Zensar_Python.Day1 import String_1


print("Program to find the largest of three numbers")
a = int(input("Enter a? "))
b = int(input("Enter b? "))
c = int(input("Enter c? "))

if a>b and a>c:
    print("a is largest")
if b>a and b>c:
    print("b is largest")
if c>a and c>b:
    print("c is largest")

#if-else block
#Even nos identification
p=int(input("Enter any number?"))
if p % 2 == 0:
    print ("The number is even")
else:
    print ("The number is odd")

#elif statement enables us to check multiple condditions
#and execute the specific block of statements depending
#uopn the values
marks=int(input("Enter student grades "))
if marks>85 and marks<=100:
    print("The student belongs to grade A")
elif marks>60 and marks<=85:
    print("The studne belongs to grade B ")
elif marks>40 and marks<=60:
    print("Grade C")
else:
    print("Fail")

#Loops
'''
The flow of the program written in any programmming
language is sequential by default. Sometimes we may
need to alter the flow of the program. The execution
of a specific code may need to be represented 
severa; times.

Advantages of loops
1.It provides code re-usablitity
2.We do not need to write the same code again
and again

For loop
the for loop in python is used to iterate ove 
statements and printing statement multiple times.
'''
string_1="Welcome"
print(string_1)
for i in string_1:
    print(i,end=' ') #end = ' ' is used to avoid the characters pass to new line.

#range function is used to generate the sequence of the
#numbers. if we pass the range(10),it will generate the number from 0 to 9

#syntax of range function
#range(start,stop,step size)
#range function executes stopvalue - 1
#by default step value is 1
for i in range(0,10): #0-->Start value   10--->stop value
    print(i)

for i in range(3,10):
    print(i)

for i in range(3,10,3): #3-->start value  10-->stop value  3-->jump to 3 and then again 3
    print(i)
