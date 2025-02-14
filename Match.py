# --------------------- Match Statement ---------------------
'''
A match statement takes an expression and compares its value to
successive patterns given as one or more case blocks.

Note: We have a class in this demo. Don't get too caught up in how it
works! We have a class video in this course :)
'''
#The basics
def Fun(x):
    match x:
        case 'A':
            return 'Excellent'
        case 'B':
            return 'Very Good'
        case 'C':
            return 'Good'
        case 'D':
            return 'Pass'
        case 'F':
            return 'Fail'

print(Fun('A'))
print(Fun('B'))
print(Fun('C'))

def Fun1(x):
    match x:
        case 1 | 2 | 3 | 4 | 5 :
            return 'less than or equal 5'
        case 6 | 7 | 8 | 9 | 10:
            return 'greater than or equal 5'
        case _:# Default case
            return 'greater than 10'
print(Fun1(1))
print(Fun1(111))

#Patterns can look like unpacking assignments, and can be used to bind variables:
# point is an (x, y) tuple

def Fun3(x):
    match x:
        case(0,0):
            print('Origin')
        case (0,y):
            print(f'Y={y}')
        case (x,0):
            print(f'X={x}')
        case (x,y):
            print(f'X={x}, Y={y}')
        case _:#if x not tuple with exactly 2 values it will raise ann error
            raise ValueError('Not a point')

x=0,0
Fun3(x)
x=1,1
Fun3(x)
x=2,0
Fun3(x)
x=0,4
Fun3(x)

#Match class
from dataclasses import dataclass
@dataclass
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

where_is(Point(0, 0))
where_is(Point(0, 10))
where_is(Point(10, 0))
where_is(Point(10, 10))


