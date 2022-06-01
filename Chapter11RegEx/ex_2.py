#extract the number from each of the lines( New Revision: 39652) using a regex and the findall() method.
# computer the average of the numbers and print out the answer as an integer

import re

x = input ("Please enter a File name (1 = mbox, 2 = mbox-short): ") #speed dial so I don't have to type the fiile name each time
count = 0.0
if x == '1' or x == "mbox.txt":
    file = open("mbox.txt")
elif x == '2'or x == "mbox-short.txt":
    file = open("mbox-short.txt")
else:
    print(x, "is not valid. Please try again.")

for line in file: #finds the "New Revision: *****" lines and pulls the numbers out
    line = line.rstrip()
    find = re.findall('^New.Revision:.([0-9]+)',line)
    #print("find",find)
    if len(find) > 0: #prints the count and the actualy results
        count+=1
        print(find)
    #print(count)
        #count = count + 1
        #sum = find + find

#average = float(sum/count)
#print(average)
