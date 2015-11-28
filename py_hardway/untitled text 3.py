 
 """
 close -- closes the file
 read-- read the contents of a file
 Readline-- reads just one line of the text file
 truncate  -- empties the file (distory contents)
 write('stuff') -- literally writes "stuff" to the file
 
 Other commands learned so far:

variable = raw_input("some kind of string for a human, " 
The variable is created from what the human entered after the string was offered as 
instructions
 
variable = raw_input(prompt) 

script, filename = argv , puts the filename to be opened as what is in argv
prompt = '> '

Remember that %s has to have it variable named, "Hi S%! How is your day?" (user_name)
The variable has to be created before it is called in the script.

Other example:

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much to you weigh? ")

print "So you're %r old, %r tall and %r heavy." % (
	age, height, weight)

from sys import argv

script, input1, input2, input2 = argv

file.py = script  (what you called in the command line)
input(n) = what you must put in the command line after the script you are going to run to 
get your variables into the argv.

from sys import argv 
from with in script, you can pull the input(n) from argv and use them as variables in 
your script.

# (\n) means new line
# (\) is an escape sequence available for different characters you would like to use
# one is to use an (\) escape sequence to escape a single ' or double " quote in side the string.
# when you have the use of quotes within the text of a string, it can end the sequence.
# using \ will help you escape the end of the sequence and keep the character.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

Review the rest of your exercise for the other operators. 

"""