import csv

f = open("sales.csv",'rt')
reader = csv.reader(f)
shoes = set()
belts = set()
shirts = set()
for row in reader:
        customer = (row[0],row[1])
        category = row[0]
        if category == "Region":
                shoes.add(customer)
        if category == "Country":
                belts.add(customer)
        if category == "Item":
                shirts.add(customer)
f.close()



print( "%s customers have purchased shoes" % len(shoes))
print( "%s customers have purchased belts" % len(belts))
print( "%s customers have purchased shoes but not belts" % len(shoes - belts))
print( "%s customers have purchased shoes and belts" % len(shoes & belts))
print( "%s customers have purchases shoes and shirts" % len(shoes & shirts))
print( "%s customers have purchased shoes, belts and shirts" % len(shoes & belts & shirts))
print( "The following customers are our most valued. They have purchased shoes & belts & shirts:")
for customer in shoes & belts & shirts:
        print(customer)

a = ( "%s customers have purchased shoes" % len(shoes))
b = ( "%s customers have purchased belts" % len(belts))
c = ( "%s customers have purchased shoes but not belts" % len(shoes - belts))
d = ( "%s customers have purchased shoes and belts" % len(shoes & belts))
e =( "%s customers have purchases shoes and shirts" % len(shoes & shirts))
f1 =( "%s customers have purchased shoes, belts and shirts" % len(shoes & belts & shirts))
g =( "The following customers are our most valued. They have purchased shoes & belts & shirts:")
f = open('static/outbins.csv', 'w')
f.write(str(a) + str(b) + str(c) + str(d) + str(e) + str(f1) + str(g))
f.close()
print(a)