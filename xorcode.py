#!/bin/sh/env python3

from random import randint
text = input("Enter string to encrypt: ")
coder = 47
coder = int(coder)
lth  = len(text)
Matrix = [[0 for x in range (5)] for y in range (lth)] 
for i in range (0, lth):
    for j in range (0, 5):
        Matrix[i][j] = randint(0,10)
enc = []
for i in range(0,lth):
	if (text[i] == ' '):
		c = 9			#Using ASCII of tab because irl web inputs won't accept tabs while you type your password lol
	else:
		c = ord(text[i])
	c = (c^coder)
	if (c != 9):
		enc.append(chr(c))
	else:
	 	enc.append(' ')
for i in range(0,lth):
	print (enc[i], end='')
print ("")
print ("The hash table is:")
for i in range (0, lth):
    for j in range (0, 5):
        print (Matrix[i][j], end=' ')
    print ('')
print ("The hashed value for " + text + " is: ", end='' )
for i in range (0, 5):
    out = 0
    for j in range (0, lth):
        out = (out + ord(enc[j])*Matrix[j][i])%128
        if out < 33:
            out += 33
    print (chr(out), end='')
print ('')
