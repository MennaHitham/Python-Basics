# --------------------- IF ---------------------
'''
Python uses the usual flow control statements known
from other languages, with some twists.
Perhaps the most well-known statement type is the
if statement.


Think of an if statement as a way to check to see if
conditions are met!

If a condition is met, do something...
else do something different!

'elif' stands for 'else if'

both elif and else are optional!

Note: I will be defining a function to demo :)
'''

def num_play(x):
    if x<0:
        print('Negative')
    elif x==0:
        print('Zero')
    elif x>0 and x&1:
        print('Positive Odd')
    else:
        print('Positive Even')


num_play(2)
num_play(3)
num_play(-1)
num_play(0)



