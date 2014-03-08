#!/usr/bin/env python
import sys, math

# convert the data into box error bar plot based on 

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

def Usage():
    print sys.argv[0] + " cat_col(z) data_col(y) x_label categories_list header < filepath"

def main():
    DEL = "\t"

    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[-1] == "y" or sys.argv[-1] == "Y":
        header = sys.stdin.readline()

    cat_col = int(sys.argv[1]) - 1
    data_col = int(sys.argv[2]) - 1
    x_label = sys.argv[3]
    cat_list = sys.argv[4:-1]

    dataMap = {}

    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split()
        category = curData[cat_col]
        if category not in cat_list:
            continue
        data = 0.0
        try:
            data = float(curData[data_col])
        except ValueError:
            print >> sys.stderr, "ValueError detected: " + line

        if not dataMap.has_key(category):
            dataMap[category] = []

        dataMap[category].append(data)

    # output result
    line = x_label + DEL
    for category in cat_list:
        sortedData = sorted(dataMap[category])
        dataLen = len(sortedData)
        line += str(getMedian(sortedData)) + DEL
        line += str(sortedData[(int)(0.05*dataLen)]) + DEL
        line += str(sortedData[(int)(0.95*dataLen)]) + DEL

    print line.strip()

if __name__ == "__main__":
    main()










