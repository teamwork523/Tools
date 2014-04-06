#!/usr/bin/env python

import sys, math

# Assume the old delimiter is tab

def Usage():
    print sys.argv[0] + " xtic_frequency xtic_col new_del < input_file"

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 4:
        Usage()
        sys.exit(1)

    empty_del = " "

    xtic_freq = int(sys.argv[1])
    xtic_col = int(sys.argv[2]) - 1
    new_del = sys.argv[3]
    
    cur_col = 0

    while True:
        line = sys.stdin.readline()
        if not line: break
        cur_data = line.strip().split()
        if cur_col % xtic_freq != 0:
            cur_data[xtic_col] = empty_del
        print new_del.join(cur_data)
        cur_col += 1
            

if __name__ == "__main__":
    main()
