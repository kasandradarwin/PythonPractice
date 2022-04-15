hrsInput = input("Enter Hours: ")
hours = float(hrsInput)

rateInput = input("Enter Rate: ")
rate = float(rateInput)

basePay = (hours * rate)

if hours <= 40:
    print(basePay)

if hours > 40:
    otHours = hours - 40
    otRate = float(rate * 1.5)
    otPay = otHours * otRate
    totalPay = (40 * rate) + otPay
    print(totalPay)
