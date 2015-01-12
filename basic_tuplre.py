#Create a Tuple by using ()
empty_tuple = ()
#TO make a tuple with one or more elements follow each elements
#with a comma. This works for one element tuples 

one_marx = 'Groucho',
#If you have more than one element, follow each element with a comma except the 
#last one 

marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)
#Tuple assign multiple variables at once
a,b, c = marx_tuple #tuple unpacking
print("a:", a, "b:", b, "c:", c)
#You can use tuples to exchange values in one statement without using a temp variable 
password = 'swordfish'
icecream = 'tuttifruitti'
password2, icecream2 = (icecream, password)
print("password: ", password2, "icecream: ", icecream2)
#tuple() conversion function make tuples from other things 
marx_list = ['Groucho', 'Chico', 'Harpo']
print("new method test: ", tuple(marx_list))
#Tuples vs List, tuples can replace list but there are fewer methods
#Tuples use lee space 
#You can't clobber tuple items by mistake
#Named tuples a simple alt to objects
#functions arguments are passed as tuples 
 