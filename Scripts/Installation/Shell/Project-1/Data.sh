#!/bin/sh

read -p "? This script will install the COVID-19 AI Quantum Tensorflow Project 1 dataset in the correct directories on your device. Are you ready (y/n)? " cmsg

if [ "$cmsg" = "Y" -o "$cmsg" = "y" ]; then

    read -p "! Enter the path to your dataset directory (Not including the COVID-19 Radiography Database directory: " dpath
    read -p "! Enter the path to your dataset directory (Not including the COVID19-AI-Quantum-Tensorflow directory: " rpath

    DFOLDER="COVID-19 Radiography Database"
    RDFOLDER="COVID19-AI-Quantum-Tensorflow/Projects/1/Data"

    FDPPATH="$dpath/$DFOLDER/COVID-19"
    FDNPATH="$dpath/$DFOLDER/NORMAL"

    FRDPPATH="$rpath/$RDFOLDER/Train/1/"
    FRDNPATH="$rpath/$RDFOLDER/Train/0/"
    FRDTSTPATH="$rpath/$RDFOLDER/Test/"

    echo "- COVID-19 AI Quantum Tensorflow Project 1 dataset installing"
    ls -Q "$FDPPATH" | head -219 | xargs -i cp "$FDPPATH"/{} $FRDPPATH
    ls -Q "$FDNPATH" | head -219 | xargs -i cp "$FDNPATH"/{} $FRDNPATH

    ls -Q "$FRDPPATH" | head -10 | xargs -i mv "$FRDPPATH"/{} $FRDTSTPATH
    ls -Q "$FRDNPATH" | head -10 | xargs -i mv "$FRDNPATH"/{} $FRDTSTPATH

    echo "- COVID-19 AI Quantum Tensorflow Project 1 dataset installed";
    exit 0
else
    echo "- COVID-19 AI Quantum Tensorflow Project 1 dataset installation terminated";
    exit 1
fi