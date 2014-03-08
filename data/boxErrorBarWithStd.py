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
    print sys.argv[0] + " cat_col(x) data_col(y) header < filepath"

def main():
    DEL = "\t"
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 4:
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[3] == "y" or sys.argv[3] == "Y":
        header = sys.stdin.readline()

    cat_col = int(sys.argv[1]) - 1
    data_col = int(sys.argv[2]) - 1
    
    dataMap = {}

    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split()
        cat = curData[cat_col]
        data = 0.0
        try:
            data = float(curData[data_col])
        except ValueError:
            print >> sys.std, "ValueError detected: " + line
        if cat not in dataMap:
            dataMap[cat] = []
        dataMap[cat].append(data)
    
    # output the result
    for cat in dataMap.keys():
        sortedData = sorted(dataMap[cat])
        data_len = len(sortedData)
        noOutlierData = sortedData[int(data_len*0.05):int(data_len*0.95)]
        totalSum = sum(sortedData)
        mean = totalSum*1.0/len(sortedData)
        diff_sum = sum([(data - mean) * (data - mean) for data in noOutlierData])
        std = math.sqrt(diff_sum/len(sortedData))
        print str(cat) + DEL + str(mean) + DEL + \
              str(mean - std) + DEL + \
              str(mean + std)

if __name__ == "__main__":
    main()
