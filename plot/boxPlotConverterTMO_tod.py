#!/usr/bin/env python

import sys

# input is CSV file, output is 5%, 25%, mean, 75%, 95% (T-Mobile)
# Assume time format: 2014 Apr 14  17:56:48.178
# Morning (0): 5 - 10
# Afternoon (1): 11 - 16
# Evening (2): 17 - 22
# Midnight (3): 23 - 4

def timeToTimeindex(time):
    hr = (int)(time.split()[-1].split(":")[0])
    # Morning
    if hr >= 5 and hr <= 10:
        return 0
    # Afternoon
    if hr >= 11 and hr <= 16:
        return 1
    # Evening
    if hr >= 17 and hr <= 22:
        return 2
    # Midnight
    return 3

def Usage():
    print sys.argv[0] + " data_col time_col xtic_offset header < filepath"

def main():
    # use a dict to hold all data. {key:value} = {x:y}
    header = ""
    DEL = ","

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 5:
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[-1] == "y" or sys.argv[-1] == "Y":
        header = sys.stdin.readline()

    data = {}
    data_col = int(sys.argv[1]) - 1
    time_col = int(sys.argv[2]) - 1
    xtic_offset = float(sys.argv[3])

    # process input
    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        if tempData[data_col] != "":
            timeIndex = timeToTimeindex(tempData[time_col])
            if timeIndex not in data:
                data[timeIndex] = []
            data[timeIndex].append(float(tempData[data_col]))
        line = sys.stdin.readline()

    # Summary
    DEL = "\t"
    for timeIndex in range(4):
        if timeIndex in data:
            curData = sorted(data[timeIndex])
            data_len = len(curData)
            min_data = curData[int(data_len*0.05)]
            max_data = curData[int(data_len*0.95)]
            first_quarter = curData[int(data_len*0.25)]
            third_quarter = curData[int(data_len*0.75)]
            mean = sum(curData) * 1.0 / data_len
            print str(timeIndex+xtic_offset) + DEL + \
                  str(min_data) + DEL + \
                  str(first_quarter) + DEL + \
                  str(mean) + DEL + \
                  str(third_quarter) + DEL + \
                  str(max_data)
        else:
            print str(timeIndex+xtic_offset) + DEL + ("0.0" + DEL)*4 + "0.0"

if __name__ == "__main__":
    main()
