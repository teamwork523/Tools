#!/bin/bash

# TODO: make it automatic recursively print for all subfolders

if [ "$1" == "-h" ]; then
    echo "./compute_folder_diff.sh folder1 folder2"
    exit 1
fi

folder1=$1
folder2=$2

folder1_filenames=$(ls $folder1 | tee temp1.txt)
folder2_filenames=$(ls $folder2 | tee temp2.txt)

# compare file difference
echo "***********************"
echo "File items diff:"
echo "***********************"
diff -u temp1.txt temp2.txt

for i in $folder1_filenames; do
    echo ">>>>>>>>>>>>>>>>>>>>>>>>"
    echo "File content diff at $i"
    diff -u $folder1$i $folder2$i
    echo "<<<<<<<<<<<<<<<<<<<<<<<<"
done

rm temp1.txt temp2.txt 2> /dev/null
