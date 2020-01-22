###############TEXT ANALYZER PROJECT##############


#1. File open and REad
filename=input(Enter a FileName : ")

with open(filename) as f:
	text= f.read()
print(text)
#return #2 here
#print(count_char(text,"r"))


#2. How many times a character occur in string
def count_char(text, char)
	count=0
	for c in text:
		if c == char:
			count+=1
	return count


#3. What % of text each character of alphabet occupies
for char in "abcdefghijklmnopqustuvwxyz":
	perc= 100* count_char(text, char)/len(text)
	print("{0} - {1}%".format(char, round(perc,2)))