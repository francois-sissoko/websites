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
tempList= list(a_tuple)
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

#get length by using len() 
print("length of all birds:", len(all_birds[1]))
#assign with =, Copy with copy()
a = [1,2,3]
print("a:", a)
b = a
print("b:", b)
a[0] = 'surprise'
print("a modified:", a)
#So what is b modified 
print("b modified:", b)
#a and b now point and pretty much are the same thing 
b[0] = 'I hate suprises'
print("a modified again:", a)
print("b modified again:", b)

#You can copy the values of a list to an independent, 
#fresh list by using any of these methods
a = [1,2.3]
b = a.copy() #copy method
c = list(a) #list copy with list creation method
d = a[:] #slice 
a[0] = 'integer list are boring'
print("a:", a, "b:", b, "c:", c, "d:", d)



