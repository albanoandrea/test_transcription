#!/bin/sh
if [ $# -ne 2 ] 
then
    echo "Usage $0 <mp3 in> <wav out>"
    exit 1
fi
ffmpeg -i $1 -ar 16000 -ac 1 $2 