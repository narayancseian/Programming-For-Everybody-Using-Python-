fname = input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    line = line.strip()
    x = fhand.read()
    print(x.upper())
