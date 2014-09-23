def removeEndSpaces(s):
	if(len(s) > 0):
		while(s[len(s)-1] == ' ' or s[len(s)-1] == '\n'):
			s = s[:-1]
	return s
#Removes the spaces and newlines at the end of a string.  
def removeInsideSpaces(s):
	#removes all spaces before a comma
	i = 0
	while(i < len(s)-1):
		if(s[i] == ' ' and s[i+1] == ','):
			s = s[:i] + s[i+1:]
			i = 0
		else:
			i+= 1
	return s

def csvChange(origin, newName):
	f = open(origin)
	g = open(newName, 'a')
	for line in f:
		g.write(removeInsideSpaces(removeEndSpaces(line)) + '\n')

def addComma(origin, newName):
	f = open(origin)
	g = open(newName, 'a')
	for line in f:
		i = 0
		counter = 0
		while(i < len(line)):
			if(line[i] == ','):
				counter+= 1
			i+= 1

			if counter == 9:
				g.write(line[:i] + '"' + line[i:])
				break
def addComma2(origin, newName):
	f = open(origin)
	g = open(newName, 'a')
	for line in f:
		i = 0
		counter = 0
		while(i < len(line)):
			if(line[i] == ','):
				counter+= 1
			i+= 1

			if counter == 9:
				g.write(line[:i-1] + '"' + line[i-1:])
				break
