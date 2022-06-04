#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
#and summing up the integers.

import re

file = open("regex_sum_42.txt")

sum = 0
count = 0
for line in file:
    line = line.rstrip()
    matches = re.findall('([0-9]+\s)', line) #uses the users input, searches for it in each line of the file
    if len(matches) > 0:
        for match in matches:
            sum += int(match)
            count += 1
print("sum: ", sum)
print("count: ", count)






#num = list(set(tlstr))
#print(num)
