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