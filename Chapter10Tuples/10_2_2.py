#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day
#for each of the messages. You can pull the hour out from the 'From ' line by finding the time and
#then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = dict()
lst = list()

delimiter = ':'
for line in handle:
    if line.startswith( "From "):
        word = line.split()
        time = word[5]
        time = time.split(delimiter)
        hour = time[0]


        if hour not in count:
            count[hour] = 1
        else:
            count[hour] += 1

for k,v in list(count.items()):
    lst.append((k,v))

lst.sort()
for k,v in lst:
    print(k,v)
