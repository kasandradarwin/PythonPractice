def computepay(h, r):
    if h <= 40:
        pay = h*r
    if h > 40:
        otHours = h - 40
        otRate = float(r * 1.5)
        otPay = otHours * otRate
        pay = (40 * r) + otPay
    return pay


hrsInput = input("Enter Hours: ")
h = float(hrsInput)

rateInput = input("Enter Rate: ")
r = float(rateInput)

p = computepay(h, r)
print("Pay", p)
