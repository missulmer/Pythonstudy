# This lesson is focused on string versatility.  You format a string when using "
# A sting is something a program might give to a human.  You can print and save
# strings to files, send strings to web servers and other stuff
# Stings are super useful and you can pack variables into them.

#now we create our variables
	
my_name = 'Laura A. Ulmer'
my_age = 35 # honestly
my_height = ((5.00 * 12.00) + .50)/ 12.00 # inches to feet
my_weight = 125 / 2.2 # Lbs to KG
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blond'

print "Let's talk about %s." % my_name
print "She's %f feet tall." % my_height
#Gusta had me change my formatter to %f instead of %d, which is for ints. I still need to fix my math.

print "She's %d kilograms." % my_weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair" % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." % my_teeth

# tricky line.

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)


#still having issues producing a floating point.  Get help.
# see line 10

# what is the difference between %d, %s, %r
# You'll learn more about this as you continue, but they are "formatters." 
# They tell Python to take the variable on the right and put it in to replace the %s with its value. 
# I don't get it, what is a "formatter"? Huh? The problem with teaching you programming is that to understand many of my descriptions 
# you need to know how to do programming already. The way I solve this is I make you do something, and then I explain it later. 
# When you run into these kinds of questions, write them down and see if I explain it later.
# love Zed