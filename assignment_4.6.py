def computepay(h, r):
    if h > 40:
        x = h * r
        y = (h -40.0) * (r * 0.5)
        z = x + y
        return z
    else:
        return h * r

hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rates: "))
p = computepay(hrs, rate)
print("Pay", p)