#!/bin/bash

read -p "? This script will install the COVID-19 AI Quantum Tensorflow Project 1 Python dependencies on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then
    echo "- COVID-19 AI Quantum Tensorflow Project 1 Python dependencies installing"
    pip3 install --user opencv-python
    pip3 install --user matplotlib
    pip3 install --user numpy
    pip3 install --user scipy
    pip3 install --user Pillow
    pip3 install --user jsonpickle
    pip3 install --user scikit-learn
    pip3 install --user scikit-image
    echo "- COVID-19 AI Quantum Tensorflow Project 1 Python dependencies installed";
    exit 0
else
    echo "- COVID-19 AI Quantum Tensorflow Project 1 Python dependencies installation terminated";
    exit 1
fi