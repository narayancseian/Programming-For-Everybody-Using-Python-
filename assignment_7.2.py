fname = input("Enter file name: ")
fhand = open(fname)
avg = 0
count = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(" ")
    val = line[pos:].rstrip()
    val = float(val)
    count = count + 1
    avg = avg + val

print("Average spam confidence:", avg / count)