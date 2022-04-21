smallest = None
largest = None

while True:
    num = input(" Please enter a number: ")
    if num == 'done':
        break
    try:
        numero = int(num)
    except:
        print("invalid input")
    if smallest == None:
        smallest = numero
    elif numero < smallest:
        smallest = numero
    if largest == None:
        largest = numero
    elif numero > largest:
        largest = numero


print("Maximum:", largest)
print("Minimum:", smallest)
