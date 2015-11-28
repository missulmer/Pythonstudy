fname = raw_input("Enter file name: ")
fhand = None
try:
    fhand = open(fname)
except:
    print 'File cannot be opened.', fname
    exit()

lst = [] #list constructor

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if not word in lst:
            lst.append(word)
lst.sort()
fhand.close()

print lst

