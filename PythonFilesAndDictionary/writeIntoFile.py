filename = "squre.txt"
outfile = open(filename, "w")


outfile.write("heloo")
outfile.close()

infile = open(filename, "r")
print(infile.read())
infile.close()
