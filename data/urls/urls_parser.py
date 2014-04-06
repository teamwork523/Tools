#!/usr/bin/env python
import sys, math, datetime

# filter out useful URLs

def resetTimer(curTimer):
    MIN_INTERVAL = 15 * 1000    # in ms
    if curTimer > MIN_INTERVAL:
        return MIN_INTERVAL
    return curTimer

def isURLinBlackList(url):
    blackList = ["_204", "www.google-analytics.com", "complete/search", \
                 "chartbeat.net", "xtify.com", "s2.youtube.com", ".jpg", ".gif", \
                 ".ico", ".tgz", ".zip", ".png", ".jpeg", "googlesyndication", \
                 "s2.wp.com", "ad.doubleclick.net", "clients1.google.com"]
    for bad_url in blackList:
        if bad_url in url:
            return True
    return False

# check whether current URL is valid or not
def isValidURLs(url):
    if len(url) < 1 or \
       len(url) > 200 or \
       not url[0].isalpha() or \
       "." in url[-5:] or \
       isURLinBlackList(url):
        return False
    return True

# sanitize the URL
def sanitizeURL(url):
    if url[-1] == "/":
        return url[:-1]
    return url

def Usage():
    print sys.argv[0] + " < url_raw_data"

def main():
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 1:
        Usage()
        sys.exit(1)
    DEL = "\t"

    results = ""
    total_hours = 0.0
    url_stats = {"total": 0.0, "demotion": 0.0, "promotion": 0.0}
    while True:
        line = sys.stdin.readline()
        if not line: break
        curData = line.strip().split(DEL)
        if len(curData) > 1 and isValidURLs(curData[0]):
            try:
                curData[1] = str(resetTimer(int(curData[1])))
                curData[0] = str(sanitizeURL(curData[0]))
                url_stats["total"] += 1
                if float(curData[1]) > 3*1000:
                    if float(curData[1]) < 4.5*1000:
                        url_stats["demotion"] += 1
                    elif float(curData[1]) > 10*1000:
                        url_stats["promotion"] += 1
                total_hours += abs(float(curData[1]))
                results += DEL.join(curData) + "\n"
            except ValueError:
                pass
    print results[:-1]

    print >> sys.stderr, "Total time is " + str(total_hours / 1000) + \
                         " = " + str(datetime.timedelta(seconds=int(total_hours / 1000)))
    print >> sys.stderr, "Total URLs is " + str(url_stats["total"]) + \
                         "; Demotion ratio is " + "%.3f" % (url_stats["demotion"] / url_stats["total"]) + \
                         "; Promotion ratio is " + "%.3f" % (url_stats["promotion"] / url_stats["total"])
    print >> sys.stderr, "*" * 80

if __name__ == "__main__":
    main()
