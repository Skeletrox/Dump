check = open("Dump.txt", "r")           #Reads the dumped hash text
seen = set()                            #Create a set of already seen elements
unique = True                           #Let's assume the list is unique
for text in check:                      #Check each line of text
    seen.add(text)                      #Add to seen
    for line in check:                  #Read line
        if line in seen:                #If line is already read, duplicate!
            unique = False              #Oh no not unique
    if (unique==False):                 #I officially gave up trying !unque or ~unique pls halp
        print ("Duplicacy exists")      #Oh no duplicate
        quit()                          #Program is useless bye bye
print ("No duplicacies")                #Yay no duplicates
check.close()                           #Avoid leakage of file data pls thx
