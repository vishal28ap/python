###Dictionary###
dict={}
dict1={"a":1,"":2}		#key:value
#key immutable


###dictionary functions###
dict={}
dict["a"]=1
print(dict)		#a: 1

#key in dictionary#
nums={
1:"one"
2:"two",}

print(1 in nums)		#True
print(4 in nums)		#True

print(nums.get(2))		#two
print(nums.get(10)		#None
print(nums.get(100, "Not present")		#Not Present



###Tuples###
#similar to list, except immutable
#created using paranthesis()

words=("span", "eggs", "sausages",)
#type error if user try to assign an already created words
words[0]= "cheese"		#TypeError

#can also be created without paranthesis, usin comma
my_tuple="one", "two"
print(my_tuple[0])		#one

#empty tuple
tup=()

##faster than list, can't be changed



###########List Slice############

#slice always return value, even empty value. Doesn't return null
#index used for slicing(final values 1 less) i.e. first index included, last isn't

squares=[0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])		#[4,9,16,25]
print(squares[0:1])		#[0]

print(squares[:3])		#[0,1,4]
print(squares[7:])		#[49,64,81]

##slicing also can be done on tuples

print(squares[::2])		#[0,4,16,36,64]
print(squares[2:8:3])	#[4,25]


##negative values
print(squares[1:-7])		#[1,4]
print(squares[::-1])		#[81,64,49,36,25,16,9,4,1,0]



##########list comprehension#############
cubes=[i**3 for i in range(5)]
print(cubes)		#[0,1,8,27,64]

evens=[i**2 for i in range(10) if i**2%2 == 0]
print(cubes)		#[0,1,4,16,36,64]

###MemoryError###if list comprehension runs out of memory


###############String Formatting#################
nums=[2,3,4]
msg="Numbers:{0} {1} {2}".format(nums[0],nums[1],nums[2])		##0,1,2 bring index positions of string
print(msg)		#Numbers: 2 3 4


#########ADDITIONAL FUNCTIONS############
print(",".join(["spam","eggs","ham"]))		#spam,eggs,ham
print("Hello Me".replace("Me","World"))		#Hello World
print("This is a sentence".endswith("sentence"))		#True
print("This is a sentence".startswith("This"))		#True
print("This is a sentence".upper())		#THIS IS A SENTENCE
print("This is a sentence".lower())		#this is a sentence
print("spam,eggs,ham".split(",")		#['spam','eggs','ham']

#min,max,abs,sum

nums=[55,44,33,22,11]

if all([i<5 for i in nums]) 
print("All larger than 5")		#All larger than 5

if any([i%2 == 0 for i in nums]) 
print("At least one is even")		#At least one is even

for v in enumerate(nums)
print(v)
#(0,55)
#(1,44)
#(2,33)
#(3,22)
#(4,11)