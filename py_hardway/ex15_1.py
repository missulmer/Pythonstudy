"""
# call from python system to import the contents of argv

from sys import argv

# When the script is run it will take the file name from the command line

script, filename = argv

# As entered by the user, and open it.
txt = open(filename)

# It will give you the file name and open it for reading. printing the text of the file.
print "Here's your file %r:" %filename
print txt.read()
"""

print "Type the filename at all:"
file_again = raw_input("> ")

with open(file_again, 'r') as in_file:
	print in_file.read()
	
print "done"
# here is opens the file again.
#file_again = open(file_again)

# and prints it for reading.
#print file_again.read()

#file_again.close()