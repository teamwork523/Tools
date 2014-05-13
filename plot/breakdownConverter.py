#!/usr/bin/env python

# output the statistics based by categories

import sys, math

def Usage():
    print sys.argv[0] + " category data_cols header < filepath"

def getMedian(li):
    # assume li sorted
    length = len(li)

    if length == 0:
        return None
    elif length == 1:
        return li[0]

    if length % 2 == 0:
        return float(li[int(length / 2)] + li[int(length / 2) - 1]) / 2.0
    else:
        return float(li[int(length / 2)])

def main():
    # delimiter
    DEL = "\t"
    data = []
    total = 0.0

    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[-1] == "y" or sys.argv[-1] == "Y":
        header = sys.stdin.readline()
    
    cat_col = int(sys.argv[1]) - 1
    data_cols = [int(i) - 1 for i in sys.argv[2:-1]]

    # category set
    dataMap = {}

    while True:
        line = sys.stdin.readline()
        if not line: break
        tempData = line.strip().split(DEL)
        category = tempData[cat_col]
        if category not in dataMap:
            dataMap[category] = {}
            for data_tag in data_cols:
                dataMap[category][data_tag] = []
        for data_col in data_cols:
            if float(tempData[data_col]) > 0:
                dataMap[category][data_col].append(float(tempData[data_col]))

    # output result
    # Mean value
    for category in sorted(dataMap.keys()):
        line = str(category) + DEL
        for data_col in sorted(data_cols):
            sortedResult = sorted(dataMap[category][data_col])
            medianValue = getMedian(sortedResult)
            dataLen = len(sortedResult)
            noOutliarData = sortedResult[(int)(dataLen*0.05):(int)(dataLen*0.95)]
            mean = sum(noOutliarData) / len(noOutliarData)
            stderr = math.sqrt(sum([(i - mean)*(i - mean) for i in noOutliarData]) \
                     / len(noOutliarData))
            #line += str(medianValue) + DEL
            line += str(mean) + DEL + str(stderr) + DEL
            #line += str(medianValue) + DEL + str(stderr) + DEL
            """
            if medianValue >= 0:
                line += str(medianValue) + DEL
            else:
                line += str(sortedResult[(int)(0.75*len(sortedResult))]) + DEL
            """
        print line

if __name__ == "__main__":
    main()
