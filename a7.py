from sys import argv
script, file = argv
f = open(file)
print "the file is", file
print f.read()


