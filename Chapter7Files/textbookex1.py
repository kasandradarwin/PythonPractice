fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Sorry, we can't find a file named", fname, "please try again.")
    quit()

for line in fh:
    print(line.upper())
