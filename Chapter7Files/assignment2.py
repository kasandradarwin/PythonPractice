fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Sorry, we can't find a file named", fname, "please try again.")
    quit()
runningtotal = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    decimal = line.find('.')
    number = float(line[decimal-1:])
    runningtotal = runningtotal + number
    count = count + 1
    average = runningtotal/count

print ("average spam confidence:", average)
