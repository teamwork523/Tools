#!/usr/bin/env python

# seperate the traces and output them into multiple files

import sys, math

def Usage():
    print sys.argv[0] + " < filepath"

def main():
    time_col = 0
    kw_col = 1

    fp_stall = open("tmp_stall.txt", 'w')
    fp_fast_retx = open("tmp_fast_retx.txt", 'w')
    fp_rto = open("tmp_rto.txt", 'w')

    kw_to_fp = {"stall": fp_stall, \
                "Fast_Retx": fp_fast_retx, \
                "RTO": fp_rto}
    kw_to_time = {"stall": [], \
                  "Fast_Retx": [], \
                  "RTO": []}

    # need to figure out the earlist time
    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split()
        try:
            curTime = float(curData[time_col])
        except ValueError:
            print >> sys.stderr, "WARNING: invalid format " + line
            continue
        curkw = curData[kw_col]
        if curkw not in kw_to_time:
            print >> sys.stderr, "ERROR: current keyword " + curkw + " not exist!"
            sys.exit(1)
        kw_to_time[curkw].append(curTime)

    # sort the time + convert to relative time globally
    start_time = None
    for key in kw_to_time.keys():
        if len(kw_to_time[key]) == 0:
            continue
        kw_to_time[key] = sorted(kw_to_time[key])
        if start_time == None or \
           kw_to_time[key][0] < start_time:
            start_time = kw_to_time[key][0]
                
    for key in kw_to_time.keys():
        kw_to_time[key] = [str(time - start_time) for time in kw_to_time[key]]

    # write to file
    for key in kw_to_time.keys():
        if len(kw_to_time[key]) == 0:
            continue
        # insert additional newline to stall event
        if key == "stall":
            for index in range(len(kw_to_time[key])):
                if index != 0 and index % 2 == 1:
                    kw_to_time[key][index] = str(kw_to_time[key][index]) + "\n"
        kw_to_fp[key].write("\n".join(kw_to_time[key]))

    fp_stall.close()
    fp_fast_retx.close()
    fp_rto.close()


if __name__ == "__main__":
    main()
