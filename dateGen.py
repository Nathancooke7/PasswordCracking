Date=open('Dates.txt', 'w')
for x in range(1,10):#single digit month
	for y in range (1,10): #single digit day
		for z in range (1900,2020): #long year
			A= '0'+str(x)+'0'+str(y)+str(z)+'\n'
			Date.write(A)
		for z in range (0,10): #short single digit year
			A= '0'+str(x)+'0'+str(y)+'0'+str(z)+'\n'
			Date.write(A)
		for z in range(11,100):#short double digit year
			A= '0'+str(x)+'0'+str(y)+str(z)+'\n'
			Date.write(A)
	for y in range (11,32): #double digit day
		for z in range (1900,2020): #long year
			A= '0'+str(x)+str(y)+str(z)+'\n'
			Date.write(A)
		for z in range (0,10): #short single digit year
			A= '0'+str(x)+str(y)+'0'+str(z)+'\n'
			Date.write(A)
		for z in range(11,100):#short double digit year
			A= '0'+str(x)+str(y)+str(z)+'\n'
			Date.write(A)
for x in range(11,13):#double digit month
	for y in range (1,10): #single digit day
		for z in range (1900,2020): #long year
			A= '0'+str(x)+'0'+str(y)+str(z)+'\n'
			Date.write(A)
		for z in range (0,10): #short single digit year
			A= '0'+str(x)+'0'+str(y)+'0'+str(z)+'\n'
			Date.write(A)
		for z in range(11,100):#short double digit year
			A= '0'+str(x)+'0'+str(y)+str(z)+'\n'
			Date.write(A)
	for y in range (11,32): #double digit day
		for z in range (1900,2020): #long year
			A= '0'+str(x)+str(y)+str(z)+'\n'
			Date.write(A)
		for z in range (0,10): #short single digit year
			A= '0'+str(x)+str(y)+'0'+str(z)+'\n'
			Date.write(A)
		for z in range(11,100):#short double digit year
			A= '0'+str(x)+str(y)+str(z)+'\n'
