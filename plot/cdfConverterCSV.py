#!/usr/bin/env python

# convert to CDF format for a csv file

import sys, math

def Usage():
    print sys.argv[0] + " col accurancy header < filepath, where accurancy is in unit of %"

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 4:
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[-1] == "y" or sys.argv[-1] == "Y":
        header = sys.stdin.readline()

    data = []
    index = int(sys.argv[1]) - 1 
    accurancy = float(sys.argv[2])
    DEL = ","
    
    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        if tempData[index] != "":
            data.append(float(tempData[index]))
        line = sys.stdin.readline()
    
    data.sort()
    dataLen = len(data)
    i = 0.0
    while i < 100.0:
        i += accurancy        
        print "%f\t%f" % (i/100.0, data[min(int(i*dataLen/100.0), dataLen-1)])

if __name__ == "__main__":
    main()
