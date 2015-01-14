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
	'black russian': {'vodka', 'kahlua'},
	'white russian': {'cream', 'kahlua', 'vodka'},
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