#slicing
#First one character
test="Python Programming"
first_character=test[0:1] #0 to 1  characters, 1 is excluded
print(first_character)

#only last character
last_character=test[-1:]
print(last_character)

#Everything except first character
Every=test[1:]
print(Every)

#Everything exept last character
test="Python Programming"
Last_no=test[0:-1]
print(Last_no)

#Everything between first two and lasst two charaacters
test="Python Programming"
between=test[2:-2]
print(between)

#Alternate characters
test="Python Programming"
between=test[0:6:2]
print(between)

#Reverser
test="Python Programming"
between=test[::-1]
print(between)

#wap to print the 10th element of the string
test="Aniket Singh"
print(test[9])

#wap print the substring starting from 9th element
test="Aniket Singh"
print(test[8:])

#print the substring ending at 20th element
test="Aniket Singh working on python programming"
print(test[0:19])

#check if "Pune" is present in given string
test="Pune Nashik Mumbai"
if "Pune" in test:
    print("yes")
else:
    print("no")

#check if delhi not in string
test="Delhi Pune India"
if "Delhi" not in test:
    print("not there")
else:
    print("its there")

#String functions
'''
1.capitalize() function converts first character of the string
into uppercase without affecting remaining characters
'''
str="administrator  hhh"
print("converting the first letter into capital letter")
str2=str.capitalize() #only first character of first string will be in capital
print("Old value", str)#make sure your string doesn't start with blank space
print("new value",str2)

'''
2. casefold() function returns a lowercase copy of the string
'''
print("demo")
str="CASEFOLD  KKK"
str2=str.casefold()
print(str2)

'''
3.  center() function align string to the string by filling
padding
'''
str="DY Patil College"
size=len(str)
print(size)
str2=str.center(25)#printing the string of 25 characters taking the main string in center
#center function add blank spaces by default to the string
print("The original string is: ",str)
print("the modified string :",str2)
size=len(str2)
print(size)

str="Aniket"
str2=str.center(40,'*')
print(str2)

'''
4. count() method returns the number of occurrencces of substring in the
specified range 

Syntax:count(sub[,start[,end]])
'''

str="Hello World"
print("The original string is: ",str)
print("Searching for 'l' in the string")
str2=str.count('l')
print("no of occurences of 'l' are: ",str2)
str2=str.count('ll')
print("no of occurences of 'll' are ",str2)
str2=str.count('o')
print("no of occurences of 'o' are ",str2)

str="this is the turning point 1 2 2 1 3 2 1"
str2=str.count('t',4) #starting from 4th character/index

str3=str.count('2',15,35)#starting from 15th character to 35th character
print(str3)

'''
find() method finds substring in the whole string and
returns index of the first match, it returns -1 is the substring
not matched
'''

str="Hello World"
print("The original string is :",str)
str2=str.find("the")
print(str2) #-1 case

str2=str.find("to")
print(str2) #match case
