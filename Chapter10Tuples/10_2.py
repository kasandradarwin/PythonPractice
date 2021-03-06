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
    if not line.startswith( "From ") :
        continue
    for word in line:
        word = line.split()
        time = word[5].split(delimiter)
        time = time[0]
        if time not in count:
            #print("time", time[0])
            count[time] = 1
        else:
            count[time] += 1

    #print("hour:",hour)
    #print("time:",time[0])

for v,k in list(count.items()):
    lst.append((v,k))
    print(lst.sort())

    print(v,k)

#lst.sort()


#print(lst)
