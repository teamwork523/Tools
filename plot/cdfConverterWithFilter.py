#!/usr/bin/env python

# extract the column with Keyword

import sys, math

def Usage():
    print sys.argv[0] + " col accurancy header filter_col keywords < filepath, where accurancy is in unit of %"

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) < 6:
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[3] == "y" or sys.argv[3] == "Y":
        header = sys.stdin.readline()
    
    data = {}
    dataLen = {}
    dataIndex = int(sys.argv[1]) - 1
    filter_col = int(sys.argv[4]) - 1
    keywords = sys.argv[5:]
    for kw in keywords:
        data[kw] = []
        dataLen[kw] = 0
    accurancy = float(sys.argv[2])
    DEL = "\t"

    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        curKey = tempData[filter_col]
        if curKey in keywords:
            data[curKey].append(float(tempData[dataIndex]))
        line = sys.stdin.readline()
    
    for kw in keywords:
        data[kw].sort()
        dataLen[kw] = len(data[kw])
    
    i = 0.0
    while i < 100.0:
        i += accurancy
        line = str(float(i/100.0)) + DEL
        for kw in keywords:
            line += str(data[kw][min(int(i*dataLen[kw]/100.0), dataLen[kw]-1)]) + DEL
        print line
        

if __name__ == "__main__":
    main()
