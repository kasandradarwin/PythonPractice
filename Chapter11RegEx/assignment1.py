#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
#and summing up the integers.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_1527512.txt (There are 69 values and the sum ends with 184)

import re

file = open("regex_sum_1527512.txt")

sum = 0
count = 0
for line in file:
    line = line.rstrip()
    matches = re.findall('([0-9]+)', line) #uses the users input, searches for it in each line of the file
    if len(matches) > 0: #lots of empty results, using if statement to eliminate those
        for match in matches:
            sum += int(match) #converting string to integer, and adding them together
            count += 1
print("sum: ", sum)
#print("count: ", count)






#num = list(set(tlstr))
#print(num)
