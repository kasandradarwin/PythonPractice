#extract the number from each of the lines using a regex and the findall() method.
# computer the average of the numbers and print out the answer as an integer

import re

x = input ("Please enter a File name (hint 1 = mbox, 2 = mbox-short): ")

if x == 1 or x == "mbox.txt":
    file = open("mbox.txt")

elif x == 2 or x == "mbox-short.txt":
    file = open("mbox-short.txt")

else:
    print(x, "is not valid. Please try again.")
