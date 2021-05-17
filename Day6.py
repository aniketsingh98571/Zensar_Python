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