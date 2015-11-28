fname = raw_input("Enter file name: ")
fhand = None
try:
    fhand = open(fname)
except:
    print 'File cannot be opened.', fname
    exit()

#list constructor
lst = []