###EXCEPTIONS###

#try/except block#
try:
	num1=7
	num2=0
	print(num1/num2)
	print('Done')
except:
	print('zerodivision error')
	
try:
	num1=7
	num2=0
	print(num1/num2)
	print('Done')
except ZeroDivisionError:
	print('zerodivision error')
except ValueError:
	print('Value error')
	
	
#finally#
#bottom of try/except
#will run no matter what happens
try:
	num1=7
	num2=0
	print(num1/num2)
	print('Done')
except:
	print('zerodivision error')
finally:
	print("Finally")

	
###raise exceptions###
print(1)
raise ValueError
print(2)		#2 won't be printed as exception already raised


print(1)
raise NameError("Invalid Name")
print(2)		#2 won't be printed as exception already raised, Invalid name printed

###reraise exception in try catch block###
try:
	num1=7
	num2=0
	print(num1/num2)
	print('Done')
except:
	print('zerodivision error')
	raise
	

###assertion###
assert 2+2 == 4
print(5)	#5
assert (15>10), "Yes"	#Yes gets printed
assert 2 == 6
print(7)	#don't get printed, AssertionError



###open file###
myfile= open("filepath")

myfile2= open(filepath,mode)	
#modes= r, w, b(binary), a(append), bw(binary write), r+(read and write)

###file once open should be closed###
myfile.close()


#read files#
file=open("filename.txt", r)
cont=file.read()	#file.read(5) will read 5 bytes of file
print(cont)		#print content of file
file.close()



#readline methods to return a list in which each element is a line in file
file=open("filename.txt", r)
print(file.readlines())		#print each line as list
file.close()

#for loop can be used
file=open("filename.txt", r)
for  line in file:
	print(line)		#print each line
file.close()



###write on a file###
file=open("filename.txt", w)	#create a file, if don't exist already
file.write("Any Text")		#existing content deleted
file.close()



#write methods
file=open("filename.txt", w)
msg="Hello"
p=file.write(msg)		
file.close()
print(p)		#return 5(number of bytes 1 char= 1 byte)


###temp var###
with open("filename.txt") as f:
	print(f.read())

#file is automatically closed at end of with statement