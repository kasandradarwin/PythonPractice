grade = float(input("Please enter a score between 0.0 and 1.0: "))

if grade >= 0.9:
  print(grade, "A. Great work!")
elif grade >= 0.8:
  print(grade, "B. Good work!")
elif grade >= 0.7:
  print(grade, "C")
elif grade >= 0.6:
  print(grade, "you're barely cuttin' it")
elif grade < 0.6:
  print(grade, "Fail. Please try again")
