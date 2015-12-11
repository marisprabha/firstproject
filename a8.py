from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "copying from %s to %s", (from_file, to_file)
in_file = open(from_file)
f = in_file.read()
print "the input file is %d bytes long" % len(f)
out_file = open(to_file, 'w')
out_file.write(f)
print "done."
out_file.close()
in_file.close()

