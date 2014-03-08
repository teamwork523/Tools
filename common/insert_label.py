#!/usr/bin/env python

# insert the column number 

import sys

def Usage():
    print sys.argv[0] + " start_num delta insert_col header < filepath"

def main():
    DEL = "\t"
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 5:
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[len(sys.argv) - 1] == "y" or sys.argv[len(sys.argv) - 1] == "Y":
        header = sys.stdin.readline()    

    insert_col = int(sys.argv[3]) - 1
    start_num = float(sys.argv[1])
    delta = float(sys.argv[2])
    cur_num = start_num

    while True:
        line = sys.stdin.readline()
        if not line: break
        tempData = line.strip().split()
        tempData.insert(insert_col, "%.1f" % (cur_num))
        print DEL.join(tempData)
        cur_num += delta 

if __name__ == "__main__":
    main()
