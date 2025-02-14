# ------------------- Tuples -------------------
#Using python to manipulate tuples

'''
similar to struct in c++ but not the same

Python knows a number of compound data types,
used to group together other values.
They are:
tuple
dictionary
set
list

Tuples are written as a list of comma-separated
values (items) between parentheses.


Tuples are immutable - this means that items can not be changed. However,
a tuple can contain mutable objects.

Tuple has 2 methods available.
count()	Returns the number of elements with the specified value
index() Returns the index of the first element with the specified value
'''

#the basic
t = 1,2,'menna'
print(t[0])
print(t)
print(len(t))

u=t,(1,2,3,4),5,23
print(u)
print(u[0])
print(u[1])
print(u[3])
print(u[0][1]) #print the second element in first group in u

#Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
 0   1   2   3   4   5   6   7   8   
-9  -8  -7  -6  -5  -4  -3  -2  -1
'''

print(u[-4])

#trailing comma
empty = () #Empty tuple
singleton = 'hello', #i put one element in tuple singleton
print(len(empty)) #0
print(len(singleton))#1
print(singleton)


#Unpacking a tuple
x, y, z = t #as t has 3 eleement so we can put every elemnt in other variable
xx=t
print(x)
print(y)
print(z)
print(xx)

#built-in function tuple()
x = tuple(['bobby', 'at', 'didcoding','dot', 'com']) # creates a tuple object
print(x)

#Tuple comprehension...Just use list comprehension with the tuple function
x= tuple([x**2 for x in range(10)])
print(x)


