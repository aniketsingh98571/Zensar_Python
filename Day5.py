#functions
'''
1.reuse code
2.length is cut short
3.program logic simple
4.can return value
'''
def my_function(): #function declaration
    #statements
    print("this is the function body")
    #return <expression> #None
    print("we can write code here")
print("the function definition ended")
#function call
print("calling the function")
my_function()
print(my_function) #returns none because we have not returned anything

def my_function1():
    print("this is function body")
    print("we can write here code")
    print("the function can be executed multiple times")
    return 1
my_function1()
print(my_function1) #returns 1 since we have returned 1

#parameters in function
def func(name):
    print("This is a function")
    print("hello",name)
    print("this function has parameters")
print("calling the function")
#calling the function
func("Aniket")

str="python"
print("calling the function ",func(str))
print("function executed successfully")

#default arguments in function
def display(a=12,b="rohit"): #giving function the default values
    print("this is default argument function")
    print("the name of the student is ",a)
    print("the age of the student",b)

print("taking values from user")
#taking value from user
a=str(input("Enter the name "))
b=int(input("Enter the age "))
print("calling the function with arguments")
#printting the details
display(a,b) #calling the function with proper values

print("calling the function with different values")
display(b="anand",a=25) #calling the funtion with values

print("calling the function without values..")
display() #calling the function with default values---this will use default values

print("calling the function with passing only one value")
display(15)#calling the function with one value--here 2nd value will be taken from default one

display(b="Rohan") #default value may be accessed

#defining the function
print("passing objects to the function as argument")
print("passing a list to the function")
def update_list(num):
    print("inside the function")
    print("ist inside the function ",num)
    num.append(200)
    num.append(300)
    print("modified list inside the function",num)

#defining the list
num=[100,300,400,500]
print("the list is ",num)

#calling the function
print("calling the function ")
update_list(num)
print("the list outside function ",num)

#passing the string to a function
print("passing the objects to the functions -strings")
def update_string(str1):
    print("inside the function...")
    print("string in the inside function",str1)
    print("trying to access the string in the function ")
    str1=str1=+"python is cool" #concatenation
    print("printing the string inside function",str1)

print("the program for the string inside function")
string1="python is developer friendly"
print("the string is ",string1)
#calling the function
print("calling the function....")
update_string(string1)
print("outside the function")
print("printing the string outside function",string1)

#required argument
print("required argument function...")
def display(name,age):
    print("Inside the function")
    print("the age is ",age)
    print("the name is ",name)
print("outside the function")
print("passing the strings to function")
#taking the values from the user
name=str(input("Enter the name "))
age=int(input("ENter the age "))
print("the name is ",name)
print("the age is ",age)

#printing the details
print("Calling the functions...")
display(age,name)
print("Calling the function with one argument")
display(name)

#non-default arguments should be written first and then the default ones
#def func(arg1,arg2=12,arg3=123)
print("Demo of functioons in python")
def display(b,a=20):
    print("Inside the function")
    print("the value of a is ",a)
    print("the value of b is ",b)
print("passing the arguments to functions")
#passing the arguments as keywords
a="sachin"
b="rahul"
print("The names are ",a,b)
print("\nCalling the function with keyword arguments")
display(a,b)    # keyword argument

print("\nKeyword arguments are argumens where you write the name of argument with values")
print("In keyword arguments if change the position then also it works")
display(b=25,a="Chahal")    # value of b will be overwritten

print("\nPassing only one value")
display(b,a=35) # keyword argument

#Classes in python
print("let uslearn classes and objects")
print("creating a circle class")
class Circle:
    pass
print("Circle class block finished")
print("creating the object")
#object_name=class_name()
my_circle=Circle()
print("Creating instance varible") #variable for the object
my_circle.radius=5 #instance variable
print("The value of radius is ",my_circle.radius)
print("Area of circle..")
print(2*3.14*my_circle.radius)

#__init__(self) constructor
class Circle:
    def __init__(self): #1
        self.radius=1  #init is nothing but a constructor
        print("The radius is ",self.radius)
print("Creating the object")
my_circle=Circle() #2
print("Object Created")
print("Radius is ",my_circle.radius)
print("Area of circle is ",2*3.14*my_circle.radius)  #3
my_circle.radius=5  #4
print("modified radius is ",my_circle.radius)
print("Area of circle is ",2*3.14*my_circle.radius)

#1 Self is set to the newly created isntance when __init__ is run
#2 we create a circle instance object
#3 radius is already initialized
#4 we overwrite the radius field
#5 radius is an instance variable of Circles instances

#methods in classes
class Circle:
    def __init__(self): #1
        self.radius=1  #init is nothing but a constructor
        print("The radius is ",self.radius)

    def area(self):
         print("Inside the area function...")
         return 2*self.radius*3.14
print("Creating the object")
my_circle=Circle() #2
print("Object Created")
print("Radius is ",my_circle.radius)
print("Area of circle is,",my_circle.area())
print("Area of circle is ",2*3.14*my_circle.radius)  #3
my_circle.radius=5  #4
print("modified radius is ",my_circle.radius)
print("Area of circle is,",my_circle.area())
print("Area of circle is ",2*3.14*my_circle.radius)


#instance and class variable
class Circle:
    def __init__(self): #1
        pi=3.14 #this is class variable
        self.radius=1  #init is nothing but a constructor
        print("The radius is ",self.radius)

    def area(self):
         print("Inside the area function...")
         return 2*self.radius*Circle.pi #class varible uses class name to be accessible
print("Creating the object")
my_circle=Circle() #2
print("Object Created")
my_circle.pi=5 #Instance variable
print("Radius is ",my_circle.radius)
print("THe class variable is ",Circle.pi)
print("The object variable is ",my_circle.pi)
print("Area of circle is,",my_circle.area())
print("Area of circle is ",2*3.14*my_circle.radius)  #3
my_circle.radius=5  #4
print("modified radius is ",my_circle.radius)
print("Area of circle is,",my_circle.area())
print("Area of circle is ",2*3.14*my_circle.radius)
print("Changing the pi value")
Circle.pi-4
print("Modified pi value is ",Circle.pi)

#Parameterized Constructor
print("Trying to understand the parameterized constructor")
print("Creating a class student")
class student:
    def __int__(self,id,name,age): #constructor with arguments
        self.id=id
        self.name=name
        self.age=age

    def display(self):
        print("ID :%d\nName:%s\nAge:%d"%(self.id,self.name,self.age))

print("Class created")
print("Creating the objects")
str1=student(101,"Rohan Mali",18) #passing value for data members
print("Object one is created")
str2=student(102,"Anike",21)
print("Object 2 created")
print("trying to call the functions for obejcts")
print("function call for object 1")
str1.display()
print("function call for object 2")
str2.display()

#file handling