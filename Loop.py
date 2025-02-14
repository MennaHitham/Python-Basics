#-------------------------- Loops --------------------------
'''
Python’s for statement iterates over the items of any sequence
(a list or a string), in the order that they appear in the
sequence.

The built-in Range function 'range()' comes in handy if you do need
to iterate over a sequence of numbers. It generates arithmetic progressions:

range(start, stop, step)
start
The value of the start parameter (or 0 if the parameter was not supplied)
stop
The value of the stop parameter
step
The value of the step parameter (or 1 if the parameter was not supplied)
'''

#The basic
x='menna'
for i in x:
    print(i)

words = ['cat', 'window', 'defenestrate'] #List
for w in words:
    print(w, len(w))


# Create a sample collection
users = {
    'Quinn': 'active',
    'Éléonore': 'inactive',
    'John': 'active'
    }

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]#if stats is inactive ,it deletes it from users


print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

#using the range function
for i in range(5):
    print(i)


#...remember range(start, stop, step)
print(list(range(5, 10)))
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#using the built-in sum function
print(sum(range(4)))#it sums from 0 to 3(stops before 4)



# ------------------------- Loop Clauses ------------------------
'''
Python has a few statements and clauses that we can use in loops. 
These are:
break
continue
else 
pass

Loop statements may have an else clause; it is executed when the 
loop terminates through exhaustion of the iterable (with for) or 
when the condition becomes false (with while), but not when the 
loop is terminated by a break statement. 
'''

#Break statement
for n in range(2, 10): #equivalent of...for n in [2,3,4,5,6,7,8,9]:
    for x in range(2, n): #first loop is for x in range(2, 2):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    #the else runs when no break clause occurs
    else:
        print(n, 'is a prime number')



#Continue statement
for num in range(2, 10): #equivalent of...for n in [2,3,4,5,6,7,8,9]:
    if num % 2 == 0:
        print("Found an even number", num)
        continue #Will continue with the next loop
    print("Found an odd number", num)


#Pass statement
class MyPassClass:
    pass

def my_pass_def(*args):
    pass #Needs looking at

