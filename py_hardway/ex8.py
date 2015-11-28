formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (
			"I had this thing.", 
			"That you could \"type up right.",
			'But it didn\'t "sing.',
			"So I said goodnight."
)			
# mistake only 1.  I missed the quotes around the group of %r.
# The reason for the difference in quotes is because there is no comma.
# python favors single quotes, where a (') appears in the sting or (")
# it will trade between the quotes as it needs.  you can use \ to escape it.

