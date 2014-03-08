#!/usr/bin/env python

import sys, math

def Usage():
    print sys.argv[0] + " col_num header DEL < filepath"

def main():
    data = []

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 4:
        Usage()
        sys.exit(1)

    col_num = int(sys.argv[1])
    # delimiter
    DEL = sys.argv[3]

    # check header
    if sys.argv[2] == "y" or sys.argv[2] == "Y":
        header = sys.stdin.readline()

    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        curData = tempData[col_num - 1]
        data.append(curData)
        line = sys.stdin.readline()
    
    print "Unique of the value is %d" % (len(set(data)))    

if __name__ == "__main__":
    main()
