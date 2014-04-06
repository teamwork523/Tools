#!/usr/bin/env python

# Extract the lines of data that falls within range of time

import calendar
from datetime import datetime
import sys

def parseUTCTimeStamp(time, tz_offset=0.0):
    splitedTime = time.split("/")
    if len(splitedTime) != 6:
        print >> sys.stderr, "ERROR: wrong time format"
        Usage()
        sys.exit(1)
    dt = datetime(int(splitedTime[0]), int(splitedTime[1]), int(splitedTime[2]), \
                  int(splitedTime[3]), int(splitedTime[4]), int(splitedTime[5]))
    return calendar.timegm(dt.utctimetuple()) + tz_offset

def Usage():
    print sys.argv[0] + " time_col t_start t_end tz_diff_to_utc header < filename"
    print " " * (len(sys.argv[0]) + 1) + "Format of time is y/m/d/h/m/s"

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) < 6:
        Usage()
        sys.exit(1)

    # check header
    if sys.argv[-1] == "y" or sys.argv[-1] == "Y":
        header = sys.stdin.readline()

    DEL = "\t"

    time_col = int(sys.argv[1]) - 1
    tz_offset = int(sys.argv[-2]) * 3600
    start_time = parseUTCTimeStamp(sys.argv[2], tz_offset)
    end_time = parseUTCTimeStamp(sys.argv[3], tz_offset)
    end_count = 0
    while True:
        line = sys.stdin.readline()
        if not line: break
        curTime = float(line.strip().split(DEL)[time_col][:10])

        if start_time <= curTime and \
           end_time >= curTime:
            if "action_post_status\tF" in line:
                end_count += 1
            print line.strip()

    print >> sys.stderr, "*" * 30 + "\n" + "Total count is " + str(end_count)

if __name__ == "__main__":
    main()
    
