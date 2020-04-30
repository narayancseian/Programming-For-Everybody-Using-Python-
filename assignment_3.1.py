hrs = float(input("Enter Hours: "))
rt = float(input("Enter Rate: "))
if hrs > 40:
    reg = hrs * rt
    otp = (hrs - 40.0) * (rt * 0.5)
    xp = reg + otp
else:
    xp = hrs * rt
print(xp)