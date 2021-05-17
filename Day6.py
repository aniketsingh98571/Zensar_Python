from _typeshed import FileDescriptor
import Modules 
import arithmatic

#there is another way to import specific items/functions from modules
from arithmatic import addition,subtraction,multiply
print("the modules file importing the file")
print("let us print the data from Modules file")
print("Calling the Hello function from Modules module")
Modules.Hello()
print("Modules imported successfully")

#dealing with arithmatic module
arithmatic.addition(2,2)
arithmatic.subtraction(2,2)
arithmatic.multiply(2,2)

#dealing the modules in another way
addition(5,4)
subtraction(5,3)
multiply(3,3)

#exceptions in python
print("Demo for the exceptions")
print("getting two numbers from user and dividing them")
a=int(input("Enter a :"))
b=int(input("Enter value b: "))
print("the value of a is ",a)
print("the value of b is ",b)
print("trying to divide the number ")
c=a/b
print("the result a/b ",c)# if b=0 then divide by zero exceptions

#try-except block

print("Demo for the exceptions")
try:
    print("getting two numbers from user and dividing them")
    a=int(input("Enter a :"))
    b=int(input("Enter value b: "))
    print("the value of a is ",a)
    print("the value of b is ",b)
    print("trying to divide the number ")
    c=a/b
    print("the result a/b ",c)
except:
    print("Inside the except block")
    print("the code did not work properly")
    print("please check the values")
print("this is outside except block")
print("the code ends here")

#exceptions with thier names
print("getting two numbers from user and dividing them")
try:
    print("inside try block.....")
    a=int(input("Enter a "))
    b=int(input("Enter b "))
    print("The values of a is ",a)
    print("the value of b is ",b)
    print("trying to divide the number")
    c=d/b #d is not defined
    print("the result a/b =%d"%c)

except:
    print("Error")

#finally block
print("Demo for finally block")
try: #try-except-finally
    print("Inside 1st try block")
    fileptr=open("Modules.py","r") #write,append,x
    #change the mode to w to chk the proper o/p
    print("the file is opened...")
    try:
        print("Inside 2nd try block ")
        print("trying to write the data in file")
        fileptr.write("hi I am good") #error expected
    finally:
        print("In the inner finally block")
        fileptr.close()
        print("file closed")
except:
    print("in the except block")
    print("error-trying to write in file,opened for read operation")
finally:
    print("final finally block")
print("program ended")

#
try:
    a = int(input("Enter a:"))
    b = (input("Enter b:"))  # taking b value as string
    try:
        c = a/b  # trying to divide a number by string gives error
        print("a/b = %d" % b)
    finally:
        print('This is the finally block...')
    # this finally block executes before except block and after the error is encountered
except ZeroDivisionError:  # not handled NameError hence we get error in o/p
    print("Trying to divide by 0")
except NameError:
    print('Define the variable before use')
except :
    print('Please chk your code')
finally:     # outer try finally block
    print('This is the finally block of outer try')
# if no other named except is called, then all other exceptions are catched here
print("Try block complete")

#raise error
print("Demo for raise keyword")
#raise keyword is used to call an exception
#here we are trying to chk the age and if age is below 18 we find exception
try:
    age=int(input("Enter the age"))
    if age<18:
        raise ValueError
    else:
        print("The age is %a is valid "%age)
except ZeroDivisionError:
    print("THis is divide by zero error")

except NameError:
    print("This is name error")
except ValueError:
    print("THe age is %a is not valid"%age)

print("this is demo for raise keyword")

#User defined exceptions
#Class inheriting exception class
#try raise keyword
#except named exception
class NumbernotProper(Exception):
    def __init__(self):
        print("Inside constructor")
        print("this is user defined error")
print("try block starts here")
try:
    a=int(input("Enter a"))
    b=int(input("Enter b"))
    if b is 0:
        raise NumbernotProper
    else:
        print("THe value of a is ",a)
        print("The value of b  is ",b)
        print("THe result a/b=",a/b)
except NumbernotProper:
    print("The value of b can't be 0")
except ZeroDivisionError:
    print("THis is except block")
except:
    print("This is except block")
print("This is demo for user defined exceptions")

#Installing Libraries
1.Click on Files  
2.Settings
3. project interpreter
4. click on plus
5. install package



