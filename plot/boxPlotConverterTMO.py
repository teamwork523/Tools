#!/usr/bin/env python

import sys

# input is CSV file, output is 5%, 25%, mean, 75%, 95% (T-Mobile)

def Usage():
    print sys.argv[0] + " data_col header < filepath"

def main():
    # use a dict to hold all data. {key:value} = {x:y}
    header = ""
    DEL = ","

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 3:
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[-1] == "y" or sys.argv[-1] == "Y":
        header = sys.stdin.readline()

    data = []
    data_col = int(sys.argv[1]) - 1

    # process input
    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        if tempData[data_col] != "":
            data.append(float(tempData[data_col]))
        line = sys.stdin.readline()

    # Summary
    DEL = "\t"
    data.sort()
    data_len = len(data)
    min_data = data[int(data_len*0.05)]
    max_data = data[int(data_len*0.95)]
    first_quarter = data[int(data_len*0.25)]
    third_quarter = data[int(data_len*0.75)]
    mean = sum(data) * 1.0 / data_len
    print str(min_data) + DEL + \
          str(first_quarter) + DEL + \
          str(mean) + DEL + \
          str(third_quarter) + DEL + \
          str(max_data)

if __name__ == "__main__":
    main()

