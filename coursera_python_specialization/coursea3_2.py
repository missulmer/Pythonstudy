import sys;

hrs = raw_input("Enter Hours:")

try:
    h = float(hrs)
    print "Uhu"
except ValueError, ex:
    print "Ooops, hrs is not a float. I am going to quit.", ex.message
    sys.exit(1)

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

#gusta wont tell me how to get this thing to stop executing if it hits the except code block. :(
#tuck all your your trys in one block then have your exception cases
#when you have nested trys you need to 'unnest' your extemptions 'inside out'