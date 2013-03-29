#!/bin/bash
# samers-maker-3.bash
# takes one argument and makes a bunch of these files with the same parameters
# using the number to name them

E_BADARGS=85

if [ ! -n "$1" ]
then
    echo "Usage: `basename $0` samers-number"
    exit $E_BADARGS
fi

./chordmaker.py 2 3 8 1 3 0 > ./testfiles/samers-3/chords-${1}.dat;
./contourmaker.py 2 3 8 16 > ./testfiles/samers-3/contour-${1}-pitch.dat;
./contourmaker.py 2 3 8 4 > ./testfiles/samers-3/contour-${1}-dynamic.dat;
./rhythmmaker.py 2 3 8 4 0.0 > ./testfiles/samers-3/rhythm-${1}.dat;
./cmloadingtests5_b.py sc ./testfiles/samers-3/pitch-range-1.dat \
    ./testfiles/samers-3/dynamic-range-1.dat \
    ./testfiles/samers-3/contour-${1}-pitch.dat \
    ./testfiles/samers-3/contour-${1}-dynamic.dat \
    ./testfiles/samers-3/chords-${1}.dat ./testfiles/samers-3/rhythm-${1}.dat \
    > ./testfiles/samers-3/render-${1}.dat

exit 0
