# call from python system to import the contents of argv
from sys import argv

# When the script is run it will take the file name from the command line

script, filename = argv

# As entered by the user, and open it.
txt = open(filename)

# It will give you the file name and open it for reading. printing the text of the file.
print "Here's your file %r:" %filename
print txt.read()

# Here it prompts you to give the file name again. This time changing the file 
# name to an abstracted name, so that you are not calling the specific file name later in the code.

print "Type the filename again:"
file_again = raw_input("> ")

# here is opens the file again.
file_again = open(file_again)

# and prints it for reading.
print file_again.read()

""" Lines 1-3 use argv to get a filename. 
Line 5 = new command (open), remember this from python doc that you and gusta talked about?
This is all about opening files in your scripts. You can see that down on line 13 you are only 
opening to be read, not written, not reading and writing.  Just read.  This will keep you from writing
over your file.  You want that.  There will be cases where you need to open docs and protect them with 
reading only in the script.  You can give a file a command like read by using (.).  (open.read)
"""