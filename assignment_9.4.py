name = input("Enter file name:")
if len(name) < 1: name = "mbox-short.txt"
fhand = open(name)
text = fhand.read()

counts = dict()
for line in fhand:
    if not line.startswith('From:'): continue
    words = line.split()
    words = words[1]
    counts[words] = counts.get(words, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)       