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