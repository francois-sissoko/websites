#sets examples
import sys 

#A set is like a dictionary with its values thrown away, leaving only the keys
#key must by unique 

#Sets are to prove existence and nothing else 

#Create a set you can use the set() function 
#Or enclose one or more comma-separated values in curly brackets

empty_set = set()
empty_set
# set()
even_numbers = {0,2,4,6,8}
print(even_numbers)
odd_numbers = {1,3,5,7,9}
print(odd_numbers)
#sets are unordered 

#You can create a set from a list, string, tuple, or dictionary, 
#discarding any duplicate values.
print(set('letters'))

#Set of dictionary
test_dict = {'apple':'red','orange':'orange','cherry':'red'}
print(set(test_dict))
#discard values 

# Test for values by using in.

#The most common way to use a set is to test for the existence of values in dictionaries 
drinks = {
	'martini': {'vodka', 'vermouth'},
	'black_russian': {'vodka', 'kahlua'},
	'white_russian': {'cream', 'kahlua', 'vodka'},
	'manhattan' : {'rye', 'vermonth', 'bitters'},
	'screwdriver' : {'orange juice', 'vodka'}
	}
# Even though both are enclosed by curly braces({ and }), a set is just a sequence of
# values and  dictionary is one or more key: value pairs

#which drink contains vodka?
for name, contents in drinks.items():
	if 'vodka' in contents:
		print("Just vodka:", name)

#If we want something with vodka but are lactose intolerant, 
#and think vermouth tastes like kerosene:

for name, interationVar in drinks.items():
	if 'vodka' in interationVar and not ('vermouth' in interationVar or 'cream' in interationVar):
		print("Vodka but no milk or vermonth:", name)
		
#Combinations and Operations
#What if you want to find any drink that has orange juice or vermonth

#Using the set intersection operator, which is an ampersand(&)

for name, loopVar in drinks.items():
	if contents & {'vermouth', 'orange juice'}:
		print(name)

# there is no intersection the returns an empty set, which is considered false 

#Rewrite: If we want something with vodka but are lactose intolerant, 
#and think vermouth tastes like kerosene:

for name, contents in drinks.items():
	if 'vodka' contents and not contents & {'vermonth', 'cream'}:
		print(name)
		
#Saving ingredients for later 
bruss = drinks['black_russian']
wruss = drinks['white_russian']

#Two sets and they have special punctuation 
a = {1, 2}
b = {2, 3}

#You get the intersection members common to both sets with the intersection operation
print("a & b:", a&b)
print("a.intersection(b)", a.intersection(b))
print("bruss & wruss:", bruss & wruss)

#You can get the union by using | or the set union() function
#The two sets become one set the one that is all 
print("a | b:", a | b)
print("a.union(b):", a.union(b))
print("bruss | wruss:", bruss | wruss)

#The difference(members of the first set but not the second)
print("a - b:", a - b) 
print("b - a:", b - a)
print("bruss - wruss:", bruss - wruss)
print("wruss - bruss:", wruss - bruss) 

#The exclusive or(items in one set or the other, but not both
#uses ^ or symmetric_difference(): 
print("a ^ b:", a ^ b)
print("a.symmetric_difference(b):", a.symmetric_difference(b))
#finds the odd one out or the exclusive ingredient in out two russian drinks 
print("bruss ^ wruss:", bruss ^ wruss) 

#You can check whether one is a subset of another
#(all members of the first set are also in the second set)
print("a <= b:", a <= b)
print("a.issubset(b):", a.issubset(b))
# adding cream to a black russian makes a white russian so wruss is a superset of bruss:
print("bruss <= wruss:", bruss <= wruss)
# To be a proper subset, the second set needs to have 
#all the members of the first and more  

# A superset is the opposite of a subset( all members of the second set are also members of the first 

# The only limitations are those in the data types themselves,
#1) dictonary keys need to be immutable, so a list dictonary, or set can't be key for another dictionary 
#2) But a tuple can be.