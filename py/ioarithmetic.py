fin = open("file.in")
fout = open("file.out")

firstnum = int(fin.readline())
secondnum = int(fin.readline())

fout.write(str(firstnum + secondnum))
fout.close()
