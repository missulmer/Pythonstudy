# comment on each line

# Here we are setting variables, in this case X, the x variable creates within it a formatted variable which is also set in this creation.
x = "There are %d types of people." % 10

# creating the variable binary
binary = "binary"

# creating variable do_not
do_not = "don't"

# creating variable y, like x we are creating a string that calls formatted variables into it.
# first example of string within string.
y = "Those who don't know %s and those who %s." % (binary, do_not)

# printing the strings created as variables which also call formatted variables into it.
print x
print y

# these strings call in a variable that has variables within in it.
# these are also 'string inside of string' examples
print "I said: %r." % x
print "I also said: '%s'." % y

# we again create variables, joke_evaluation calls a formatted variable within it.
# another string within a string example.
hilarious = False
joke_evaluation = "Isn't that joke funny?! %r"

# this sting calls the joke_evaluation variable and then calls the variable hilarious which
# returns false as an answer, the last string within string example.	
print joke_evaluation % hilarious

# here we are introduced to formatters w and e.  w which prints the left side of a string
# and e prints the right side. They will be printed together to create a complete sentence.
w = "This is the left side of..."
e = "a string with a right side."

# here is how they are placed together, and will print 
# "This is the left side of...a string with a right side."
print w + e 	

# more on formatters.  %r is best for debugging, and other formats are for actually displaying
# variables. It is for debugging because it displays a "raw" data variable.
# %s and %d the these are used to display actual variables to people.

# why single (') quotes inside the string and double (") outside.  
# style choice.  It makes neater looking code to read.

# Review of what was introduced in this lesson
# print
# variable creation
# placing variables within strings
# placing multipul variables within a string
# the formatter
# %r = raw data
# %d = pull a variable 
# %s = pull a variable
# w = pull the left side of a string
# e = pull the right side of a string
		