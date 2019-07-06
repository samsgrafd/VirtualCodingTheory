// encoding=utf8
var sys = require('sys');
reload(sys);
sys.setdefaultencoding('utf-8');

var os = require('os');

inputStrBin = '';

f = open('svghex.txt', 'r');

inputStrBin = f.read();

output = 0;

f.close();

''.join(map(chr, Number(inputStrBin)));

f = open('model.txt', 'w');

f.write(str(inputStrBin));

f.close();
