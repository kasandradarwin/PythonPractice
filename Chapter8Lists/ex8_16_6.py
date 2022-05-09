min = None
max = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("please enter an integer only")
        quit()
    if max == None:
        max = num
    if min == None:
        min = num
    if num >= max:
        max = num
    if num <= min:
        min = num
    else:
        continue



print("Maximum:", float(max))
print("Minimum:", float(min))
