NumFile=open("Numbers.txt", "w")
for x in range(0,1000000):
	NumFile.write(str(x)+'\n')
NumFile.close
