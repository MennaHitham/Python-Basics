# ----------------- List -----------------
'''
Python knows a number of compound data types,
used to group together other values. The most
versatile of which is a list.
Others include:
1)tuple
2)dictionary
3)set

-Lists are written as a list of comma-separated
values (items) between square brackets

-Lists are mutable - this means that items can be changed
-List have a bunch of methods available.
append() Adds an element at the end of the list
clear()	Removes all the elements from the list
copy() Returns a copy of the list
count()	Returns the number of elements with the specified value
extend() Add the elements of a list (or any iterable), to the end of the current list
index() Returns the index of the first element with the specified value
insert() Adds an element at the specified position
pop() Removes the element at the specified position
remove() Removes the first item with the specified value
reverse() Reverses the order of the list
sort() Sorts the list
'''

#declaration
v = [1,2,3,4,5]
v

#Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''
print(v)
print(v[0]) # indexing returns the item
print(v[2:]) # slicing returns a new list

#create a list copy
print(v[:])

#Concatenation
print(v + [6,7,8,9,10])

#Alter items
cubes = [1 , 8 , 27 , 65 , 125 ]
cubes[3]=64 #replace 65 with 64
print(cubes)

cubes.append(12)
print(cubes)
print(len(cubes))


#Nesting
list1=['a','b','c','d','e','f','g','h']
list2=[1,2,3]
list3=[list1,list2]
print(list3)
print(list3[0])
print(list3[1])
print(list3[1][0])#print index 0 in the second list in list3


#List Comprehension
y=[]
for x in range(10):
    y.append(x**2)
print(y)
y = [x**2 for x in range(10)] #Faster than using a loop because it avoids repeated .append() calls.
print(y)

#built-in function list()
x = list(('bobby', 'at', 'didcoding','dot', 'com')) # creates a list object
print(x)

#list of characters
letters =['a','a','c','d','a','f','g','h']
letters.pop()
x= letters.copy()
#letters.clear()
#print(letters)
#print(x)
print(letters.count('a'))
letters.extend('b')
print(letters)
letters.remove('a')
print(letters)
letters.sort()
print(letters)


#Test
y=[ x/2 for x in range(10)] # the expression that numbers will be stored in list , for x in range(end of range)
print(y)

