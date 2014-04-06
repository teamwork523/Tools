#!/usr/bin/env python

# seperate the traces and output them into multiple files
# plot the water level plot for retransmission and throughput

import sys, math

def Usage():
    print sys.argv[0] + " < filepath"

def main():
    DEL = "\t"
    time_col = 0
    kw_col = 1
    data_col = 2

    fp_stall = open("tmp_stall.txt", 'w')
    fp_fast_retx = open("tmp_fast_retx.txt", 'w')
    fp_rto = open("tmp_rto.txt", 'w')
    fp_retx = open("tmp_retx.txt", 'w')
    fp_throughput = open("tmp_throughput.txt", 'w')

    kw_to_fp = {"stall": fp_stall, \
                "Fast_Retx": fp_fast_retx, \
                "RTO": fp_rto, \
                "Retx": fp_retx, \
                "throughput": fp_throughput}
    kw_to_time = {"stall": {}, \
                  "Fast_Retx": {}, \
                  "RTO": {}, \
                  "throughput": {}}

    # need to figure out the earlist time
    start_time = None
    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split()
        try:
            curTime = float(curData[time_col])
            if start_time == None or \
               curTime < start_time:
                start_time = curTime
        except ValueError:
            print >> sys.stderr, "WARNING: invalid format " + line
            continue
        curkw = curData[kw_col]
        if curkw not in kw_to_time:
            print >> sys.stderr, "ERROR: current keyword " + curkw + " not exist!"
            sys.exit(1)
        if curkw == "throughput":
            try:
                curThroughput = float(curData[data_col])
            except ValueError:
                print >> sys.stderr, "WARNING: not valid throughput value " + str(curData[data_col])
                continue
            kw_to_time[curkw][curTime] = curThroughput
        else:
            if curTime not in kw_to_time[curkw]:
                kw_to_time[curkw][curTime] = 0
            kw_to_time[curkw][curTime] += 1
                

    # write each keyword to file
    # stall event
    curKey = "stall"
    if len(kw_to_time[curKey]) != 0:
        time_list = sorted(kw_to_time[curKey].keys())
        for index in range(len(time_list)):
            if index % 2 == 1:
                time_list[index] = str(time_list[index] - start_time) + "\n"
            else:
                time_list[index] = str(time_list[index] - start_time)
            kw_to_fp[curKey].write(time_list[index] + "\n")

    # TCP retransmission event (convert to cumulative points)
    for key in ["Fast_Retx", "RTO"]:
        sorted_time_list = sorted(kw_to_time[key].keys())
        priv_count = 0
        for time in sorted_time_list:
            cur_count = priv_count + kw_to_time[key][time]
            kw_to_fp[key].write(str(time - start_time) + DEL + \
                                str(priv_count) + "\n")
            kw_to_fp[key].write(str(time - start_time) + DEL + \
                                str(cur_count) + "\n")
            priv_count = cur_count

    retx_times = sorted(kw_to_time["Fast_Retx"].keys() + kw_to_time["RTO"].keys())
    priv_count = 0
    curKey = "Retx"
    for retx_time in retx_times:
        cur_count = priv_count        
        if retx_time in kw_to_time["Fast_Retx"]:
            cur_count += kw_to_time["Fast_Retx"][retx_time]
        if retx_time in kw_to_time["RTO"]:
            cur_count += kw_to_time["RTO"][retx_time]
        kw_to_fp[curKey].write(str(retx_time - start_time) + DEL + \
                               str(priv_count) + "\n")
        kw_to_fp[curKey].write(str(retx_time - start_time) + DEL + \
                               str(cur_count) + "\n")
        priv_count = cur_count

    # Throughput value
    curKey = "throughput"
    sorted_times = sorted(kw_to_time[curKey].keys())
    for time in sorted_times:
        kw_to_fp[curKey].write(str(time - start_time) + DEL + \
                               str(kw_to_time[curKey][time]) + "\n")

    fp_stall.close()
    fp_fast_retx.close()
    fp_rto.close()
    fp_retx.close()
    fp_throughput.close()


if __name__ == "__main__":
    main()
