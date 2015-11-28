hrs = raw_input("Enter Hours:")
h = float(hrs)
r = raw_input("Enter Pay Rate;")
rte = float(r)

if h > 40.0:
    thalf = h - 40.0
    dhalf = thalf * (rte * 1.5)
    dreg = (40.0 * rte)
    pay = dreg + dhalf
    print "Here is your total pay", pay

elif h < 40.0:
    pay = h * rte
    print "Here is your total pay", pay
