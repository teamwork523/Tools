#!/usr/bin/env python

# generate PMF for each data point

import sys, math

def Usage():
    print sys.argv[0] + " col header < filepath"

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 3:
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[2] == "y" or sys.argv[2] == "Y":
        header = sys.stdin.readline()    

    dataMap = {}
    dataSize = 0.0
    index = int(sys.argv[1]) - 1 
    DEL = "\t"
    
    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        curData = float(tempData[index])
        if curData not in dataMap:
            dataMap[curData] = 0.0
        dataMap[curData] += 1
        dataSize += 1
        line = sys.stdin.readline()
    
    sortedData = sorted(dataMap.keys())
    for data in sortedData:
        print "%f\t%f" % (data, dataMap[data] / dataSize)
        

if __name__ == "__main__":
    main()
