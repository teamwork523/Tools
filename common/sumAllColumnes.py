#!/usr/bin/env python

import sys, math

# sum up all the columns

def Usage():
    print sys.argv[0] + " < filename"

def main():
    # delimiter
    DEL = "\t"
    
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        Usage()
        sys.exit(1)

    dataByCol = []

    while True:
        line = sys.stdin.readline()
        if not line: break
        splittedLine = line.strip().split(DEL)
        if dataByCol == []:
            dataByCol = [float(i) for i in splittedLine]
        else:
            for index in range(len(splittedLine)):
                dataByCol[index] += float(splittedLine[index])

    print DEL.join([str(i) for i in dataByCol])
                
        
if __name__ == "__main__":
    main()
