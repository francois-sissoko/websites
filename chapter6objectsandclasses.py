#Chapter 6. OH OH: Objects and Classes 

#Everything in Python is an object
#If you type num = 7 you create and object of type
#integer with the value 7 and assign an object ref to the name num

#objects contain both data(variables, called attributes and code(functions, called methods)

#When you create new objects no one has ever created before you have to create a class.
#Ex 7 and 8 belong to the class integer and can use add and mult 
#'cat' and 'duck belong to class string and can use methods capitalize()

print("Example creating a class with the init methiod")
print("self is like this in javascript and refers to the current obj")

class Person():
    def __init__(self,name):
	    self.name = name	
hunter = Person("Francois")
print('The mighty hunter', hunter.name)

#inheritance is creating a new class from an existing class but with some additions or changes
print("creating a class that inherits,car is the superclass and has a method yugo just passes")
class Car():
	def exclaim(self):
		print("I'm a Car!")
	def riding(self):
		print("Cars ride clean")
class Yugo(Car):
	def riding(self):
		print("Cars ride clean but Yugos ride dirty")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
print("Calling 'exclaim' method on car")  
print(give_me_a_car.exclaim())
print("Calling 'exclaim' method on yugo")
print(give_me_a_yugo.exclaim())

print("you can also overwrite methods")

print("Calling 'riding' method on car")  
print(give_me_a_car.riding())
print("Calling 'riding' method on yugo 'overwrited'")
print(give_me_a_yugo.riding())

#You can refer to the parant class as super()

print("Example of getting help from a Parent")
class Person():
	def __init__(self, name):
		self.name = name
		
class EmailPerson(Person):
	def __init__(self, name, email):
		super().__init__(name)
		self.email = email
		
bob = EmailPerson('Bob Frapples', 'bob@frapples.com')
print(bob.name)
print(bob.email)