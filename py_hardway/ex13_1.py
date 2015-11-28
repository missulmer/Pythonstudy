
from sys import argv

script, user_name = argv
prompt = '> '

print "Hi, %s I am the %s script and I am all about angry words." % (user_name, script)

print "I'd like to play a game, what is your favorite color?"
color = raw_input(prompt)

print "what is your favorite descriptor"
descriptor = raw_input(prompt)

print "What is your favorite sware word?"
sware_word = raw_input(prompt)

print "So you are a %r, %r, %r!" % (color, descriptor, sware_word)

"""
Well that was a pain in the ass.  here is what I fucked up.
when importing from argv you need to input command line variables in order to get the script to print the strings you 
want to have printed with the variables.  I was failing to run the script with input variables.
the purpose of argv is to hold input variables for you, if you don't put in any it the script wont work.

I have no idea. Get help.

ok so using ex14 and some screwing around, i have used raw_input and argv to create a script that insults you with your
own words.

Nice.  I will work at amazon in no time. 

"""
