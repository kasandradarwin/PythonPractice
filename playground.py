items = ['d', 'b', 'c', 'a']
def chop():
    print(items[1:3])

def middle(x):
    del x[1:3]
    print(x)

print(sorted(items))
chop()
middle(items)
print(sorted(items))
