from sys import argv
script, file = argv
def print_all(f):
	print f.read()
def rewind(f):
	f.seek(0)
def print_a_line(line_count, f):
	print line_count, f.readline()
current_file = open(file)
print "print the whole file:\n"
print_all(current_file)
print "rewind a file like a tape"
rewind(current_file)
print "print two lines"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

