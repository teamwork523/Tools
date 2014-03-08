#!/usr/bin/env python

# replace a keyword based on the schema file (colon seperated)

import sys

def Usage():
    print sys.argv[0] + " schema_file extraInfo < filepath"

def main():
    DEL = ":"
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) < 2:
        Usage()
        sys.exit(1)

    extraInfo = ""
    if len(sys.argv) > 2:
        extraInfo = sys.argv[2] + ":"

    s = open(sys.argv[1], "r")
    results = sys.stdin.read()

    for line in s.readlines():
        splittedLine = line.strip().split(DEL)
        results = results.replace(splittedLine[0], extraInfo + splittedLine[1])
    # remove the last newline
    print results[:-1]
    s.close()
    
if __name__ == "__main__":
    main()
