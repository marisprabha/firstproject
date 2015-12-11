numbers = '\n1\n2\n3\n4\n5\n'
print "here are the numbers", numbers
print"""prabha
pandi
khanushma"""
formatter = "%r %r"
print formatter % ('a', 'b')
print formatter % ('good', 'bad')
tabs = "\ti\tam\ta\tgirl\t"
print tabs
x = "yy \' zz \" aa \a ff \b vv \f ss \r kk \t"
print x 
y = "\r jj"
print y
age = raw_input("how old are you?")
print age
print "how are you?."
health = raw_input()
x = raw_input("who are you?")
print "you are %r" %(x)
from sys import argv
x, y, z = argv
print "a is", x
print "b is", y
print "c is", z

