#!/bin/bash

FMSG="- Tensorflow Quantum installation terminated"

read -p "? This script will install Tensorflow Quantum on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then

    echo "- GeniSysAI installing Tensorflow Quantum"
    
    pip3 install --upgrade pip
    pip3 install tensorflow==2.1.0
    pip3 install cirq==0.7.0
    pip3 install tensorflow-quantum

    exit 0

else
    echo $FMSG;
    exit 1
fi