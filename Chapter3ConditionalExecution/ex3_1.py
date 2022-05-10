hours = float(input("Enter how many hours you worked: "))
rate = float(input("Enter your rate: "))

basePay = hours*rate

if hours <+ 40:
  print("Your pay is: ", basePay)

if hours > 40:
  overtimeHours = hours - 40
  overtimeRate = rate * 1.5
  overtimePay = overtimeHours * overtimeRate
  totalPay = (40 * rate) + (overtimePay)
  print("Your total pay this week is:",totalPay)
