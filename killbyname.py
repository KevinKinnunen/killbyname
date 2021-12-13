#!/usr/bin/python3
#!/usr/bin/env python3

from kbnmodule import *
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-n', '--name', type=str, metavar='', help='Close program using name.')
parser.add_argument('-id', '--procid', type=int, metavar='', help='Close program using pid.')
parser.add_argument('-i', '--pinfo', type=str, metavar='', help='Get process information.')
args = parser.parse_args()

##FIXA HÄR :(
##import en module, skapa en klass, därefter klar!

if __name__ == '__main__':
    objOfMethods = Methods
    if (args.name):
        print(objOfMethods.CloseProcessName(args.name))
    elif (args.procid):
        print(objOfMethods.CloseProcessPid(args.procid))
    elif (args.pinfo):
        print(objOfMethods.GetProcessInfo(args.pinfo))

