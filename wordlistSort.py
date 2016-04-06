import sys

if len(sys.argv)<2:
	sys.exit("Error: Must specify file to sort\n")
else:
	print 'Sorting passwords in file ' + sys.argv[1]

#files to open for writing
MasterList=open(sys.argv[1], "r")
Short=open("ShortPass.txt", "w")
SixDigits=open("6Digits.txt", "w")
LongDigits=open("LongDigits.txt", "w")
SixAlpha=open("6Alpha.txt", "w")
LongAlpha=open("LongAlpha.txt", "w")
SixAlphaNum=open("6AlphaNum.txt", "w")
LongAlphaNum=open("LongAlphaNum.txt", "w")
SixMix=open("6Mix.txt", "w")
LongMix=open("LongMix.txt", "w")

#sort passwords into files by characteristics
for password in MasterList: #each line is a password
	password=password[:-1] #chop off \n
	if len(password)<6: 				#short
		Short.write(password + '\n')
	elif len(password)==6 and password.isdigit(): 	#6 and all numbers
		SixDigits.write(password+ '\n')
	elif password.isdigit(): 			#long and all numbers
		LongDigits.write(password+ '\n')
	elif len(password)==6 and password.isalpha(): 	#6 and all letters
		SixAlpha.write(password+ '\n')
	elif password.isalpha(): 			#long and all letters
		LongAlpha.write(password+ '\n')
	elif len(password)==6 and password.isalnum(): 	#6 and alphanumeric
		SixAlphaNum.write(password+ '\n')
	elif password.isalnum(): 			#long and alphanumeric
		LongAlphaNum.write(password+ '\n')
	elif len(password)==6: 				#6 and includes special char
		SixMix.write(password+ '\n')
	else: 						#long and includes special char
		LongMix.write(password+ '\n')

#close all files
print 'Passwords sorted, closing files.'
MasterList.close()
Short.close
SixDigits.close
LongDigits.close
SixAlpha.close
LongAlpha.close
SixAlphaNum.close
LongAlphaNum.close
SixMix.close
LongMix.close
