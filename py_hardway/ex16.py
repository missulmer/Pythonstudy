 #make a simple text editor
 
from sys import argv
 
script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."
 
# raw_input = ("?")  I accidentally redefined the symbol for raw input
# from the function to a string. The correction follows.

raw_input("?")
#This just calls the function. 

print "Opening this file..."
target = open(filename, 'w')
 
print "Truncating the file.  Good-bye!"
target.truncate()
 
print "Now I going to ask for three lines."
 
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
 
print "I'm going to write these to the file."
 
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# watch your slashes carefully. You originally had /n rather than \n
 
print "And finallay, we close it."
target.close()




