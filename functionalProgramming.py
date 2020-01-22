####################Functional Programming#######################

#based around functions
#higher order functions

#Pure functions-->value depends on arguments-->easy to memorize,store so no recalculation need to be done

#LAMBDAS#
#anonymous functions
def my_fun(f, arg):
	return f(arg)
	
print(my_func(lambda x: 2*x*x, 5))		#50


###map###
#high order functions
#operate on lists, or iterables

def add_five(x)
	return x+5
	
nums=[11,22,33,44,55]
result= list(map(add_five,nums))
print(result)							#[16,27,38,49,60]

#lambdas can also be used
result1= list(map(lambda x: x+5, nums)
print(result1)								#[16,27,38,49,60]


###filter###
#remove item that don't match predicate(function that return boolean) from an iterable

nums=[11,22,33,44,55]
res= list(filter(lambda x: X%2 ==0, nums))
print(res)										#[22,44]


############GENERATORS##############
#type of iterables like list or tuple
#don't allow indexing, but can be iterated using for loop
#created using functions and yield statement
def countdown():
	i=5
	while i>0:
		yield i
		i-=1
		
for i in countdown():
	print(i)
	#5
	#4
	#3
	#2
	#1

#yield defines generator, replacing return so as to not destroy local variables

#don't have memory restrictions, can be infinite



###########DECORATORS################
#modify functions using another function
#extend functionality of functions that don't want to modify(kind of inheritance/interface)
def decor(func):
	def wrap():
		print("=======")
		func()
		print("=======")
	return wrap

	
#Method 1
def print_text():
	print("Hello World")

decorated =  decor(print_text)		#changed with annotation @decor in Method 2

decorated()
#=======
#Hello World
#=======
#NOTE----------> decor is the decorator function extending print_text

#Method 2
@decor
def print_text():
	print("Hello World")

print_text()