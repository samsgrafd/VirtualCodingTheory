# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os

inputStrBin = ""

f = open("svghex.txt", 'r')

inputStrBin = f.read()

output = 0

f.close()
 
"".join(map(chr, int(inputStrBin)))

f = open("model.txt", 'w')

f.write(str(inputStrBin))

f.close()


