#!/bin/bash
# samers-maker-1.bash
# takes one argument and makes a bunch of these files with the same parameters
# using the number to name them

E_BADARGS=85

if [ ! -n "$1" ]
then
    echo "Usage: `basename $0` samers-number"
    exit $E_BADARGS
fi

./chordmaker.py 2 3 8 8 3 0 > ./testfiles/samers-1/chords-${1}.dat;
./contourmaker.py 2 3 8 8 > ./testfiles/samers-1/contour-${1}-pitch.dat;
./contourmaker.py 2 3 8 8 > ./testfiles/samers-1/contour-${1}-dynamic.dat;
./rhythmmaker.py 2 3 8 8 0.2 > ./testfiles/samers-1/rhythm-${1}.dat;
./cmloadingtests5_b.py sc ./testfiles/samers-1/pitch-range-1.dat \
    ./testfiles/samers-1/dynamic-range-1.dat \
    ./testfiles/samers-1/contour-${1}-pitch.dat \
    ./testfiles/samers-1/contour-${1}-dynamic.dat \
    ./testfiles/samers-1/chords-${1}.dat ./testfiles/samers-1/rhythm-${1}.dat \
    > ./testfiles/samers-1/render-${1}.dat

exit 0
