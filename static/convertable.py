inputStrBin = ""
f = open("2.txt", 'r')
inputStrBin = f.read()
f.close()
	
binaryCount = 0 
current = ""
for i in inputStrBin:
	binaryCount += 1
	current += i
	binaryCount +=1

propability = propability/binaryCount