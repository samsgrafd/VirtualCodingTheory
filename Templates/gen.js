#!/usr/bin/env python;
/*
    python autobot.py

    TODO: Add usage information here.
 */
var jiphy = require('jiphy');

jiphy.to.javascript(python_code);
jiphy.to.python(javascript_code);

var sys = require('sys');

from argparse var ArgumentParser = require('ArgumentParser');

function execute_autobot(name, classname, methodname) {
    /*  TODO: Add docstring here.  */
    // TODO: Add or delete code here.
    // Dump all passed argument values.

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
    parser.add_argument(action='store', dest='name', help='TODO:');
    parser.add_argument(action='store', dest='classname', help='TODO:');
    parser.add_argument(action='store', dest='methodname', help='TODO:');

    // Parse the command line.
    arguments = parser.parse_args(args=argv);
    name = arguments.name;
    classname = arguments.classname;
    methodname = arguments.methodname;

    status = 0;
    try {
        f = open(arguments.name, 'w');
	f.write( '%YAML 1.1 %TAG !u! tag:unity3d.com,2011:\r\n' +
	'--- !u!1001 &100100000\r\n' +
	'Prefab:\r\n' +
	'  m_ObjectHideFlags: 1\r\n' +
	'  serializedVersion: 2\r\n' +
	'  m_Modification:\r\n' +
	'    m_TransformParent: {fileID: 0}\r\n' +
	'    m_Modifications: []\r\n' +
	'    m_RemovedComponents: []\r\n' +
	'  m_SourcePrefab: {fileID: 0}\r\n' +
	'  m_RootGameObject: {fileID: 1664241225732296}\r\n' +
	'  m_IsPrefabAsset: 1\r\n' +
	'--- !u!1 &1664241225732296\r\n' +
	'GameObject:\r\n' +
	'  m_ObjectHideFlags: 0\r\n' +
	'  m_CorrespondingSourceObject: {fileID: 0}\r\n' +
	'  m_PrefabInternal: {fileID: 100100000}\r\n' +
	'  serializedVersion: 6\r\n' +
	'  m_Component:\r\n' +
	'  - component: {fileID: 4037147750317178}\r\n' +
	'  m_Layer: 0\r\n' +
	'  m_Name: GameObject\r\n' +
	'  m_TagString: Untagged\r\n' +
	'  m_Icon: {fileID: 0}\r\n' +
	'  m_NavMeshLayer: 0\r\n' +
	'  m_StaticEditorFlags: 0\r\n' +
	'  m_IsActive: 1\r\n' +
	'--- !u!4 &4037147750317178\r\n' +
	'Transform:\r\n' +
	'  m_ObjectHideFlags: 1\r\n' +
	'  m_CorrespondingSourceObject: {fileID: 0}\r\n' +
	'  m_PrefabInternal: {fileID: 100100000}\r\n' +
	'  m_GameObject: {fileID: 1664241225732296}\r\n' +
	'  m_LocalRotation: {x: 0, y: 0, z: 0, w: 1}\r\n' +
	'  m_LocalPosition: {x:\r\n' + '\r' +
    format(arguments.name) +
         'y:\r\n ' +  '\r' +
	format(arguments.classname)+
         'z: \r\n ' + '\r' +
	format(arguments.methodname)+
	'}'+
	'  m_LocalScale: {x: 1, y: 1, z: 1}\r\n' +
	'  m_Children: []\r\n' +
	'  m_Father: {fileID: 0}\r\n' +
	'  m_RootOrder: 0\r\n' +
	'  m_LocalEulerAnglesHint: {x: 0, y: 0, z: 0}')
	f.close();
        execute_autobot(name, classname, methodname);
    } catch ( ValueError as value_error) {
        console.log value_error;
        status = -1;
    } catch ( EnvironmentError as environment_error) {
        console.log environment_error;
        status = -1;
    return status;
    }
if (__name__ == '__main__') {
    sys.exit(main());

}
}
