#!/usr/bin/env python

# output the video name with advertisement

import sys

def Usage():
    print sys.argv[0] + " < filename"

def main():
    video_name_col = 1
    ads_check_col = 2
    ads_kw = "ads"
    video_begin_kw = "video_begin"
    DEL = "\t"

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 1:
        Usage()
        sys.exit(1)
    
    # check header
    if sys.argv[-1] == "y" or sys.argv[-1] == "Y":
        header = sys.stdin.readline()

    adsList = set([])

    # process input
    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        curVideoName = tempData[video_name_col]

        try:
            if tempData[ads_check_col] == ads_kw:
                adsList.add(curVideoName)
        except KeyError:
            pass
        line = sys.stdin.readline()

    for adsV in adsList:
        print adsV

if __name__ == "__main__":
    main()
