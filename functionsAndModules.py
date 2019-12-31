###Code Reuse###
#DRY(Don't Repeat Yourself)


#Function#
def my_func():
	print("spam")
my_func()	#spam

def print_ex(word):
	print(word+" !")
print_ex("Hey")	#Hey!

def max(x,y):
	if x>=y:
		return x		#cannot be used outside function
	else:
		return y
print(max(4,5))		#5
z=max(15,7)		#15

#function as argument to other function
def add(x,y):
	return x+y

	def do_twice(func, x, y):
		return func(func(x,y),func(x,y))

a=5
b=10

print(do_twice(add,a,b))		#30


#Modules#
#already created common task code

import random
for i in range(5):
	value=random.randint(1,6)
	print(value)		#any random between 1 and 6 5 times

from math import sqrt as square_root
print(square_root(100))		#10

#Types of modules--->install from external source, pre installed, standard library#