print "welcome to my project"
print "i\'d like to learn about python second version"

python = """
Python is one of programming language. it is easy to understand./n it has different functions, many characters and
many codes.
"""
print "python"

sum = 8/2*6-8+3
print "the sum is %s" % sum

def formula(total):
	foot_balls = total * 50
	baskets = foot_balls/10
	return foot_balls, baskets

total = 100
balls , baskets = formula(total)

print "in total %d" % total
print "we'd have %d balls, %d baskets" % (balls, baskets)
total = total / 2
print "we'd have %d balls and %d baskets" % formula(total)
