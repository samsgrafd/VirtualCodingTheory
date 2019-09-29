import os
import re
import sys

Inall=""
Inb="01"
current=""
binaryCount=0
str1 =""
dslArray1 =[]
dslArray2 =[]
output= "output.txt"
propability= 0
binaryCount= 0
serach= ""
count= 0
f = open("out.txt", 'r')

Inall = f.read()

f.close()

print("this is inputStrBin:" + Inall)	


if Inb in Inall:
                        
        Inb="0"
        print("this is Inall + Inb:" + Inall + Inb)	

if Inb in Inall:
        for i in Inall:

                binaryCount += 1

                current += i

                binaryCount +=1

                if(binaryCount > 0 and current =="0"):

		

                    dslArray1 +="1"

                    dslArray2 += "0"

                    dslArray1 += Inall
	    
                
                        

for i, s in enumerate(dslArray1):

	  			s +="1"
	  			dslArray1[i] = s.strip()

str1 = ''.join(dslArray1)

propability = propability/binaryCount

dslArray1 +=("1",propability,propability, binaryCount)

f = open(output, 'w')

f.write(str1 + str(dslArray1) + str(dslArray2))

f.close()

print(binaryCount)

print(propability)

print(str(dslArray1))

print(str(dslArray2))

print(Inall)

#put in output: line number/s which causes '1' mark
