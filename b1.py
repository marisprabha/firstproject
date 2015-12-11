from sys import argv
from os.path import exists
script, f1, f2 = argv
print "copying from %s to %s", (f1,f2)
in_file = open(f1)
f = in_file.read()
print "the length of input file is %d bytes" % len(f)
out_file = open(f2, 'w') 
out_file.write(f)
print"done"
in_file.close()
out_file.close()

