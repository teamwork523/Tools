#!/usr/bin/env python

# convert to histogram

import sys, math

def hist(x, width):
    return width*math.floor(x/width)+width/2.0

def Usage():
    print sys.argv[0] + " data_col min max interval header < filepath"

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 6:
        Usage()
        sys.exit(1)
    
    # check header
    if sys.argv[-1] == "y" or sys.argv[-1] == "Y":
        header = sys.stdin.readline()

    histMap = {}
    data_col = int(sys.argv[1]) - 1 
    dataMin = float(sys.argv[2])
    dataMax = float(sys.argv[3])
    interval = float(sys.argv[4])

    DEL = "\t"
    width = (dataMax - dataMin) / interval
    
    while True:
        line = sys.stdin.readline()
        if not line: break
        tempData = line.strip().split(DEL)
        curData = 0.0
        try:
            curData = float(tempData[data_col]) 
        except ValueError:
            print >> sys.stderr, "ERROR: invalid float number at " + line
        histValue = hist(curData, width)
        if histValue not in histMap:
            histMap[histValue] = 0
        histMap[histValue] += 1
    
    sortedHistValue = sorted(histMap.keys())
    for data in sortedHistValue:
        print str(data) + DEL + str(histMap[data])
        

if __name__ == "__main__":
    main()
