#!/usr/bin/env python
"""
    python filledBin.py

    TODO: Add usage information here.
"""
import sys
# TODO: Uncomment or add imports here.
#import os
#import re
#import time
#import subprocess
from argparse import ArgumentParser

def execute_filledBin(arg1, arg2):
    """ TODO: Add docstring here. """
    # TODO: Add or delete code here.
    # Dump all passed argument values.
    print ('arg1 = {0}'.format(repr(arg1)))
    print ('arg2 = {0}'.format(repr(arg2)))
    return 0

# Start of main program.
def main(argv=None):
    # Initialize the command line parser.
    parser = ArgumentParser(description='TODO: Text to display before the argument help.',
                            epilog='Copyright (c) 2019 TODO: your-name-here.',
                            add_help=True,
                            argument_default=None, # Global argument default
                            usage=__doc__)
    parser.add_argument(action='store', dest='arg1', help='TODO:')
    parser.add_argument(action='store', dest='arg2', help='TODO:')
    # Parse the command line.
    arguments = parser.parse_args(args=argv)
    arg1 = arguments.arg1
    arg2 = arguments.arg2
    status = 0
    try:
	

        f = open(arguments.arg1, 'w')
        f.write("import sys\r\n" +
"import os\r\n" +
"dslArray1 = []\r\n" +
"dslArray2 = []\r\n" +
"inputStrBin = \"\"\r\n" +
"str1 = \"\"\r\n" +
"binaryCount = 0\r\n" +
"propability = 1 \r\n" +
"output = \"\"\r\n" +
"output = \"out2.txt\";\r\n" +
"f = open(\"2.txt\", 'r')\r\n" +
"inputStrBin = f.read()\r\n" +
"f.close()\r\n" +
"print(\"this is inputStrBin:\" + inputStrBin)	\r\n" +
"	\r\n" +
"binaryCount = 0 \r\n" +
"current = \"\"	\r\n" +
"s = \"\"	\r\n" +
"	\r\n" +
"for i in inputStrBin:\r\n" +
"	binaryCount += 1\r\n" +
"	current += i\r\n" +
"	binaryCount +=1\r\n" +
"	if(binaryCount > 0 and current ==" + format(arguments.arg2) + "):\r\n" +
"		\r\n" +
"	    dslArray1 +=\"1\"\r\n" +
"	    dslArray2 += \"0\"\r\n" +
"	    dslArray1 += inputStrBin\r\n" +
"for i, s in enumerate(dslArray1):\r\n" +
"	  			s +=\"1\"\r\n" +
"                               dslArray1[i] = s.strip()\r\n" +
"str1 = ''.join(dslArray1)\r\n" +
"propability = propability/binaryCount\r\n" +
"dslArray1 +=(\"1\",propability,propability)\r\n" +
"f = open(output, 'w')\r\n" +
"f.write(str1 + str(dslArray1) + str(dslArray2))\r\n" +
"f.close()\r\n" +
"print(binaryCount)\r\n" +
"print(propability)\r\n" +
"print(str(dslArray1))\r\n" +
"print(str(dslArray2))\r\n" +
"print(inputStrBin)\r\n" +
"	\r\n" +
"	\r\n" +
"	\r\n" +
"	\r\n")
        f.close()

        execute_filledBin(arg1, arg2)
    except ValueError as value_error:
        print (value_error)
        status = -1
    except EnvironmentError as environment_error:
        print (environment_error)
        status = -1
    return status

if __name__ == "__main__":
    sys.exit(main())
