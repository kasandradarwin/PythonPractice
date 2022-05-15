#Exercise  9.1: Write a program that reads the words in words.txt and stores
#them as keys in a dictionary. Download a copy of the file from
#https://www.py4e.com/code3/words.txt. It doesn't matter what the values are.
#Then use the 'in' operator as a fast way to check whether a string is in the
#dictionary.

dictionarywords = dict()
file = open("words.txt")

for line in file:
    words = line.split()
    for word in words:
        if word not in dictionarywords:
            dictionarywords[word] = 1
        else:
            dictionarywords[word] += 1

print(dictionarywords)

search_word = input("Please enter a word: ")

if search_word in dictionarywords:
    print("true")
else:
    print("false")
