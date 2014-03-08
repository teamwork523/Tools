#!/usr/bin/env python

# seperate the traces and output them into multiple files
# handle the timestamp

import sys, math

def Usage():
    print sys.argv[0] + " < filepath"

def main():
    # pre-defined variables
    filename_col = 0
    time_col = 1
    plot_value_col = 2
    extra_info_col = 3
    RRC_state_value_map = {"PCH": 1, \
                           "PCH_TO_FACH": 2, \
                           "FACH": 3, \
                           "FACH_TO_DCH": 4, \
                           "DCH": 5, \
                           "DCH_TO_FACH": 4, \
                           "FACH_TO_PCH": 2}
    
    fp_IP = open("tmp_IP.txt", 'w')
    #fp_RLC_begin = open("tmp_RLC_begin.txt", 'w')
    #fp_RLC_end = open("tmp_RLC_end.txt", 'w')
    fp_RLC = open("tmp_RLC.txt", 'w')
    fp_DCH_to_FACH_start = open("tmp_DCH_to_FACH_start.txt", 'w')
    fp_DCH_to_FACH_end = open("tmp_DCH_to_FACH_end.txt", 'w')
    fp_FACH_to_DCH_start = open("tmp_FACH_to_DCH_start.txt", 'w')
    fp_FACH_to_DCH_end = open("tmp_FACH_to_DCH_end.txt", 'w')
    fp_PCH_to_FACH_start = open("tmp_PCH_to_FACH_start.txt", 'w')
    fp_PCH_to_FACH_end = open("tmp_PCH_to_FACH_end.txt", 'w')
    fp_FACH_to_PCH_start = open("tmp_FACH_to_PCH_start.txt", 'w')
    fp_FACH_to_PCH_end = open("tmp_FACH_to_PCH_end.txt", 'w')

    DEL = "\t"
    data = []

    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        Usage()
        sys.exit(1)

    baseTime = None

    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split()
        filename = curData[filename_col]

        if baseTime == None:
            baseTime = float(curData[time_col])
        line = str(float(curData[time_col]) - baseTime) + DEL

        if filename == "IP":
            if curData[extra_info_col] in RRC_state_value_map:
                line += str(RRC_state_value_map[curData[extra_info_col]]) + "\n"
            else:
                line += str(0) + "\n"
            fp_IP.write(line)

        elif filename == "RLC_begin":
            if curData[plot_value_col] in RRC_state_value_map:
                line += str(RRC_state_value_map[curData[plot_value_col]]) + "\n"
            else:
                line += str(0) + "\n"
            fp_RLC.write(line)
        elif filename == "RLC_end":
            # add extra space for discontinuous points
            if curData[plot_value_col] in RRC_state_value_map:
                line += str(RRC_state_value_map[curData[plot_value_col]]) + "\n\n"
            else:
                line += str(0) + "\n\n"
            fp_RLC.write(line)
        elif filename == "DCH_to_FACH_start":
            line += str(RRC_state_value_map["DCH_TO_FACH"]) + "\n"
            fp_DCH_to_FACH_start.write(line)
        elif filename == "DCH_to_FACH_end":
            line += str(RRC_state_value_map["DCH_TO_FACH"]) + "\n"
            fp_DCH_to_FACH_end.write(line)
        elif filename == "FACH_to_DCH_start":
            line += str(RRC_state_value_map["FACH_TO_DCH"]) + "\n"
            fp_FACH_to_DCH_start.write(line)
        elif filename == "FACH_to_DCH_end":
            line += str(RRC_state_value_map["FACH_TO_DCH"]) + "\n"
            fp_FACH_to_DCH_end.write(line)
        elif filename == "PCH_to_FACH_start":
            line += str(RRC_state_value_map["PCH_TO_FACH"]) + "\n"
            fp_PCH_to_FACH_start.write(line)
        elif filename == "PCH_to_FACH_end":
            line += str(RRC_state_value_map["PCH_TO_FACH"]) + "\n"
            fp_PCH_to_FACH_end.write(line)
        elif filename == "FACH_to_PCH_start":
            line += str(RRC_state_value_map["FACH_TO_PCH"]) + "\n"
            fp_FACH_to_PCH_start.write(line)
        elif filename == "FACH_to_PCH_end":
            line += str(RRC_state_value_map["FACH_TO_PCH"]) + "\n"
            fp_FACH_to_PCH_end.write(line)

    fp_IP.close()
    #fp_RLC_begin.close()
    #fp_RLC_end.close()
    fp_RLC.close()
    fp_DCH_to_FACH_start.close()
    fp_DCH_to_FACH_end.close()
    fp_FACH_to_DCH_start.close()
    fp_FACH_to_DCH_end.close()
    fp_PCH_to_FACH_start.close()
    fp_PCH_to_FACH_end.close()
    fp_FACH_to_PCH_start.close()
    fp_FACH_to_PCH_end.close()

if __name__ == "__main__":
    main()
