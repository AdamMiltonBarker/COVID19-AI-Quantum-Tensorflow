#!/bin/bash

read -p "? This script will install the COVID-19 AI Quantum Tensorflow Project 1 Python dependencies on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then
    echo "- COVID-19 AI Quantum Tensorflow Project 1 Python dependencies installing"
    pip install opencv-python
    pip install matplotlib
    pip install numpy
    pip install scipy
    pip install Pillow
    pip install jsonpickle
    pip install scikit-learn
    pip install scikit-image
    echo "- COVID-19 AI Quantum Tensorflow Project 1 Python dependencies installed";
    exit 0
else
    echo "- COVID-19 AI Quantum Tensorflow Project 1 Python dependencies installation terminated";
    exit 1
fi