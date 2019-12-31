#high level programming language
#processed at runtime by interpreter, not complined
"""
multi line comments for documentation mostly. Actually a DockSting
"""

#No indentation is used(;)

#hello world program#
print('Hello World!')

#spaces around operators optional, but makes it easier to read
2+2

5 + 4

#/=>decimal division, //=>integer division
20/3	#6.666...	computer can't sore floats accurately

20//3	#6

"""
Operators
+
-
/(float division, always produces decimal eg. 2/2=1.0)
//(integer division or quotient)
*
**(exponent eg. x^y)
%(remainder)
"""

#escape character(\), for single and double quote escape(newline too). only used if single quote is used in single quote string and doule quote used for double quote string#
'Brian\'s mother'

#newlines
#method1
'\n'

#method2
"""Cust: Hello
Shop:Hi
Cust:Test"""


#input and output#
#input
s=input('Enter something: ')

#output
print(s)	#prints everything inside s including Enter something:




#concatenation#
print('a'+'b')	#ab

##can't concatenate string and integer(convert integer to string using str())
'a'+5	#error
'a'+str(5)	#a5

#string*integer(not with other strings or float)
'a'*5	#aaaaa





#Type Conversion#
#to integer
int('7')	#7

#to string
str(7)	#'7'

#to float
float(7)	#7.0
float('7')	#7.0



#Variables#
#no need to declare the data type
x=[]
y=7

#can be reassigned to another data type too(not a good practice)
x='a'
x=7
print(x)	#7

#variable names
#letters,numbers and underscored(can't start with numbers)

#python is case sensitive#
Lname != lname

#can't refer an undeclared variable
#del to remove a variable


#in place operators#
#+,-,*,/,%
x=1
x +=3
print(x)	#4