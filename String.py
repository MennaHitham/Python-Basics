# ************* String *************
#string can be enclosed in single quotes 'menna' or "menna"
# '\' can be used to escape quotes
#String can not be change like that s[0] = 'c' ,  it is immutable
x= 'menna'
print(x)
x = 'menna\nhitham'
print(x)
print('menna\nhitham') # here \n means newline
print(r'menna\nhitham') # note the r before the quote so will print \n
print('--------------')
x = 'menna\nhitham' # here \n is include output (part of string)
print(x) #because i will print x , it will produce a new line
print('menna\nhitham') # here \n with print() ,\n produces a new line

#string literals
print('''
my name is menna
Python is a programming language.
it is so easy 
''')

#Concatenated
x = 3 * 'un' + 'nnn'
print(x)

x = 'menna'+'hitham'
print(x)


#Indexing
x = 'menna'
#   'm  e  n  n  a'
#    0  1  2  3  4
#   -1 -2 -3 -4 -5
print(x[0]) #m
print(x[-1])#m
print(x[0:2]) #print from index 0 (included) to index 2 (excluded)
print(x[0:]) #print from index 0 # (included) to the end
print(x[:4]) ##print from the beginning to index 4 (excluded)

print(len(x)) # print the length of string


#str , repr ,format FUNCTIONS
x=200
y=400
print(repr((x,y,('spam','eggs'))))
print(str((x,y,('spam','eggs'))))
print("Values are {0} and {1}".format(x, y))
#✔️ repr() is useful for debugging, logging, storing data for reconstruction
#✔️ str() is better for user-facing messages ,	Displaying information to users
#✔️ format()	When you need well-structured text output


