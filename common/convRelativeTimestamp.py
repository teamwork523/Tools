#!/usr/bin/env python

# convert a column's unix time into relative timestamp
import sys

def Usage():
    print sys.argv[0] + " time_col divider header < filepath"

def main():
    DEL = "\t"
    
    # check header
    if sys.argv[-1] == "y" or sys.argv[-1] == "Y":
        header = sys.stdin.readline()

    time_col = int(sys.argv[1]) - 1
    divider = int(sys.argv[2]) - 1
    minTime = None
    dataByLine = []

    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split(DEL)
        curData[time_col] = float(curData[time_col])
        if minTime == None or \
           curData[time_col] < minTime:
            minTime = curData[time_col]
        dataByLine.append(curData)

    # reassign timestamp
    for data in dataByLine:
        data[time_col] = str((data[time_col] - minTime) / divider)
        print DEL.join(data)

if __name__ == "__main__":
    main()
