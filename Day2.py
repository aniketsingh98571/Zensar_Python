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
