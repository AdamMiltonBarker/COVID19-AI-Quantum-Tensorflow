#!/bin/bash

FMSG="- COVID-19 AI Quantum Tensorflow Project 1 installation terminated"

read -p "? This script will install the COVID-19 AI Quantum Tensorflow Project 1 on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then

    echo "- Installing COVID-19 AI Quantum Tensorflow Project 1"

    sh Scripts/Installation/Shell/Project-1/Python.sh
    if [ $? -ne 0 ]; then
        echo $FMSG;
        exit
    fi

    sh Scripts/Installation/Shell/Project-1/Data.sh
    if [ $? -ne 0 ]; then
        echo $FMSG;
        exit
    fi

    exit

else
    echo $FMSG;
    exit
fi