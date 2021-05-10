#print function --->comments
print("Hello")
print(123)
print("World")
#variable
abc=123
print("The value of abc is ",abc)
stringdemo="Hi there"
print(stringdemo)
_variable=456
print(_variable)

#type function--->to get the data type of variable
print(type(abc))
print(type(stringdemo))

a=12.54
print(type(a))

#assigning multiple values to variables at once
z,b,c=12,15,16

#assigning same values to all variables
q=w=e=15

#reusing the variable
g=124
print(g)
g="Aniket"
print(g) #value gets changed

#id() function provides you with the unique id of the variable
#id are nominated for memory location
j=5
print(j)
print(type(j))
print(id(j))
p=j
print(p)
print(type(p))
print(id(p))# it will be same because both the variable p and j  are pointing to same memory location.
p=6
print(p)
print(type(p))
print(id(p))

#datatypes
'''
Numbers--using umeric data-int,float,double
String-seq. of characters
Boolean-true/false
collection in python:-
List
Set
Dictiionary
tuple
'''

#arithmatic operator:- +,-,/,**,//
m=5
n=6
print(m)
print(n)
print("Addition + ",m+n)
print("Substraction - ",m-n)
print("Multiplication * ",m*n)
print(" Division /", m/2)
print("Floor division //", n//2)#quotient
print("Floor division ", m//5)
print(" The exponential ** ", 2**2)
print("Remainder %",n%2)

#Comparison operator(==,!=,<,>,<=,>=)
k=2
l=6
print(k)
print(l)
print(k==l)

print(k!=12)
print("Less than",k<l)
print(" greater than ",k>l)
print(" less than =",k<=l)
print("greater than =",k>=l)

#Shorthand operator
o=5
i=6
o+=i #o=o+i
print("Addition is ",o)

i-=o #i=i-o
print("Substraction ", i)

o*=5 #o=o*5
print("Multiplication ",o)

i/=3 #i=i/3
print(" Division ",i)
#Bitwise operator
#Logical operator
#membership operator-in, not in
#Logical operator- is,is not

#write a program to demonstrate diff data types in python, print variable values 
#with types
integer_1=5
print(integer_1)
print(type(integer_1))

float_1=15.6
print(float_1)
print(type(float_1))

String_1="Aniket"
print(String_1)
print(type(String_1))

Boolean_1=True
print(type(Boolean_1))

#Write a program to demonstrate arithmatic operators
t=5
y=6
print(" Addition",t+y)
print("Substraction ",t-y)
print("Multiplication ",t*y)
print(" Division ",t/y)

#Write a program to demonstrate comparison operator
v=5
r=6
print(" greater",t>y)
print("less ",t<y)
print("Equal" ,t==y)
print(" greater than = ",t>=y)
print("less than =",t<=y)

