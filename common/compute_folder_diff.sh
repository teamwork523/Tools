#!/bin/bash

folder1=$1
folder2=$2

folder1_filenames=$(ls $folder1 | tee temp1.txt)
folder2_filenames=$(ls $folder2 | tee temp2.txt)

# compare file difference
diff -u temp1.txt temp2.txt

for i in $folder1_filenames; do
    echo "*********************"
    echo "File difference at $i"
    diff -u $folder1$i $folder2$i
done

rm temp1.txt temp2.txt 2> /dev/null
