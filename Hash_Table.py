'''
Definition:
A hash table is a data structure that organizes data using keys and values. For example, "lasagna" is a key, and its price is the value. Many programming languages have built-in hash tables, like Python's dictionaries.
Structure:
A hash table is like a row of storage boxes (called slots or buckets). When a hash table is created, all the slots are empty.
Hash Functions:
A hash function is a process that takes a key (like "lasagna") and determines which slot it should go into.
A hash function must always return the same slot for the same key.
Lookups:
To find a value, we hash the key to find out where it is stored.
Once we know the slot, we look inside and retrieve the value. This is very fast, taking constant time (O(1)).
Collisions:
Sometimes, different keys might get mapped to the same slot, causing a collision. For example, if "moussaka" is also mapped to slot 1, we have a problem. There are ways to fix this, but Python handles it for us.
'''

'''
Python Dictionary:
In Python, hash tables are called dictionaries. An empty dictionary is written as {}. We can add items, where the keys are dish names and the values are prices.
'''
#Example:
dic ={'menna':1 ,'noor':2}

'''
Python Dictionary - Get
To get a value, we use square brackets ([]) with the key. If the key doesn’t exist, Python gives an error. Instead, we can use .get(), which returns None if the key isn’t found.
'''
#Example:
print(dic.get('noor'))

'''
Python Dictionary - Items, Keys & Values
.items() gives all key-value pairs.
.keys() gives only the keys.
.values() gives only the values.
'''
#Example:
print(dic.items())
print(dic.keys())
print(dic.values())

'''
Python Dictionary - Insert
To add a new item, we assign a value to a new key
'''
dic['kareem']=3

'''
Python Dictionary - Modify
To change an existing value
'''
dic['menna']=10

'''
Python Dictionary - Remove
del menu["lasagna"] removes a key-value pair.
menu.clear() removes everything.
del menu deletes the dictionary entirely.
'''
del dic['menna']
dic.clear()
del dic

'''
we can iterate over a dictionary using for loop 
'''
dic ={'menna':1 ,'noor':2}
for key,value in dic.items():
    print(key,value)

'''
we can iterate over keys 
'''
for key in dic:
    print(key)

'''
we can iterate over a values
'''
for value in dic.values():
    print(value)


'''
Nested Dictionary 
'''
my_menu ={
    'menna' : { 'name' : 'menna' , 'age' : 20},
    'noor' : { 'name' : 'noor' , 'age' : 30},
}

