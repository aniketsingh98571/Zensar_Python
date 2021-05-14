#wap to print first three elements of list
list=[1,2,3,4]
print(list[0:3])

#wap to print last 3 elements from list
list=[1,2,3,4]
print(list[-3:])

#wap to print only even position elements from the list -index-0,2,4
list=[1,2,3,4]
print(list[0::2])

#wap to print only odd position from list
list=[1,2,3,4]
print(list[1::2])

#wap to print the list in reverse order
list=[1,2,3,4]
print(list[::-1])

#Tuple -It is a collection of different data elements separated by comma within in round brackets
#it is immutable
print("Demo for tuple")
print("tuples are used to store the data items/elements of any type")
print("tuple are immutable")

tup=(1,2,2,3,4,5)
print("the tuple members are",tup)

tup1=("one","two","three","four")
print("Tthe tuple of string",tup1)

tup2=(1,2,3,"one","two","three")
print("tuple of mixed ",tup2)

print("type of tuple",type(tup2))
print("we can print the tuple using for loop")
for i in tup:
    print(i,end=' ')

print("code to check whether an element is present in tuple or not")
if 1 in tup2:
    print("present")
else:
    print("absent")

if 6 in tup:
    print("present")
else:
    print("absent")

print("trying to delete the elements")
del tup2[2]
print(tup2)#it will give error because we cannot delete items in tuple

#we can delete tuple as a whole
del tup2 #It deletes the whole tuple.

#slice a tuple from 3rd index to last index
tup=(1,2,3,4,5)
print(tup[2:])

#slice a tuple from second last index to first
tup=(1,2,3,4,5)
print(tup[:-1])

#slice a tuple in reverse order
tup=(1,2,3,4,5)
print(tup[::-1])

#slice a tuple printing even elements
tup=(1,2,3,4,5)
print(tup[0::2])

#slice a tuple to print only last element
tup=(1,2,3,4,5)
print(tup[-1])

#slice a tuple to print 2nd last element
tup=(1,2,3,4,5)
print(tup[-2])

#some functions under tuple
#sorted() function used to sort the tuple, ascending by default
tup=(5,6,7,1,3,2,9,12,14,23,12)
print(sorted(tup)) #returns a list of sorted elements

tup2=("nashik","pune","nagpur","kolhapur")
print(sorted(tup2))

#tuple concatenation
tup=("nashik","pune","aurangabad","kolhapur")
tup1=(1,2,3,4)
print("tuple 1 values ",tup)
print("the 2nd tuple is ",tup2)
tup3=tup+tup1
print("concatenated tuple is ",tup3)

#find the index of an element in tuple
tup1=(1,2,3,4)
idx=tup1.index(2)
print("the index of position 2 is ",idx)

#counting no of occurrence of an element
tup=(11,12,13,15,11)
n=tup.count(11)
print("no of occurences of  11 is ",n)

#length of tuple
tup=(1,2,3,4)
length=len(tup)
print("the length of given tuple is ",length)
print("prints the minimum element in tuple ",min(tup))
print(" prints the maximum number of element in tuple ",max(tup))

tup1=("Aniket","ABC","A")
print(min(tup1)) #prints string of minimum length

#sets
'''
1.unordered collection of various items enclosed within curly braces
2.the elemetns of the set cannot be duplicate
3.the elements of the python set must mutable
4.no index attachd to the element of the set
5.directly access any element of the set by ht index.
'''
print("demo for python set")
print("creating the set of days")
days={"monday","tuesday","wednesday","thursday","friday","saturday","sunday"}
print("the original set is ",days)
print("the type of set is ",type(days))
#looping in the set
for i  in days:
    print(i,end=' ')#same memory area is referred

#converting a list into set
print("converting list to set")
list=["ANiket","homosapiens","ottman"]
print("the original element is ",list)
number =set(list)
print("the converted list is ",number)
print("printing the set using for loop ",number)
for i in number:
    print(i,end=' ')

#adding element to the set
number={1,2,3,4,5}
number.add(6)
number.add(7)
print("the modified list is ",number)

#adding multiple elements to set
number={1,2,3,4,5,6}
number.update([6,7,8,9])
print(number)

print("removing the elements using the discard()")
number={1,2,3,4,5}
number.discard(2)
print(number)

print("removing the elements using the remove()")
number={1,2,3,4,5}
number.remove(2)
print(number)

#remove all the elements from set
tup={1,2,3,4}
tup.clear()
print(tup)

day1={"Sunday","monday","tuesday"}
day2={"wednesday","thursday","friday"}
print("The day1 is ",day1)
print("day2 is here",day2)
 #union
print("union of day1 and day2",day1.union(day2))
print("union of day1 and day2",day1|day2) #using pipe symbol

#intersection
day1={"Sunday","monday","tuesday","thursday"}
day2={"wednesday","thursday","friday"}
print("intersection between two sets is ",day1.intersection(day2))
print("intersection between two sets is ",day1&day2)

#Dictionary:collection of different elements in key value pairs enclosed in curly brackets
print("demo for dictionary in python")
d1={'id':101,'name':"rohan",'marks':75,'city':"pune"}
#key:value   key/value number/string
print("the dict  is",d1)
d1={1:"nashik",2:"pune",3:"khalapur"}
print("the dict is :",d1)
d1['Nsk']=103 #adding element d1[key]=value
d1['aug']=104
print(d1[1]) #accessing the element using key
print(d1[3])

d2={} #empty dict
d2[0]=101
d2[1]=102
print("the dict is ",d2)
a=d2.get(1) #using get() to print the element for the key
print("the element is ",a)

#deleting the element from dict.
print("removing the element using pop() from dict")
print("the dict is ",d1)
#d1.pop()  #error-atleast one argument is required
print("the dict is ",d1)
d1.pop(2) #key
print("the dict is ",d1)
d1.pop('Nsk') #removing the element using pop()
print(d1)

#delete a dictionary/clear a dictionary
d1={"nashik":1,"pune":1,"goa":3}
print("the dict is ",d1)
d1.clear() #deleting all the elements from dict
print("after clear function")
print("the dict is ",d1)

#deletes the dictionary completely
d3={"nashik":1,"pune":1,"goa":3}
del d3 #

#iterate a dictionary
d1={1:"nashik",2:"pune",3:"khalapur","nsk":103,"aug":105,"pun":106}
print("printing only the keys from dict")
for x in d1: #printing the key
    print("the key is",x)

print("***********************")
print("printing only the values from dict")
for x in d1: #printing the value
    print("the value is ",d1[x])

print("************************")
print("printing the values from dict")
for x in d1.values(): #printing the values
    print("the value is",x)
print("*************************")
print("printing the keys and values using items form dict")
for x,y in d1.items(): #printing keys and values
    print("the key is ",x,"   the value is ",y)

#length of dictionary
d1={1:"Nashik",2:"Pune"}
print("length is ",len(d1))

#sort the dict
d1={1:"Nashik",2:"Pune"}
print("length is ",sorted(d1))

d1={1:"Nashik",2:"Pune"}
for x,y in d1.items(): #printing keys and values
    if x==1:
        print("it is present")
#converting tuple to dictionary
tup=((1,"one"),(2,"two"),(3,"three"))
print("the tup is ",tup)
print("converting a tuple to dictionary")
print(dict(tup))

#converting list to dictionary
lst=[[1,"one"],[2,"two"]]
print(dict(lst))

#