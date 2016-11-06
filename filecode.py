#!/bin/sh/env python3

from random import randint

#Making a global Matrix because it's used in multiple functions. Maybe use a class if we need more security?

Matrix = [[0 for x in range (5)] for y in range (100)]

def makeMatrix():
  global Matrix                           #We are using the global matrix, no need to define another one here
  for i in range (0, 100):
        for j in range (0, 5):
            Matrix[i][j] = randint(0,10)

def hashit (text):
    coder = 47
    lth  = len(text)
    enc = []
    throw = []
    for i in range(0,lth):
        if (text[i] == ' '):
            c = 9
        else:
            c = ord(text[i])
        c = (c^coder)
        if (c != 9):
            enc.append(chr(c))
        else:
            enc.append(' ')

    #   After enc gets the xorcoded value we shall use the generated matrix in order to create the hash string

    for i in range (0, 5):
        out = 0
        for j in range (0, lth):
            out = (out + ord(enc[j])*Matrix[j][i])%94 + 33
        throw.append(chr(out))
    string = ''.join(throw)
    return string

#   The main program. Opens the list of names from Hashlist and writes the names into Dump

inside = open("Hashlist.txt", "r")
outside = open("Dump.txt", "w")
makeMatrix()
for name in inside:
   # print (name)                       //For Debug Purposes
    string2 = hashit(name)
   # print (string2)                    //For Debug Purposes
    outside.write (string2 + "\n")
inside.close()
outside.close()
