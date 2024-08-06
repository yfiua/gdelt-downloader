#!/bin/sh
#check existence of lastupdate.txt
if [ -f lastupdate.txt ]; then
    curl -O -z lastupdate.txt http://data.gdeltproject.org/gdeltv2/lastupdate.txt
else
    curl -O http://data.gdeltproject.org/gdeltv2/lastupdate.txt
fi
