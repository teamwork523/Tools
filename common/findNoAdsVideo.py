#!/usr/bin/env python

# output the video name without advertisement

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

    noAdsList = set([])

    # process input
    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        curVideoName = tempData[video_name_col]

        try:
            if tempData[ads_check_col] == ads_kw:
                noAdsList.remove(curVideoName)
            elif tempData[ads_check_col] == video_begin_kw:
                noAdsList.add(curVideoName)
        except KeyError:
            pass
        line = sys.stdin.readline()

    for noneAdsVideo in noAdsList:
        print noneAdsVideo

if __name__ == "__main__":
    main()
