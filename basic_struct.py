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

#Math precedence ops 
x = 7
print("x == 5:",x == 5)
print("x == 7:",x == 7)
print("5 < x:",5 < x)
print("x < 10:",x < 10)

#repeat with while 
count = 1 
while count <= 5:
	print(count)
	count+= 1 

#Cancel with break

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