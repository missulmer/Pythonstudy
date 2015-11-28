
fname = raw_input("Enter file name: ")
fh = None
try:
    fh = open(fname)
except:
    print 'File cannot be opened.', fname
    exit()

dspam = "X-DSPAM-Confidence: "
pos = len(dspam)
count_choc = 0
sum_score = 0.0
for line in fh:
    if line.startswith(dspam):
        count_choc += 1
        score = line.strip()[pos:]
        float_score = float(score)
        sum_score += float_score
avg = sum_score/count_choc
print "Average spam confidence: {0}".format(avg)








