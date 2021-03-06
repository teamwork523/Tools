#!/usr/bin/env python

import sys, math

# append two files if both first cols are the same, append the non common cols
# otherwise append everything the raw by raw
# Notice that file1 could be empty

def Usage():
    print sys.argv[0] + " file1 file2 cols_from_file2"

def main():
    # delimiter
    DEL = "\t"
    
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        Usage()
        sys.exit(1)

    f1 = open(sys.argv[1])
    f2 = open(sys.argv[2])
    col_of_interest = [int(i) - 1 for i in sys.argv[3:]]

    while True:
        file1_line = f1.readline()
        file2_line = f2.readline()
        if not file2_line:
            break
        l1 = file1_line.strip().split()
        l2 = file2_line.strip().split()
        l2_wanted = []
        for col_num in col_of_interest:
            l2_wanted.append(l2[col_num])

        print DEL.join(l1 + l2_wanted)


if __name__ == "__main__":
    main()
