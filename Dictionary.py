# -------------------------Dictionaries-------------------------
'''
Like map in c++

Dictionaries are used to store data values in key:value pairs.

some_dict = {
    'a_key': 'a_value',
    'a_key_2': 'a_value_2',
    'a_key_3': ['a_list', 'as', 'a value'],
    'a_key_4': {'a_dict': 'as a value'}
}

Dictionaries are mutable - this means that item values can be changed

Dictionaries have a bunch of methods available.
clear() Removes all the elements from the dictionary
copy() Returns a copy of the dictionary
fromkeys() Returns a dictionary with the specified keys and value
get() Returns the value of the specified key
items() Returns a list containing a tuple for each key value pair
keys() Returns a list containing the dictionary's keys
pop() Removes the element with the specified key
popitem() Removes the last inserted key-value pair
setdefault() Returns the value of the specified key. If the key does not exist:
insert the key, with the specified value
update() Updates the dictionary with the specified key-value pairs
values() Returns a list of all the values in the dictionary
'''

dics ={ 'm':1, 'e':2 , 'n' :3 , 'n':4 , 'a':6 , 9:8}#i give for every key a value
#but when i give n =3 then n=4 , so it override on value 3 and put 4
print(dics)
print(dics['m'])#print value of key 'm'
#print(dics['b']) #error cause there is no key called 'b

#I can give for one key a lot of values :
dics1 = {
    'menna' : [1,2.22,3],
    'hitham' : [4,5,6]
}
print(dics1['hitham']) # [4,5,6]
print(dics1['hitham'][0]) #4

#Create a copy
dics_copy=dics.copy()
print(dics_copy)

#Altering a dict
dics1['hitham']=55 #change value of hitham from [4,5,6] to 55
print(dics1)
print(dics1['hitham'])

#Lenght
print(len(dics1)) #2

#show all keys and values
print(dics1.keys())
print(dics1.values())

#Dics comprehension
x={x : x**2 for x in (2,3,5)} #i store for every 2,3,5 s a key , value that is x**2
print(x)

#builtin function dict()
x=dict(a=1,b=2,c=3)
print(x)

