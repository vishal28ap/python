#control structures

#Boolean#
#string can be compared lexicographically i.e. based on alphabetical order of their characters


#####indentation is mandatory in Python###


#if statement#
if expression: 
	statements
	
#else statement#
x=4
if x==5:
	print('Yes')
else:
	print('No')
	

#if-else ladder#
num=7
if num == 5:
	print('5')
elif num ==6:
	print('')
else:
	print('Not')
	

#Boolean Logic#
a and b
a or b
not a


#Operator Precedence#
#paranthesis->exponential->multiplication/diision->addition/subtraction-->in/not in/is/is not/</<=/>,>=,!=,== -->not-->and-->or-->Assignment


#while loops#
i=1
while i<=5:
	print(i)
	i=i+1
#ctrl+c to stop infinite loop
#break--> end loop prematurely
#continue --> back on top of loop


#list#
#list of list act as multidimensional array


#string also can print like list
s="Hello"
print(s[4])	#o

#add item at certain index
num=[7, 7, 7, 7, 7,7]
num[2]=2
print(num)	#[7, 7, 2, 7, 7, 7, 7]

num=num*2	#[7, 7, 2, 7, 7, 7, 7,7, 7, 2, 7, 7, 7, 7]	#kind of like string
num=num+[2,3]	#7, 7, 2, 7, 7, 7, 7,7, 7, 2, 7, 7, 7, 7,2,3

#string can be thought as list of characters that can't be changed


#list operators#
#in
a=[x,y,z]
print(x in a)	#True

#not
print(not 10 in a)	#True



#List Functions#
#append
nums=[1,2]
nums.append(3)

#length
print(len(nums))		#3

#length notmal function, but append a method(that y dot used)#

#insert
nums.insert(3, 7)	#.insert(index, thingToInsert)
print(nums)		#1,2,3,7

#index
print(nums.index(1))	#0
#print index of first occurence of the letter in list



#other important functions#
max(nums)
min(nums)
nums.count(3)		#count occurance of 3 in list
nums.remove(7)		#remove 7
nums.reverse()		#reverses list



#Range#
#create sequential list of numbers
numbers = list(range(10))
print(numbers)		#[0,1,2,3,4,5,6,7,8,9]
#call to list imp

#first to second
numbers1=list(range(3,8))
print(numbers1)		#[3,4,5,6,7]

#interval in range
numbers2=list(range(5,20,2))
print(numbers2)		#[5,7,9,11,13,15,17,19]



#For Loop#
words=['a','b','c']
for word in words:
	print(word)		#a b c
#for loop in python is like for each loop


#for loop with range #it is indexed
for i in range(5):
	print("Hi")		#Hi Hi Hi Hi Hi

