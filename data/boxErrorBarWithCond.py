#!/usr/bin/env python
import sys, math

# convert excel type of data into box err bar (5% median 95%)

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
    print sys.argv[0] + " label_col(x) data_col(y) cond_col(z) cond header < filepath"

def main():
    DEL = "\t"
    data = []
    pre_defined_label_group = ["PCH", "FACH", "DCH",\
                               "PCH_TO_FACH", "FACH_TO_DCH",\
                               "DCH_TO_FACH", "FACH_TO_PCH"]

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 6:
        Usage()
        sys.exit(1)
    
    label_col = int(sys.argv[1]) - 1
    data_col = int(sys.argv[2]) - 1
    cond_col = int(sys.argv[3]) - 1
    cond = sys.argv[4]

    # check header
    if sys.argv[5] == "y" or sys.argv[5] == "Y":
        header = sys.stdin.readline()
        
    
    # read data
    condTrueDataMap = {}
    condFalseDataMap = {}

    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split()
        label = curData[label_col]
        data = 0.0
        condData = 0.0
        try:
            data = float(curData[data_col])
            condData = curData[cond_col]
        except ValueError:
            print >> sys.std, "ValueError detected: " + line

        if eval(str(condData) + cond):
            dataMap = condTrueDataMap
        else:
            dataMap = condFalseDataMap

        if dataMap.has_key(label):
            dataMap[label].append(data)
        else:
            dataMap[label] = [data]

    # generate the boxErrorBar plot result
    sortedLabel = sorted(condTrueDataMap.keys())

    for i in range(len(pre_defined_label_group)):
        curLabel = pre_defined_label_group[i]
        line = curLabel + DEL + str(i+0.5) + DEL
        # true data
        if condTrueDataMap.has_key(curLabel):
            data_len = len(condTrueDataMap[curLabel])
            condTrueDataMap[curLabel].sort()
            sortedData = condTrueDataMap[curLabel]
            myMedian = getMedian(sortedData)
            myLower = sortedData[int(data_len*0.05)]
            myUpper = sortedData[int(data_len*0.95)]
        else:
            myMedian = 0.0
            myLower = 0.0
            myUpper = 0.0
        line += str(myMedian) + DEL + str(myLower) + DEL + str(myUpper) + DEL
        # false data
        if condFalseDataMap.has_key(curLabel):
            data_len = len(condFalseDataMap[curLabel])
            condFalseDataMap[curLabel].sort()
            sortedData = condFalseDataMap[curLabel]
            myMedian = getMedian(sortedData)
            myLower = sortedData[int(data_len*0.05)]
            myUpper = sortedData[int(data_len*0.95)]
        else:
            myMedian = 0.0
            myLower = 0.0
            myUpper = 0.0
        line += str(myMedian) + DEL + str(myLower) + DEL + str(myUpper) + DEL
        print line.strip()

    # print the proportion statistics into standard error
    totalTrueDataLen = sum([len(i) for i in condTrueDataMap.values()])
    totalFalseDataLen = sum([len(i) for i in condFalseDataMap.values()])
    totalLen = float(totalTrueDataLen + totalFalseDataLen)
    print >> sys.stderr, "Type" + DEL + DEL.join(pre_defined_label_group) + DEL + "Total"
    truePercentLine = "True Ratio" + DEL
    falsePercentLine = "False Ratio" + DEL
    delayRatioLine = "Median Slow Rate (PRACH/normal)" + DEL
    delayIncreaseLine = "Delay increase" + DEL
    

    for label in pre_defined_label_group:
        if condTrueDataMap.has_key(label):
            truePercentLine += "%.6f" % (float(len(condTrueDataMap[label])) / totalLen) + DEL
        else:
            truePercentLine += "0.0" + DEL
        if condFalseDataMap.has_key(label):
            falsePercentLine += "%.6f" % (float(len(condFalseDataMap[label])) / totalLen) + DEL
        else:
            falsePercentLine += "0.0" + DEL
        if condTrueDataMap.has_key(label) and condFalseDataMap.has_key(label):
            trueLen = len(condTrueDataMap[label])
            falseLen = len(condFalseDataMap[label])
            trueMedian = getMedian(condTrueDataMap[label])
            falseMedian = getMedian(condFalseDataMap[label])
            if falseMedian > 0:
                delayRatioLine += "%.6f" % (trueMedian / falseMedian) + DEL
                delayIncreaseLine += "%.6f+%.6f" % (trueMedian - falseMedian, falseMedian) + DEL
            else:
                delayRatioLine += "N/A" + DEL
                delayIncreaseLine += "N/A" + DEL
        else:
            delayRatioLine += "N/A" + DEL
            delayIncreaseLine += "N/A" + DEL

    print >> sys.stderr, truePercentLine
    print >> sys.stderr, falsePercentLine
    print >> sys.stderr, delayRatioLine
    print >> sys.stderr, delayIncreaseLine

if __name__ == "__main__":
    main()



