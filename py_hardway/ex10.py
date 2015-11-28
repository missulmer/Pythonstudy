# (\n) means new line
# (\) is an escape sequence available for different characters you would like to use
# one is to use an (\) escape sequence to escape a single ' or double " quote in side the string.
# when you have the use of quotes within the text of a string, it can end the sequence.
# using \ will help you escape the end of the sequence and keep the character.

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 1 error misspelled backslash_cat when calling it for printing.
