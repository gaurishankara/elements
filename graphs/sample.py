from collections import namedtuple
cord = namedtuple('cord', ('x', 'y'))
def outerFunc(s):
	print s
	def inner():
		print "inner"
	inner()


#def main():
	
x = 2
y = 5
map(outerFunc, map(cord, (x+1, x-1, x, x), (y, y, y-1, y+1)))
