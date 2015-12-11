def add(a,b):
	print "adding %d + %d" % (a,b)
	return a+b
def subtract(a,b):
	print "subtracting %d - %d" % (a,b)
	return a-b
def multiply(a,b):
	print "multiplying %d * %d" %(a,b)
	return a*b
def divide(a,b):
	print "dividing %d / %d" %(a,b)
	return a/b
print "applying numbers.."
a = add(1,2)
b = subtract(5,4)
c = multiply(6,7)
d = divide(8,9)
print "a = %d, b = %d, c = %d, d = %d" %(a,b,c,d)
e = add(a,subtract(b,multiply(c,(divide(d,1)))))
print "e is %d" %e
