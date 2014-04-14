#!/usr/bin/env python

# output the statistics based by categories

import sys, math

def Usage():
    print sys.argv[0] + " data_col cond header < filepath"

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
    cond = sys.argv[2]

    # check header
    if sys.argv[3] == "y" or sys.argv[3] == "Y":
        header = sys.stdin.readline()

    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split(DEL)

        try:
            data = float(curData[data_col])
        except ValueError:
            print >> sys.stderr, "ValueError detected: " + line

        if eval(str(data) + cond):
            print line.strip()

if __name__ == "__main__":
    main()
