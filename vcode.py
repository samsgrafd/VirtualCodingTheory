import os
import re
import sys
import csv



Inall=""
Inb="01"
all1 = ""
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






Onepluszero = set()
oneone = set()
zeroandone = set()


f = open("in.txt",'r')
reader = csv.reader(f)

for row in reader:
        if len(row)- 1 >= 0 and len(row) - 1 < len(row):
                customer = (row[0], 1)
        if len(row) - 1 >= 0 and len(row) -1 < len(row):
                category = (row[0], 1)
        if Inall in row:
                Onepluszero.add(customer)
        if "1" + Inall in row:
                oneone.add(customer)
        if "11" + Inall in row:
                zeroandone.add(customer)
        print(row)                
f.close()

print( "%s customers have purchased shoes" % len(Onepluszero))
print ("%s customers have purchased belts" % len(oneone))
print ("%s customers have purchased shoes but not belts" % len(Onepluszero - oneone))
print ("%s customers have purchased shoes and belts" % len(Onepluszero &oneone))
print ("%s customers have purchases shoes and shirts" % len(oneone & Onepluszero))
print ("%s customers have purchased shoes, belts and shirts" % len(Onepluszero & oneone & zeroandone))
print ("The following customers are our most valued. They have purchased shoes & belts & shirts:")
for customer in Onepluszero & oneone & zeroandone:
        print( customer)





