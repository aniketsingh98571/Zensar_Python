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

'''
split function
'''
str="Welcome to Python"
print("The original string is:",str)
str2=str.split()
print("The modified string is", str2)#it splits the string into comma separated list(of words)
print("-----------")

str="D.Y.Patil College"
print("The string is:",str)
num=str.split()
print("The modified string is :",num)

str="Python is a programming language"
str2=str.split()
print("The string is :",str)
print("The modified string is ",str2)
print("-----------------------------")
str3=str.split("is")
print(str3)

str4=str.split(' ')
print(str4)

str5=str.split('a')
print(str5)

str6=str.split('g')
print(str6)

'''
replace() method replaces all the occurrences of the substring with the given  substring
'''

str="Python is a programming language"
print("The original string is: ",str)
str2=str.replace("Python","java") #replace(old,new)
print("The modified string is ",str2)
str2=str.replace("g","$$",3) #replace(old,new,no of occurrences)
str2=str.replace(str,"Welcome to Python")
print(str2)

#isdigit() ---If string contains numbers then it will give true and if it contain numbers with special character like "-" it will give false
str='98765'
print("The string is ",str)
str2=str.isdigit()
print(str2)

str="980-25-65"
print(str.isdigit())

str="!@#12234t8&^%"
if str.isdigit()==True:
    print("It is digit")
else:
    print("It is not digit")

#strip() function
str="    Hello   World    "
print("The modified string is ",str.strip())#removes all blank spaces from starting and end of the string
print("------------------")

print("The modifiend string is", str.rstrip())#remove all blank spaces from right of the string
print("------------------")

print("the modified string is",str.lstrip())#remove all blank spaces from left of the string

#wap to replace all blank spaces with ','
#wap to count all the occurrences of 'a' in a string
#wap to remove a char from the string
#






#Lists-Heterogeneous collection of elements enclosed within a pair of square brackets separated by comma.Mutable objec
#Index is availablle to traverse the list. slicing can also be done

list1=[1,2,3,5,25] #list of numbers
print("The list we have is ",list1)

print("The element of the list is ",list1[0])
print("The element of the list is ",list1[1])
print("The element of the list is ",list1[2])
print("The element of the list is ",list1[3])

print("The variable type is ",type(list1))
list2=["Nashik","khalapur","jamshedpur","kolkata"]#list of strings
print("THe list 2 is ",list2)
print("The type of variable is",type(list2))
print("The element of the list is ",list2[0])
print("The element of the list is ",list2[1])
print("The element of the list is ",list2[2])
print("The element of the list is ",list2[3])

list3=[1,2,3,"Aniket","kolkata"]
print("THe list 3 is ",list3)
print("The type of variable is",type(list3))
print("The element of the list is ",list3[0])
print("The element of the list is ",list3[1])
print("The element of the list is ",list3[2])
print("The element of the list is ",list3[3])

#updating list
list4=["Punjab","Gujrat","Kashmir","Delhi"]
print("the original list is",list4)
print("trying to update the list")
list4[1]="Jamanagar"
print("The modifed list is",list4)

list4=["Punjab","Gujrat","Kashmir","Delhi"]
print("the original list is",list4)
print("trying to update the list")
list4[0]="Java"
print("The modifed list is",list4)

#creating a list
print("creating the list using for loop")

#generating the list using for loop
number=[x+6 for x in [1,2,3,4,5]]
print("The list is ",number)
#[1+6,2+6,3+6,4+6,5+6]

#creating a list using for loop and range function
number=[x+6 for x in range(2,12)]
print("the list is",number)

#converting a string into list
print("Converting a string into list")
str=list("python")
print(str)

city="Nashik Pune"
print("the string is ",city)
city1=list(city)
print(city)
print(list(city))

print("Searching the elements using for loop in list")
list6=[1,2,3,4,"Aniket","Singh","Web Dev"]
for elements in list6:
    print(elements)
    if "Aniket" in list6:
        print("Found")
    else:
        print("not found")

if "Tech" in list6:
    print("Yes")
else:
    print("No")

#adding elements to the list using append function
list7=[11,12,5,6]
print("The original list is ",list7)
list7.append(23)
print("The modified list is ",list7)

list8=["Aniket","Web Dev","Frontend"]
print("The original list is ",list8)
list8.append("open source")
print("The modified list is ",list8)

list9=[1,2,3,"Web Dev","Front dev"]
print("The original list is ",list9)
list9.append(23)
print("The modified list is ",list9)

#adding the element to a particualar position
print("Adding the element at index position using insert() function")
list10=[1,2,3,4,5]
print("Original list ",list10)
list10.insert(3,30)
print("Modified list ",list10)

#Removing the element using del
list10=[1,2,3,4,5]
print("Original list ",list10)
del list10[1]
print("modified list is ",list10)

#deleting list
del list10

#remove()
list10=[1,2,3,4,5]
print("Original list ",list10)
list10.remove(2) #specify the element you want to delete
print("modified list is ",list10)



