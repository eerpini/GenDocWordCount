#!/usr/bin/python

import os 
import sys

def list_dir(path, level=1):
    for f in os.listdir(path):
        file = os.path.join(path, f)
        if os.path.isfile(file):
            for i in range(1,level):
                print "|    ",
            print "|--- "+os.path.basename(file)
        elif os.path.isdir(file):
            for i in range(1,level):
                print "|    ",
            print "|--- ",
            print "\033[1;36m%s\033[0;39m" % os.path.basename(file)
            list_dir(file, level+1)
        else:
            print "Trying to print"+file+"from the directory"+os.getcwd()

if __name__ == '__main__':
    list_dir(sys.argv[1])
        
        

