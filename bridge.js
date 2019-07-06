#!/usr/bin/env python;
/*
    python bridge.py

    TODO: Add usage information here.
 */
var sys = require('sys');
// TODO: Uncomment or add imports here.
#var os = require('os');
#var re = require('re');
#var time = require('time');
#var subprocess = require('subprocess');
var random = require('random');
from argparse var ArgumentParser = require('ArgumentParser');

function execute_bridge( pos1, pos2, pos3) {
    /*  TODO: Add docstring here.  */
    // TODO: Add or delete code here.
    // Dump all passed argument values.

    console.log 'pos1 = {0}'.format(repr(pos1));
    console.log 'pos2 = {0}'.format(repr(pos2));
    console.log 'pos3 = {0}'.format(repr(pos3));
    return 0;
}
// Start of main program.
function main(argv=null) {
    // Initialize the command line parser.
    parser = ArgumentParser(description='TODO: Text to display before the argument help.',
                            epilog='Copyright (c) 2018 TODO: your-name-here.',
                            add_help=true,
                            argument_default=null, // Global argument default
                            usage=__doc__);

    parser.add_argument(action='store', dest='pos1', help='TODO:');
    parser.add_argument(action='store', dest='pos2', help='TODO:');
    parser.add_argument(action='store', dest='pos3', help='TODO:');
    // Parse the command line.
    arguments = parser.parse_args(args=argv);

    pos1 = arguments.pos1;
    pos2 = arguments.pos2;
    pos3 = arguments.pos3;
    status = 0;
    try {

        globalrange =50;
    }
}

        p1=0;
        p2=0;
        p3=0;
        p1= random.randint(0,globalrange);
        p2= random.randint(0,globalrange);
        p3= random.randint(0,globalrange);
        f = open('parameters.bat', 'w');
        f.write('python gen.py' + ' '+ format(p1)+ ' ' + format(p2) + ' ' + format(p3));
        f.close();
        execute_bridge(pos1, pos2, pos3);
    } catch ( ValueError as value_error) {
        console.log value_error;
        status = -1;
    } catch ( EnvironmentError as environment_error) {
        console.log environment_error;
        status = -1;
    return status;

if (__name__ == '__main__') {
    sys.exit(main());

}
