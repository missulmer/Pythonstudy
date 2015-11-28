# this exersize is focused on using the raw_input(), using the () parenthesis
# characters.  just like when using the %r %s and such.
# you can also add a prompt for the human so they know what to type. (x, y)
# raw_input("Name? ")
# when the human puts in their name, it fills in the y variable

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much to you weigh? ")

print "So you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
"""
	 open(...)
    open(name[, mode[, buffering]]) -> file object

    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.
"""	
# """ lets you do multi-line comment

