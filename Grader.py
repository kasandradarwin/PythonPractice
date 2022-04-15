score = input("Enter score between 0.0 and 1.0: ")

try:
    score = float(score)
except:
    print("Please enter a number only, eg. 0.85")
    quit()


if score < 0:
    print("Please enter a number greater than 0")
elif score > 1:
    print("Please enter a number less than 1.0")
elif score >= 0.9:
    print("A")
elif score >= 0.8:
    print("B")
elif score >= 0.7:
    print("C")
elif score >= 0.6:
    print("D")
else:
    print("F")
