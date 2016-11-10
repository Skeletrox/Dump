import math

infile = open("bank1.cc", "r")
outfile = open("bank2.cc", "w")
i=0
for line in infile:
	i=i+1
	if i==1:
		val = 2
	else:
		val = int(math.log(i/2, 10) + 2)
	line2 = line[val:]
	outfile.write (line2)

