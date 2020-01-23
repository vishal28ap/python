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


######################################################
######################RECURSION#######################
######################################################

#self reference
def factorial(x):
	if x == 1:
		return 1
	else:
		return x * factorial(x-1)

print(factorial(5))
#120

#can cause runtime error if no exit condition used

#indirect recursion
def is_even(x):
	if x == 0:
		return True
	else:
		return is_odd(x-1)

def is_odd(x):
	return not is_even(x)

print(is_odd(17))	#True
print(is_even(23))	#False



#########SETS###############
num_set = {1,2,3,4,5}

#set have unique values only
#union |(combine 2 sets, no repeat duplicates)
#intersection & (item in both)
#difference - (item in first set not in second)
#symmetric difference ^(item not in other set)
first={1,2,3,4,5,6}
second={4,5,6,7,8,9}

print(first | second)		#{1,2,3,4,5,6,7,8,9}
print(first & second)		#{4,5,6}
print(first - second)		#{7,8,9}
print(second - first)		#{1,2,3}
print(first ^ second)		#{1,2,3,7,8,9}








#######################################################################################################
#############################################WHEN TO USE###############################################
#######################################################################################################

#1. Dictionary
#logical association between key:value pair required
#fast lookup based on custom key
#data constantly modified, as keys are mutable

#2. List
#data doesn't need random access
#simple, iterable collection that is modified frequently

#3. Set
#uniqueness of elements

#4. Tuples
#data cannot change, but iterable using index

#######################################################################################################
#######################################################################################################
#######################################################################################################



###itertools###

#standard library containing functions

#count
#cycle
#repeat
from itertools import count

for i in count(3):
	print(i)
	if i>=11:
		break
		
#3
#4
#5
#6
#7
#8
#9
#10
#11

#takewhile(take items from iterable while predicate functin is true)
#accumulate
#product
#permutations
from itertools import accumulate, takewhile

nums=
list(accumulate(range(8)))
print(nums)		#[0,1,3,6,10,15,21,28]

print(list(takewhile(lambda x: x<=6, nums)))	#[0,1,3,6]
