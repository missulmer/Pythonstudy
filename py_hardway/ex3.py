#This exersize is about introducing math concepts into code.
#Following the lesson, we will play with math

# this line prints the string in quotes
print "I will now count my chickens:"

# this line prints "Hens" with the total of the math afterward
print "Hens", 25 + 30 / 6

#this line prints "roosters" with the total of the math afterward
print "Roosters", 100 - 25 * 3 % 4

# this line prints the string in quotes
print "Now I will count the eggs:"

# this line does the math and provides the product
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# this line prints the string which exposes the math we want to compute
print "Is it true that 3 + 2 < 5 - 7?"

# this string shows the product as a true or false based on the question posed by the < sign
print 3 + 2 < 5 - 7

# this line provides the string which exposes the mathematical question, as well as gives the sum afterward 
print "What is 3 + 2?", 3 + 2 

# this line provides the string which exposes the mathematical question, as well as gives the difference afterward 
print "What is 5 - 7?", 5 - 7

# this line prints the string in quotes
print "Oh, that's why it's False."

# this line prints the string in quotes
print "How about some more?"

#These stings print the sting as well as answers the question posed by the >, >=. <= signs (True/False)
print "is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

print "study buddy question about floating point. Rounding 2.675 to only 2 places after the point"
print round(2.675, 2)
print "1/3 as a rounded decimal"
print round(1/3, 3)

# there are two ways to see your math "floating point"
# 1 is casting

print "casting example", float(1) / float(3)
print "casting example", float(1) / 3
print "casting example", 1 / float(3)

# second example is not to use ints
print "casting example", 1.0 / 3.0

#using a decimal forces the use of a float.



