name = input("Enter file name:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

hours = dict()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()

    hour = words[5].split(":")
    hours[hour[0]] = hours.get(hour[0],0) + 1

list = []

for a,b in hours.items():
    list.append((a,b))

list.sort()


for a,b in lst:
    print(a,b)