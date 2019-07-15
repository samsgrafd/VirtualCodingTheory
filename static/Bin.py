import sys
import os
dslArray1 = []
dslArray2 = []
inputStrBin = ""
binaryCount = 0
propability = 1 
output = ""
output = "out.txt";
f = open("in.txt", 'r')
inputStrBin = f.read()
f.close()
print("this is inputStrBin:" + inputStrBin)	
	
binaryCount = 0 
current = ""	
	
for i in inputStrBin:
	binaryCount += 1
	current += i
	binaryCount +=1
	if(binaryCount > 0 and current =="2 "):
		
	    dslArray1 +="1"
	    dslArray2 += "0"
	    dslArray1 += inputStrBin
propability = propability/binaryCount
dslArray1 +=("1",propability,propability)
f = open(output, 'w')
f.write(str(dslArray1) + str(dslArray2))
f.close()
print(binaryCount)
print(propability)
print(str(dslArray1))
print(str(dslArray2))
print(inputStrBin)
	
	
	
	
