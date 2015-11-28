from sys import argv

script, red, fat, fuck = argv

print "The script is called:", script
print "Your first variable is:", red
print "Your second variable is:", fat
print "Your third variable is:", fuck

"""
Well that was a pain in the ass.  here is what I fucked up.
when importing from argv you need to input command line variables in order to get the script to print the strings you 
want to have printed with the variables.  I was failing to run the script with input variables.
the purpose of argv is to hold input variables for you, if you don't put in any it the script wont work.

"""

