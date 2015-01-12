#Python basic list ops 
import sys
py = [
	"At the end of the day",
	"Having said that",
	"The fact of the matter" ]

print(py[1])

#List comprehension shows more than one way to create a list 
#List are good for keeping track of things by their order can
#make a list with [] or the list function 

#list() function converts other data types to list
list('cat')

#converts a tuple to a list
a_tuple = ('ready', 'fire', 'aim')
tempList=list(a_tuple)
print(tempList)

#list can contain list you can mutate them but you can change the list itess 
#inside the list 
#list of list 
small_birds = ['hummingbird','finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian BLue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

print(all_birds[1])
print(all_birds[1][0])