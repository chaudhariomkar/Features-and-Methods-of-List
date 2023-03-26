""""""
"""
Features of List
Syntax [ ]
1.List is an important data types in python
2.While giving elements in a list use a comma(,) as a seprator
3.List is mutable data types
    Mutable - Values can be updated 
    Immutable - Values cannot be updated
4.Accepts all types of Data 
    Homogenous - Can only store single type of data 
    Hetrogenous - Can store more than one type of data
5.Background Data Structure of List is - ARRAY
6.Sequence order is preserved
7.Indexing (To Fetch Single Element) is Supported
    Positive Indexing - LEFT to RIGHT
    Negative Indexing - RIGHT to LEFT
8.Slicing (To Fetch Multiple Element or Substring in a sequence) is Supported
9.There are many methods in list like .....
"""
#Create an empty list
a = [] #Method 1
print(a)
b = list() #Method 2
print(b)
x = [1,2,3,4,5] #Elements in a list are seperated by comma's
print(len(x)) #Checks total numbers of elements in a list
#Indexing - to fetch single element
print(x[0])  #(positive - left to right)
print(x[-1]) #(negative - right to left)
#Slicing - to fetch multiple elements
print(x[1:3])
#Replace using indexing
x[0] = 100
print(x)
x[-1] = 500
print(x)
#Replace using Slicing
x[1:4] = [200,300,400]
print(x)
#1.Append - append object to the end of the list
#default takes only one agruements
x.append('Sagar')
print(x)
#but we can add multiple agruemnts using list
x.append([1,2])
print(x)
#2.Extend - adds collection of elements seperately
x.extend([1,2])
print(x)
"""
Q.What is difference between append & extend
Both Append & Extend are used to add elements to a list, but they work differently
Main Difference between append and extend is that
'append' adds a single element to the end of the list
'extend' adds multiple element to the end of the list
Q.What is difference between str & list
A str is a sequence of characters between single or double quotes. A list is a sequence of items, where each item
could be anything (an int,a float,a str)
"""
#3.Insert - Insert object before index
x.insert(1,'Omkar')
print(x)
#4.Clear - it will make the list empty
x.clear()
print(x)
x.clear() #performing clear on empty list
print(x)
#5.pop - remove and return item at index (default last)
y = [100,200,300,400,500]
print(y)
y.pop()
print(y)
y.pop()
print(y)
#if we supply wrong index - (Index error - pop index out of range)
y.pop(1) #by + indexing
print(y)
y.pop(-1) #by - indexing
print(y)
#6.Remove - Removes first occurence of value
z = [100,200,300,400,'Sonal','Ashutosh']
print(z)
z.remove(100) #Remove is value based, takes only one arguement,
print(z)
#If given value is absent - Value Error
#7.Copy - Returns shallow copy of the list
#Shallow Copy - Internal elements of a list are same but ids are different
p = z.copy()
print(p) #Same List
print(id(p))
print(id(z)) #Different ID
#Individual object with different memory location
#Deep Copy - Internal elements of a list are same but ids are also same
r = [1,2,3,4,5]
s = r
print(r)
print(s)  #Same list
print(id(r))
print(id(s))  #Same ids
#Now lets change and check
r[0]=100
print(r)
print(s)
#changes occured in both, because ids are same - deep copy
#8.Index - Returns first Index of value
t = [1,2,3,1,1,1,4]
print(t.index(1)) #first index
#if value is absent - Value Error
#Reverse - Permanently performs changes in the same object
print(t)
print(t[::-1])  #temporary reverse
t.reverse() #permanent reverse
print(t)
#9.Sort - Stable Sort
name = ['Abhishek','Ashutosh','Preetesh','Sandip','Shubham','Sujay','Sagar','Vipul']
name.sort() #Sorts values in Alphabetic Order
print(name)
name.sort(reverse=True) #Sorts in Descending Order Z-A
print(name)
name.sort(key=len) #Sorts values with len
print(name)
name.sort(key=len,reverse=True) #Sorts in Descending Order
print(name)
nm = ['Sonal',30,'Nitin',35,'Shinde'] #Sort not supported between instances of 'int' and 'str'

