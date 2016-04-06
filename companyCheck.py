import sys

if len(sys.argv)<2:
	sys.exit("Error: Must specify company wordlist file\n")
else:
	print 'checking passwords'
	
#open files
CompanyWord=open(sys.argv[1], 'r')
CompanyMatch=open('Company.txt', 'w')
CustomerList=open('CrackedCustomers.txt', 'r')

#load wordlist into a list
words=[]
for line in CompanyWord:
	words.append(line[:-1])#chops off \n

for line in CustomerList:
	if line=='\n':#not the penultimate line
		break
	splitUp=line.split(':')#[0]=username, [1]=password
	password=splitUp[1].lower()
	password=password[:-1]#chops off \n
	for x in words:
		if password.find(x)>=0:
			CompanyMatch.write(line)
			break

#close files
CompanyMatch.close
CompanyWord.close
CustomerList.close
