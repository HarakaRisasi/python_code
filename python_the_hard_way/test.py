from sys import argv
script, filename = argv
target = open(filename, 'w')
target.truncate()
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
target.close()
