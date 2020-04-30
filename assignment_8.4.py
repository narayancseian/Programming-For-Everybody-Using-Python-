fname = input("Enter file name: ")
fhand = open(fname)
words = list()
for line in fhand:
    words = words + line.split()
    words.sort()
words2=[]

for word in words:
	if word not in words2:
		words2.append(word)
print(words2) 