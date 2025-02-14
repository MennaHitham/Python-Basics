# ************* Numbers *************
x = 5.666675678
y=round(x,2) #it will print x with just 2 decimal numbers
print(y)
z = 4_000_000 #python can handle large number and represent it like that
print(z)

#basics
print(2+2)
print(5-3)
print(7*10)

#Division and Modulus
print(10/4) # classic division returns a float
print(10//4) #floor division discards the fractional part
print(10%4) # % operator returns the remainder of the division
a = divmod(10,3) #return number of b in a , the mod of a/b
print(a)

#Fancy Sums
print(50 - 5*6) #will multiply first then minus
print((50 - 5*6) / 4 ) # will operate what is inside brackets( * then -) then operate outside brackets( / )
print( 5 * 3 + 2 ) #floored quotient * divisor + remainder

#Exponentiantion ( power of)
print( 5 ** 2 ) # 5*5
print( pow(2,4) ) # 2 to the power of 4

#Using variables
width = 60
height = 40
print(width * height)
