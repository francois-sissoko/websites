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

