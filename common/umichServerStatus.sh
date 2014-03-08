#/bin/bash

user="haokun"

serverArray=("ep2" "dolphin" "koala" "spidermonkey" \
             "falcon" "beluga" "owl")

for server in "${serverArray[@]}"; do
    hostname="$server.eecs.umich.edu"
    echo "################"
    echo "@ $hostname"
    ssh $user@$hostname 'df -h | head -2 | tail -1'
done
