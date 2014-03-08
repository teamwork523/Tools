#!/usr/bin/env python
import sys, math

# convert tabular data into box err bar type (5% median 95%)
# apply to single column with a condition type

def Usage():
    print sys.argv[0] + " data_col cond_col cond true_label header < filepath"

def getMedian(li):
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
    DEL = "\t"
    data = []

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 6:
        Usage()
        sys.exit(1)
    
    data_col = int(sys.argv[1]) - 1
    cond_col = int(sys.argv[2]) - 1
    cond = sys.argv[3]
    
    # read data
    # TODO: change the label if needed
    trueLabel = sys.argv[4]
    falseLabel = "No_" + trueLabel
    condDataMap = {trueLabel:[], falseLabel:[]}

    # check header
    if sys.argv[5] == "y" or sys.argv[5] == "Y":
        header = sys.stdin.readline()

    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split()
        data = 0.0
        condData = None
        try:
            data = float(curData[data_col])
            condData = curData[cond_col]
        except ValueError:
            print >> sys.std, "ValueError detected: " + line

        if eval(str(condData) + cond):
            condDataMap[trueLabel].append(data)
        else:
            condDataMap[falseLabel].append(data)

    # Only need to output true and false label
    labels = [trueLabel, falseLabel]
    for i in range(len(labels)):
        line = labels[i] + DEL + str(i+0.5) + DEL
        # sort data first
        condDataMap[labels[i]].sort()
        sortedData = condDataMap[labels[i]]
        data_len = len(sortedData)
        if data_len >= 2:
            myMedian = getMedian(sortedData)
            myLower = sortedData[int(data_len*0.05)]
            myUpper = sortedData[int(data_len*0.95)]
        else:
            myMedian = 0.0
            myLower = 0.0
            myUpper = 0.0
        line += str(myMedian) + DEL + str(myLower) + DEL + str(myUpper)
        print line.strip()
    
    trueLen = len(condDataMap[trueLabel])
    falseLen = len(condDataMap[falseLabel])
    print >> sys.stderr, ("Delay Ratio is %.6f" % (getMedian(condDataMap[trueLabel]) / \
                          getMedian(condDataMap[falseLabel])))

if __name__ == "__main__":
    main()

