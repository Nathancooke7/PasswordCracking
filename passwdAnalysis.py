

#open files
CustomerList=open('CrackedCustomers.txt', 'r')
Alphacount=open('Alphacount.txt', 'w')
PolicyPass=open('Policy Pass.txt', 'w')
Same=open('Password=username.txt', 'w')
Most=open('Most first.txt', 'w')

blacklist=['fashion','passw','p@ssw','yellow','blue','purple','june','august','september','october','november','december','love','ball','shop','poo','star','abc','123','butter','dance','monkey','jesus','letmein','sunshine','princess','qwerty','welcome','flower','hello','scooter','tiger','ginger','magnolia','blondie','summer']
bl=0
count={}
special=('!','@','#','$','%','^','&','*','(',')','-','=','_','+','<',',','>','.','/','?')

for line in CustomerList:
	if line=='\n':#not the penultimate line
		break

	splitUp=line.split(':')#[0]=username, [1]=password
	if splitUp[1] in count:
		count[splitUp[1]]=count[splitUp[1]]+1
	else:
		count[splitUp[1]]=1

	#check if password should be blacklisted
	password=splitUp[1].lower()
	for word in blacklist:
		if password.find(word)>=0: #>=0 because it might start with searchstring
			bl+=1
			break

	#check if username in password, don't split up so it checks domain too, match 4gram
	username=splitUp[0].lower()
	N = 4
	grams = [username[i:i+N] for i in xrange(len(username)-N)]
	for gram in grams:#every 4gram in username
		if password.find(gram)>=0:
			Same.write(splitUp[0]+' : '+splitUp[1])
			break

print 'should be blacklisted:', bl

#sort by count
frequency=[]
stop=0
for x in sorted(count, key=count.get):#sorts least to greatest
	y=x[:-1]
	frequency.append(y)
for w in reversed(frequency):#reverses to greatest to least
	A = w+' = '+str(count[w+'\n'])+'\n'
	Most.write(A)

#sort by alphabet
for x in sorted(count.items()): #x[password, count]
	y=x[0]
	z=y[:-1]#chop off \n
	A=z+' = '+str(count[y])+'\n'
	Alphacount.write(A)
	#check if cracked password would pass new policy
	for r in special:
		if z.find(r)>0:
			if len(z)>7 and any(j.isupper() for j in z) and any(j.islower() for j in z) and any(j.isdigit() for j in z):
				PolicyPass.write(y)



#close files
CustomerList.close
Alphacount.close
PolicyPass.close
Same.close
Most.close
