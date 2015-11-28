def computepay(h,r):

    if h > 40.0:
        thalf = h - 40.0
        dhalf = thalf * (r * 1.5)
        dreg = (40.0 * r)
        pay = dreg + dhalf

    elif h < 40.0:
        pay = h * r

    return pay

#    elif h < 40.0:
#        pay = h * r
#        return pay

r = 10.50
hrs = raw_input("Enter Hours:")
h = float(hrs)
p = computepay(h,r)

print computepay(h,r)

