# ---------------------- Set ----------------------
'''

A Set is an unordered collection with no duplicate elements. Like a dictionary,
a set is defined by a curly bracket.

Sets are mutable - this means that items can be changed.

Set has a whole bunch of methods available.
add() Adds an element to the set
clear() Removes all the elements from the set
copy() Returns a copy of the set
difference() Returns a set containing the difference between two or more sets
difference_update() Removes the items in this set that are also included in another, specified set
discard() Remove the specified item
intersection() Returns a set, that is the intersection of two or more sets
intersection_update() Removes the items in this set that are not present in other, specified set(s)
isdisjoint() Returns whether two sets have a intersection or not
issubset() Returns whether another set contains this set or not
issuperset() Returns whether this set contains another set or not
pop() Removes an element from the set
remove() Removes the specified element
symmetric_difference() Returns a set with the symmetric differences of two sets
symmetric_difference_update() Inserts the symmetric differences from this set and another
union() Return a set containing the union of sets
update() Update the set with another set, or any other iterable


**Key Takeaways:
-No indexing or direct access in sets.
-Use loops to iterate over elements.
-Use in to check for existence.
-Convert to list if indexing is necessary.
-Use pop() to remove and retrieve an arbitrary element.
'''

#The basic
fruit ={'apple','orange','apple','pear','banana'}
print(fruit)#duplicates have been removed
#print(fruit[0]) #can not access like that

#Fast membership testing
print('orange' in fruit) #check if orange on fruit [True]
print('lemon' in fruit) #check if lemon in fruit [False]

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a) # unique letters in a
print(a - b) # letters in a but not in b
print(a | b) # letters in a or b or both (UNION)
print(a & b) # letters in both a and b (Intersection)
print(a ^ b) # letters in a or b but not both


#Set Comprehension
a={x for x in 'mennahitham' if x not in 'merna'}#will store all chars in mennahitham that not in merna but no duplicates
print(a)#hit

#buiilt in function in set
x=set((1,2,3,4,5,5,3,2)) # creates a set object
print(x)

#Print set using loop
a={1,2,3,4,5,5,3,2}
for x in a:
    print(x)