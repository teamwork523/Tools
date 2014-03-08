#!/usr/bin/env python
import sys, math

# convert three dimensional data into a column wise data

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
    print sys.argv[0] + " label_col(x) data_col(y) category(z) header < filepath"

def main():
    DEL = "\t"
    data = []

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 5:
        Usage()
        sys.exit(1)

    pre_defined_label_group = ["Normal", "DCH", "FACH+DCH"]

    label_col = int(sys.argv[1]) - 1
    data_col = int(sys.argv[2]) - 1
    cat_col = int(sys.argv[3]) - 1

    # check header
    if sys.argv[4] == "y" or sys.argv[4] == "Y":
        header = sys.stdin.readline()

    dataMap = {}
    label_set = set()

    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split()
        label = curData[label_col]
        label_set.add(label)
        category = curData[cat_col]
        data = 0.0
        try:
            data = float(curData[data_col])
        except ValueError:
            print >> sys.stderr, "ValueError detected: " + line

        if not dataMap.has_key(label):
            dataMap[label] = {}
        if not dataMap[label].has_key(category):
            dataMap[label][category] = []

        dataMap[label][category].append(data)

    sortedLabel = sorted(label_set)
    for i in range(len(label_set)):
        curLabel = sortedLabel[i]
        line = curLabel + DEL + str(i+0.5) + DEL

        for category in pre_defined_label_group:
            if dataMap[curLabel].has_key(category):
                data_len = len(dataMap[curLabel][category])
                sortedData = sorted(dataMap[curLabel][category])
                myMedian = getMedian(sortedData)
                myLower = sortedData[int(data_len*0.05)]
                myUpper = sortedData[int(data_len*0.95)]
            else:
                myMedian = 0.0
                myLower = 0.0
                myUpper = 0.0
            line += str(myMedian) + DEL + str(myLower) + DEL + str(myUpper) + DEL

        print line.strip()

    # print the median latency difference
    print >> sys.stderr, "Host" + DEL + DEL.join(pre_defined_label_group)
    for label in sortedLabel:
        line = label + DEL
        normalMedian = getMedian(sorted(dataMap[label][pre_defined_label_group[0]]))
        line += str(normalMedian) + DEL
        for category in pre_defined_label_group[1:]:
            if dataMap[label].has_key(category):
                line += str(getMedian(sorted(dataMap[label][category])) - normalMedian) + DEL
            else:
                line += "N/A" + DEL
        print >> sys.stderr, line

if __name__ == "__main__":
    main()


