#Write a simple program to simulate the operation of the grep command on Unix.
#Ask the user to enter a regex and count the number of lines that matched the regex

import re

x = input(" Please enter a RegEx, eg '^Author': ")
file = open("mbox-short.txt")

try:
    for line in file:
        line = line.rstrip()
        result = re.findall(x,line)
        if len(result) > 0:    
            print(result)


except:
    print(x, "not found. Please check your Regular Expression and try again")
