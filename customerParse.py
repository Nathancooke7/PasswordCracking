import sys

if len(sys.argv)<2:
	sys.exit("Error: Must specify file to sort\n")
	
#open files
CustAll = open(sys.argv[1], 'r')
PassList = open('CustomerPasswordHashes.txt', 'w')

#parse customer csv for username and passHash
for line in CustAll:
	#create dictionary from line
	parseThis=line.split(',')
	if parseThis[0].find('@')>=0:#checks is first element is email address
		parsed={'username':'','passhash':'','salt':''}
		parsed['username']=parseThis[0]
		hashSalt=parseThis[14]#hash:salt
		if hashSalt=='':
			parsed['passhash']='go look this up'#might have the wrong index
		else:
			splitUp=hashSalt.split(':')
			parsed['passhash']=splitUp[0]
			parsed['salt']=splitUp[1]
		#create string with username, passHash and salt formatted for john the ripper
		writeThis=parsed['username']+':$dynamic_61$'+parsed['passhash']+'$'+parsed['salt']#dynamic_1017=md5(s.p); dynamic_61=sha256(s.p)
		#write string to file
		PassList.write(writeThis+'\n')

#close files
CustAll.close
PassList.close
