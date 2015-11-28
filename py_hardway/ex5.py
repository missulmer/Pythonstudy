# This lesson is focused on string versatility.  You format a string when using "
# A sting is something a program might give to a human.  You can print and save
# strings to files, send strings to web servers and other stuff
# Stings are super useful and you can pack variables into them.

#now we create our variables

my_name = 'Laura A. Ulmer'
my_age = 35 # honestly
my_height = 75 # inches
my_weight = 125 # Lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blond'

print "Let's talk about %s." % my_name
print "She's %d inches tall." % my_height
print "She's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair" % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." % my_teeth

# tricky line.

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
