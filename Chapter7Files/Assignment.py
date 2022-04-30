# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
contents = fh.read()
upper_contents = contents.upper().strip()
print(upper_contents)
