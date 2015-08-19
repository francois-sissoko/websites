import sys
#max line length is 80 char, continuation character \(backslash) 
alphabet = ''
alphabet += 'abcdefg'
alphabet += 'hijklmnop' 
alphabet += 'qrstuv' 
alphabet += 'wxyz'
print('alphabet with string concat:', alphabet)
#or you can do it in one step, using the continuation character
alphabetContinuation = 'abcdefg' + \
	'hijklmnop' + \
	'qrstuv' + \
	'wxyz'
print('alphabetContinuation:', alphabetContinuation)
#Line continuation is also needed if a Python expression spans multiple lines 
tempNum = 1 + 2 + \
	3
print("tempNum:", tempNum)

#Code structure nested if and else loops 
furry = True
small = True
if furry:
	if small:
		print("It's a cat.")
	else:
		print("It's a bear!")
else: 
	if small:
		print("It's a skunk!")
	else:
		print("It's a human. Or a hairless bear.")
print("\n")

#Math precedence ops 
x = 7
print("x == 5:",x == 5)
print("x == 7:",x == 7)
print("5 < x:",5 < x)
print("x < 10:",x < 10)
print("\n")

#repeat with while 
count = 1 
while count <= 5:
	print(count)
	count+= 1 

#Cancel with break
print("\n")

#If you want to loop until something occurs, but you're 
#not sure when that might happen, you can use an 
#infinite loop with a break statement.

#Example
#This time we'll read a line of input from the 
#keyboard via Python's input() function and then
#print with the first letter capitalize

while True:
	stuff = input("String to capitalize[type q to quit]: ")
	if stuff == "q":
		break
	print(stuff.capitalize())
	
#Skip Ahead with Continue 

#Sometimes you don't want to break out of a loop
#but just want to skip ahead to the new iteration

#Example
#Let's read an integer, print the square if it's
#odd, and skip it if it's even. 
print("squares an odd number only using continue:")
while True:
	value = input("Integer, please [q to quit]: ")
	if value == 'q': 
		break
	number = int(value)
	if number % 2 == 0: #an even number
		continue
	print(number, "squared is", number*number)

#Check break Use with else 

#If the while loop ended normally (no break call),
#control passes to an optional else. Use this when
#you've coded a while loop to check for something
#and breaking as soon as it is found. THe else
#would be run if the while loop completed but the
#object was not found:

#Example
numbers = [1,3,5]
position = 0
while position < len(numbers):
	number = numbers[position]
	if number % 2 == 0:
		print('Found even number',number)
		break
	position += 1
else: #break not called
	print("No even number found")	
print("\n")
	
#Iterate with for

#Python make frequent use of iterators. 
#Make it possible to traverse data structures 
#without knowing how large they are or how they
#are implemented. You can even iterate over data 
#that is created on the fly, allowing processing of
#data streams that would otherwise not fit in 
#memory all at once

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
	print(rabbits[current])
	current += 1
	
#Better pythonic way
for rabbit in rabbits:
	print(rabbit)
	
#String iteration produces a character at a time

word = 'cat'
print("Iterate over string 'cat':")
for letter in word:
	print(letter)
print("\n")
	
#Iterating over a dictionary(or its keys() function)
#returns the keys

accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
'person':'Col. Mustard'}
print("iterate over dictionary returns keys:")
for card in accusation: #for card in accusation.keys():
	print(card)

#To iterate over the values rather than the keys,
#You use the dictionary's values() function

print("iterate over dictionary return values:")
for value in accusation.values():
	print(value)
	
#To return both the key and value in a tuple, tou can 
#use the items() function

print("iterate over dictionary returns key and value:")
for item in accusation.items():
	print(item)
	
#Remember that you can assign to a tuple in one step.
#For each tuple returned by items(), assign the first
#value(the key) to card and the second (the value)
#to contents

for card, contents in accusation.items():
	print('Card',card, 'has the contents',contents)
	
#Check break Use with else
	
#Similar to while, for has an optional else that 
#checks if the for completed normally. If break was
#not called, the else statement is run
	
#Useful when you want to verify that the previous
#for loop ran to completion, instead of being stopped
#early with a break. 
	
#The for loop in the following
#example prints the name of the cheese 
#and breaks if any cheese is found in the cheese shop
print("\n")

cheeses = []
for cheese in cheeses:
	print('This shop has some lovely',cheese)
	break
else: #no break means no cheese
	print('This is not much of a cheese shop, is it?')
	
#The use of else with for might not seem non-intuitive
#It makes more sense if you think of the for as 
#looking for something and else being called if you 
#didn't find it 

#Same as code above without else
cheeses = []
found_one = False
for cheese in cheeses:
	found_one = True
	print('This shop has some lovely', cheese)
	break
	
if not found_one:
	print('This is not much of a cheese shop, is it?')

#Iterate Multiple Sequence with zip()

#There's one more nice iteration trick: iterating over 
#multiple sequences in parallel by using the zip() function

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange','peach']
drinks = ['coffee','tea','beer']
desserts = ['tiramisu','ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days,fruits,drinks,desserts):
	print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
	
#Zip() stops when the shortest sequence is done. One of the lists
#(dessers) was longer than the others, but no one gets 
#pudding unless we extend the other lists

#Dictionaries" can use dict() function can create dictionaries
#from two-item sequences like tuples, lists, or strings.
#You can use zip() to walk through multiple sequences 
#and make tuples from items at the same offsets.

#Lets make two tuples of corresponding English and French words:

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'

#Now, use zip() to pair these tuples. THe value returned by zip()
#us utself not a tuple or list, but an iterate value 
#that can be turned into one:

#feeding result to list
list(zip(english, french))
#[('Monday', 'Lundi'),('Tuesday, 'Mardi'),('Wednesday','Mercredi')]

#feeding result to dict
dict(zip(english,french))

#Generate Number Sequences with range()

#This lets you create huge range without using all the memory in your computer 
#range(start,stop, step) stop is the only required parameter 

#The following snippet uses a step size of 2 to get the even numbers from 0 to 10
print("prints a list of even numbers from 0-10 using the range function")
print( list( range(0,11,2) ) )
print("\n")

#A comprehension is a compact way of creating a Python data structure from one or more iterators.
#Make is possible to combine loops and conditional test. Pythonic
#List comprehension [ expression for item in iterable if condition ]

#Lets make a new comprehension that builds that builds a list of odd numbers between 1-5
#Remember that number % 2 is true for Odd number and false for even

print( "Odd list of number from 1-5 using list comprehension" )
a_list = [ number for number in range(1,6) if number % 2 ]
print(a_list)

#There can be more than one set of for clauses in the corresponding comprehension. 

#Using a comprehension to make rows and col
print("Using a list comprehension like a nested for loop to create rows and cols")
rows = range(1,4)
cols = range(1,3)
cells = [ (row,col) for row in rows for col in cols]
print( [cell for cell in cells] )
print("\n")

#Dictionary Comprehensions 
#{ key_expression: value_expression for expression in iterable if_condition }

#Dictionary Comprehensions that counts the number of letters in a word 
word = 'letter' 
letter_counts = {letter: word.count(letter) for letter in word }
print("Dictonary Comprehension that shows number of each letters in letter")
print(letter_counts) 
print("\n")
