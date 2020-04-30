import re
fhand = open('regex_sum_461584.txt', 'r')
sum = 0
for line in fhand:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        sum = sum + int(number)
print(sum)