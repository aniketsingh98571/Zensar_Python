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