// encoding=utf8
var sys = require('sys');
reload(sys);
sys.setdefaultencoding('utf-8');

var os = require('os');

inputStrBin = '';

f = open('svgilhex.txt', 'r');

inputStrBin = f.read();

output = '';

f.close();

output = (inputStrBin, 'utf8');

f = open('model.txt', 'w');

f.write(str(output));

f.close()
