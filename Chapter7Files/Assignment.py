# Use words.txt as the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
except:
    print("Sorry, we can't find a file named", fname, "please try again.")
    quit()
contents = fh.read()
upper_contents = contents.upper().strip()
print(upper_contents)
