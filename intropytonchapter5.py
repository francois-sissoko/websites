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