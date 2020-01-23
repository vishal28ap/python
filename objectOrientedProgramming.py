########################################################################
#################################OOPS###################################
########################################################################


###Classes###
#3 paradigms of programming--->imperative(statements), functional(function), oop(classes)

#oop
class Cat:
	def __init__(self,color,legs):
		self.color=color
		self.lega=legs
		
felix=Cat("ginger",4)
rover=Cat("brown",4)

#__init__ method most imp
#called when instance of class is created, using classname as function
#all methods must have self as first parameter(instance of method)

class Dog:
	def __init__(self,name,color):
		self.name=name
		self.color=color

	def bark(self):
		print("Woof!")

fido=Dog("Fido","brown")
print(fido.name)			#Fido
fido.bark()					#Woof!

#AttributeError--> access attribute of an instance that isn't define, i.e. call an undefined method



###Inheritance###

#superclass
class Animal:
	def __init__(self,name,color):
		self.name=name
		self.color=color

class Cat(Animal):
	def purr(self):
		print("Purr...")
		
class Dog(Animal):
	def bark(self):
		print("Woof!")
		

fido= Dog("Fido","brown")
print(fido.color)		#brown
fido.bark				#Woof!


#subclass overrides method of superclass
class Wolf:
	def __init__(self,name,color):
		self.name=name
		self.color=color
	
	def bark(self):
		print("Grr...")
		
class Dog(Wolf):
	def bark(self):
		print("Woof!")
		
husky=Dog("Max","grey")
husky.bark					#Woof!



#super function refers to parent class
class A:
	def spam(self):
		print(1)
		
class B(A):
	def spam(self):
		print(2)
		super().spam()
		
B().spam()		
#2
#1



########Magic Methods########

#double underscore at beginning and end of names.
#also known as dunders
#functionality that can't be represented by normal methods
#operator overloading
class Vector2D:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def __add__(self,other):
		return Vector2D(self.x+other.x,self.y+other.y)

first= Vector2D(5,7)
second= Vector2D(3,9)
result=first+second
print(result.x)		#8
print(result.y)		#16

#__sub__,__mul__,__truediv__,__floordiv__,__mod__,__pow__,__and__,__xor__,__or__


############OBJECT LIFECYCLE##############

