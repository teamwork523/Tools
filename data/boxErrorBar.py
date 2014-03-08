#!/usr/bin/env python
import sys, math

# convert excel type of data into box err bar type (mean std mean std)

def Usage():
    print sys.argv[0] + " label_col(x) data_col(y) header < filepath"

# calculate the standard deviation of the data
def cal_std (data, mean):
    diff_sum = 0.0
    for ele in data:
        diff_sum += (ele-mean)*(ele-mean)
    return math.sqrt(diff_sum / len(data))

def main():
    DEL = "\t"
    data = []
    pre_defined_label_group = ["PCH", "FACH", "DCH",\
                               "PCH_TO_FACH", "FACH_TO_DCH",\
                               "DCH_TO_FACH", "FACH_TO_PCH"]

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 4:
        Usage()
        sys.exit(1)

    label_col = int(sys.argv[1]) - 1
    data_col = int(sys.argv[2]) - 1

    # check header
    if sys.argv[3] == "y" or sys.argv[3] == "Y":
        header = sys.stdin.readline()

    # read data
    dataMap = {}   
    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split()
        label = curData[label_col]
        data = 0.0
        try:
            data = float(curData[data_col])
        except ValueError:
            print >> sys.std, "ValueError detected: " + line
        if dataMap.has_key(label):
            dataMap[label].append(data)
        else:
            dataMap[label] = [data]
    
    # generate the boxErrorBar plot result
    sortedLabel = sorted(dataMap.keys())
    for i in range(len(pre_defined_label_group)):
        curLabel = pre_defined_label_group[i]
        line = curLabel + DEL + str(i+0.5) + DEL
        if dataMap.has_key(curLabel):
            # myMean = float(sum(dataMap[curLabel]))/float(len(dataMap[curLabel]))
            # myStd = cal_std(dataMap[curLabel], myMean)
            data_len = len(dataMap[curLabel])
            sortedData = sorted(dataMap[curLabel])
            myMedian = sortedData[int(data_len*0.5)]
            myLower = sortedData[int(data_len*0.05)]
            myUpper = sortedData[int(data_len*0.95)]
        else:
            # myMean = 0.0
            # myStd = 0.0
            myMedian = 0.0
            myLower = 0.0
            myUpper = 0.0
        # line += str(myMean) + DEL + str(myStd) + DEL
        line += str(myMedian) + DEL + str(myLower) + DEL + str(myUpper) + DEL
        print line.strip()

if __name__ == "__main__":
    main()

