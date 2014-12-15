def replaceAt(origin, newname):
	f = open(origin)
	g = open(newname, 'a')
	for line in f:
		g.write(line.replace(" at ", "@"))

def check(filename):
	f = open(filename)
	x = 0
	for line in f:
		if(line.count("@") == 1):
			x += 1
	print x