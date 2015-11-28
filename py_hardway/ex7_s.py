# study drills

# the next three lines print the quoted strings.
# where the %s appears it prints the variable defined in short quotes defined at the 
# end of the line
print "Mary had a little lamb."
print "Its fleece was white as %s." 'snow'
print "And everywhere that Mary went."

# what did that do?

print "." * 10 
# this printed 10 of the quoted char at the end of the line.

# this defines variables as char, but really they are very short strings.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch the comma at the end. try removing it and see what happens.

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# These added together with (+) cause this to print Cheese Burger.
# It is the comma that creates the space between the words
# take it away and they run together.