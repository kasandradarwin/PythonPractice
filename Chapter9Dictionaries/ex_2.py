#9.2 Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this, look for line that start with "from", then look for the third word to keep a running count of
# each of the days of the week. At the end of the program, print out the contents of your dictionary (order does not matter)


name = input("Enter file: ") #open the file, handle exceptions
if len(name) < 1:
    name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print("Oops! Please try again, we couldn't find",name)
counter = dict()
for line in handle:
    if not line.startswith('from '): #pulls out lines starting with from,splits the line, pulls out day of week
        continue
    words = line.split()
    words = words[2:3] # print out day of the week the commit was done
    for word in words: #filters out duplicates and increases the count for that word instead
        counter[word] = counter.get(word,0) +1

#printing the email of the person who sent the most emails, as well as the count

print(counter.values())

#print(emailer, emailsent)
