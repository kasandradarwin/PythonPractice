#Write a simple program to simulate the operation of the grep command on Unix.
#Ask the user to enter a regex and count the number of lines that matched the regex

import re

x = input("Please enter a RegEx, eg '^Author': ") #gets input from user to use as regex
file = open("mbox.txt")
count = 0
for line in file:
    line = line.rstrip()
    find = re.findall(x, line) #uses the users input, searches for it in each line of the file
    if len(find) > 0:
        count+=1 #counts each match

print("mbox.txt had", count, "lines that matched", x) #prints total
