\\In the code below: we are using a while loop to continue to request score until it meets a set of condidtions.
So while the variable scr = none, the while loop will continue.  We want to be sure that the user input is in the correct type
and format for the remainder of the program, because the program is to return a grade value mapped to a score in a float format.
in the try section, we are both converting the input to a floating point, and comparing it to conditions.  If we get an exeption
because the user entiered a non-numberic input it will provide an approproate error message.  If the input fails to meet the other conditions
then the appropate message is shown and scr is set back to None, to begin the loop again.

Note that we have try and except with nested if statments.  The ifs come before the exeption because if the float conversation fails
it will skip the if conditionals and drop right to the exeption.  The conversation and ifs are nested within the try
the indention forms each block of logic.
\\

scr = None

while (scr is None):
    score = raw_input("Enter Score:")

    try:
        scr = float(score)
        if scr < 0.0:
            print "score can't be less than zero"
            scr = None
        if scr > 0.9:
            print "score can't be greater than 1"
            scr = None
    except ValueError, ex:
        print "Please provide score as a decimal number. (Float Error)"
        #scr = None
if scr >= 0.9:
    print 'A'
elif scr >= 0.8:
    print 'B'
elif scr >= 0.7:
    print 'C'
elif scr >= 0.6:
    print 'D'
elif scr < 0.6:
    print 'F'

print 'all done'

