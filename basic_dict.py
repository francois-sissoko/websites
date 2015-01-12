#basic dictionary in Python opens youtube video

import sys 
import webbrowser

quotes = {
	"Moe" : "A wise guy,, huh?",
	"Larry" : "Ow!",
	"Curly" : "nyak,NYAK",
	"Nyan cat"  : "https://www.youtube.com/watch?v=QH2-TGUlwu4"
	}
	
stooge = "Curly"
cat = "Nyan cat"
print(stooge, "Says:", quotes[stooge])
webbrowser.open(quotes[cat])
#Dictonaries are key value pairs can be any o fpython's immutable types, 
#boolean, int, float, tuple, string and othersthat you'll 
#you'll see in late chapters 

#in other lang dictonaries are aksi call assicuatuve arrays
#hashes, or hashmaps 

#create an empty dictionary
empty_dict = {}

#Small dictionary between Ambrose Biere's and The Devil's Dictionary 
bierce = {
	"day": "A period of twenty-four hours, mosty misspent",
	"positive": "mistaken at the top of one's voice",
	"misfortune": "The kind of fortune that never misses",
	}
#You can use dict() to convert two-value sequence into dictionary 
lol = [["strantium", '90'],["carbon", '14']]
print("elements: ", dict(lol))
#the first value is the key the second is the value\
listOfTwoCharString = ['ab','cd','ef']
print("list of two char string turned into dictionary:", dict(listOfTwoCharString))
#zip() makes easy to create these two item sequencee
pythons = {
	'Chapman' : 'Graham',
	'Cleese' : 'John', 
	'Idle' : 'Eric',
	'Jones': 'Terry',
	'Palin': 'Michael',
	}
#update copies the keys from one dictionary into another 
others = {
	'Marx': 'Groucho', 
	'Howard': 'Moe'
	}
print("update pythons with others:", pythons.update(others))

#TO test for a key by using in method
print("Test for key in dictionary:", 'Chapin' in pythons)
# To avoid errors use get function. You provide the dictionary, key, and optional value.
# If the key exist you get its value
pythons.get('Marx', 'Not a python')
signals = {
	'green':'go',
	'yellow':'go faster',  
	"red" : "smile for the camera" 
	}
print("blah the keys are:", signals.keys())
# calling list of signals.keys converts the object to a list
print("The list of keys is:", list(signals.keys()))
# ALl you need is list() to turn results of values() and items() into normal python lists
print("All the values of dictionary:", signals.values())
print("All the key values of dictionary using items", signals.items()) #returned as a tuple 
