#!/bin/sh

mkdir build
cd assets

for infile in $(ls *.svg) ; do
    outfile=$(echo $infile | sed 's/\.svg/\.png/')
    inkscape -o "../build/$outfile" $infile
done

