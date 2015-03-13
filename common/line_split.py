#!/usr/bin/env python

# Convert
# 1
# 2
# 3
# 4
#
# Into
# 1 2
# 3 4

import sys

def Usage():
    print sys.argv[0] + " < filename"

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 1:
        Usage()
        sys.exit(1)

    count = 0
    DEL = ","
    buf = ""

    # process input
    line = sys.stdin.readline().strip()
    while line != "":
        if count % 2 == 0:
            buf = line + DEL
        else:
            buf += line
            print buf
        count += 1
        line = sys.stdin.readline().strip()

if __name__ == "__main__":
    main()