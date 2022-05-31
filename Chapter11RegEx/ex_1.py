#Write a simple program to simulate the operation of the grep command on Unix.
#Ask the user to enter a regex and count the number of lines that matched the regex

import re

x = input("Please enter a RegEx, eg '^Author': ")
file = open("mbox-short.txt")
count = 0
try:
    for line in file:
        line = line.rstrip()
        print("line: ",line)
        print ("x: ", x)
        result = re.findall(x,line)
        #print("result: ",result)
        for word in line:
            print("count pre len: ", count)
            if len(line) > 0:
                count += 1
                print("count post len: ", count)

    #print("mbox.txt had", count, "lines that matched", x)



except:
    print(x, "not found. Please check your Regular Expression and try again")
