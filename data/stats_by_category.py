#!/usr/bin/env python

# output the statistics based by categories

import sys, math

def Usage():
    print sys.argv[0] + " data_col cat_col header < filepath"

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

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 4:
        Usage()
        sys.exit(1)

    data_col = int(sys.argv[1]) - 1
    cat_col = int(sys.argv[2]) - 1

    # check header
    if sys.argv[3] == "y" or sys.argv[3] == "Y":
        header = sys.stdin.readline()

    # category set
    dataMap = {}
    cat_set = set()

    while True:
        line = sys.stdin.readline()
        if not line: break
        tempData = line.strip().split()
        try:
            curData = float(tempData[data_col])
        except ValueError:
            print line
        curCat = tempData[cat_col]
        cat_set.add(curCat)
        if not dataMap.has_key(curCat):
            dataMap[curCat] = []

        dataMap[curCat].append(curData)

    totalLen = float(sum([len(x) for x in dataMap.values()]))

    # output result
    for category in cat_set:
        data_len = float(len(dataMap[category]))
        sortedData = sorted(dataMap[category])
        noOutlierData = sortedData[int(data_len*0.05):int(data_len*0.95)]
        totalSum = sum(sortedData)
        #totalSum = sum(noOutlierData)
        mean = totalSum*1.0/len(sortedData)
        #mean = totalSum*1.0/len(noOutlierData)
        diff_sum = sum([(data - mean) * (data - mean) for data in noOutlierData])
        std = math.sqrt(diff_sum/len(sortedData))
        #std = math.sqrt(diff_sum/len(noOutlierData))
        result = []
        result.append(sortedData[0])
        result.append(sortedData[int(data_len*0.05)])
        result.append(sortedData[int(data_len*0.25)])
        result.append(getMedian(sortedData))
        result.append(sortedData[int(data_len*0.75)])
        result.append(sortedData[int(data_len*0.95)])
        result.append(sortedData[-1])
        
        print str(category) + DEL + str(data_len) + DEL + \
              "%.3f" % (data_len * 100 / totalLen) + "%" + \
              DEL + str(result) + DEL + str(mean) + \
              DEL + str(std)
        

if __name__ == "__main__":
    main()
