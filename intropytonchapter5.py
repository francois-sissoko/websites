#A module is just a file of Python code 

#We refer to other modules by using the import 
#statements 

#To allow modules to scale even more you can organize files into hierarchies called packages 
#When you are about to write a module it is wise to check to see if there is a module that 
#already does what you want

#Set setdefault() function is like get() ,  but also assigns an item to the dictionary if the keys
#is missing: 

print("Example showing how to use setdefault function")
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

#if key was not in dictionary, the new value is used:

carbon = periodic_table.setdefault('Carbon',12)
print("/n","Carbon was added to the periodic_table by using setdefault")
print(periodic_table)

#if we try to assign a different defaulot value to an existing key, the original vale is 
#returned and nothing is changed

#defaultdict() is similar, but specifies the default value for any new key up front

from collections import defaultdict 

periodic_table = defaultdict(int)

#Now any missing vaule will be an integer(int) with  the value 0:

periodic_table['Hydrogen'] = 1
periodic_table['Lead']

print(periodic_table)

#The argument to defaultdict() is a function that returns the value to be assigned to a missing key
#So if there is no key that default value return is set by defaultdict()
#In noide() is executed to return a value when needed 

from collections import defaultdict

def no_idea():
	return "huh?"
	
bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'

print("Showing defaultdict behavior")
print("Only A and B keys have been set")
print("Huh! is the missing key reply")

print(bestiary['A'])  
print(bestiary['B']) 
print(bestiary['C']) 

#The stdlib has a counter module that can do
#A lot of cool things like

from collections import Counter
breakfast = ['spam','spam','eggs','spam']
breakfast_counter = Counter(breakfast)
print("Example showing Counter module:")
print("Prints the number of each value in the list")
print(breakfast_counter)
print("Example of the most common function")
print(breakfast_counter.most_common())
print("Most common takes an arg to know how many different elements to return")
print("Only returning the most common")
print(breakfast_counter.most_common(1))
print("You can also do set opertations on Counter")
lunch = ['eggs','eggs','bacon']
lunch_counter = Counter(lunch)
print("Creating and printing a lunch counter for union ops")
print("breakfast_counter:")
print(breakfast_counter)
print("lunch_counter:")
print(lunch_counter)
print("breakfast_counter + lunch_counter") 
print(breakfast_counter + lunch_counter)
print("breakfast_counter - lunch_counter")
print(breakfast_counter - lunch_counter)
print("breakfast_counter & lunch_counter")
print(breakfast_counter & lunch_counter)
print("breakfast_counter | lunch_counter")
print("union picks the item from the list with the highest count") 
print(breakfast_counter | lunch_counter)

#Ordered Dictionary are used when the order or the keys
#is important because a normal dictionary doesn't remember 
#order 

from collections import OrderedDict
quotes = OrderedDict([
	('Moe','A wise guy, huh?'),
	('Larry','Ow!'),
	('Curly','Nyuk nyuk!'),
	])

#it is like a dictionary that takes 2-tuples(immutable)
#instead of a key, value pair 

print("Showing that order Dictionary works")
for stooge in quotes:
	print(stooge)
	
#Stack + Queue = deque(deck) like double end queue 
#popleft removes from the left most and pop removes from the 
#right most 

print("showing the deque, popleft and pop")
def palindrome(word):
	from collections import deque
	dq = deque(word)
	while len(dq) > 1:
		if dq.popleft() != dq.pop():
			return False
	return True
		
print("Creates a function to see if word is palindrome")
print("It does this by popping from the left and right at the same time")
print("Is 'a' palindrome")
print(palindrome('a'))
print("Is 'racecar' palindrome")
print(palindrome('racecar'))
print("Is 'halibut' palindrome")
print(palindrome('halibut'))

#The easiest way to see if palindrome is to check 
#A word against it's reverse
#Python doesn't have a reverse method for strings
#but you can use slice to reverse a word 

print("example of a palindrome using slice")
def another_palindrome(word): 
	return word == word[::-1]
	
print("Is 'radar' a palindrome")
print(another_palindrome('radar'))

#iterate tools is important for iteration 
#the tool returns an item at time when called in 
#for...in loop

print("This is an example of chain:")
print("this prints the args as though the were a single iterable")

import itertools 
for item in itertools.chain([1,2],['a','b']):
	print(item)

i = 0
print("cycle is  an infinite iterator, cycling through arg")
for item in itertools.cycle([1,2]):
	print(item)
	i = item + i
	if i > 20: 
	    break

print("accumulate calculated accumulated values")
print("accumulate by default adds")
print("adding 1,2,3,4 accumulator") 
for item in itertools.accumulate([1,2,3,4]):
	print(item)
	
#Printing Nicely with pprint 
print("You can print more fomated with 'pprint'")
from pprint import pprint
quotes = OrderedDict([
	('Moe', 'A wise guy,  huh?'),
	('Larry', 'Ow!'),
	('Curly','Nyuk nyuk'),
	])
	
print("Normal print:")
print(quotes)
print("pprint:")
pprint(quotes)

