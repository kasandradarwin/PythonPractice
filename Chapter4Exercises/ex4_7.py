def computeGrade (score):
    if score < 0:
        return "Please enter a number greater than 0"
    if score > 1:
        return "Please enter a number less than 1.0"
    elif score >= 0.9:
        return "Grade A"
    elif score >= 0.8:
        return "Grade B"
    elif score >= 0.7:
        return "Grade C"
    elif score >= 0.6:
        return "Grade D"
    else:
        return "Grade F"

scoreInput = input("Enter score between 0.0 and 1.0: ")

try:
    score = float(scoreInput)
except:
    print("Please enter a number only, eg. 0.85")
    quit()

print(computeGrade(score))
