#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.

#✅The program looks for 'From ' lines and
#✅takes the second word of those lines as the person who sent the mail.
#✅The program creates a Python dictionary that maps the sender's mail address to a
#count of the number of times they appear in the file.

#After the dictionary is produced, the program reads through the dictionary
#using a maximum loop to find he most prolific committer.

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print("Oops! Please try again, we couldn't find",name)
counter = dict()
for line in handle:
    if not line.startswith('From'):
        continue
    words = line.split()
    words = words[1:2]

    for word in words:
        counter[word] = counter.get(word,1) +1
