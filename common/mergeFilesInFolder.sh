#!/bin/bash

folderPath=$1
targetFileName=$2
output=$3

rm $output 2> /dev/null; touch $output

for file in $(ls $folderPath); do
    cat $folderPath/$file/$targetFileName >> $output
done
