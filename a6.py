from sys import argv
script, file_name = argv
target = open(file_name, 'w')
target.truncate()
print "type two lines."
line1 = raw_input("line1:")
line2 = raw_input("line2:")
print "write these lines to the file"
target.write(line1)
target.write(line2)
target.close()
f = open(file_name)
print f.read
