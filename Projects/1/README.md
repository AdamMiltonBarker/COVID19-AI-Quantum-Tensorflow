# Peter Moss COVID-19 AI Research Project

## COVID-19 AI Quantum Tensorflow

### Leveraging Quantum MNIST to detect COVID-19

[![GeniSysAI Server](../../Media/Images/covid-19-ai-research-qtf.png)](https://github.com/COVID-19-AI-Research-Project/COVID19-AI-Quantum-Tensorflow)

# Introduction
In this project we will leverage [Tensorflow Quantum](https://www.tensorflow.org/quantum "Tensorflow Quantum") [MNIST Classification](https://www.tensorflow.org/quantum/tutorials/mnist "MNIST Classification") code and modify the network to detect COVID-19.

&nbsp;

# Hardware

I used the following hardware, but the tutorial should work fine on other CPUs/NVIDIA GPUs.

- Intel® Core™ i7-7700HQ CPU @ 2.80GHz × 8
- NVIDIA GTX 1050 Ti Ti/PCIe/SSE2

&nbsp;

# Operating system

- Ubuntu 18.04

&nbsp;

# Programming language

- Python 3.7

&nbsp;

# Software

In this project we have used the following core softwares:

- Tensorflow 2.1.0
- Tensorflow-Quantum

&nbsp;

# Tensorflow Quantum

"TensorFlow Quantum (TFQ) is a quantum machine learning library for rapid prototyping of hybrid quantum-classical ML models. Research in quantum algorithms and applications can leverage Google’s quantum computing frameworks, all from within TensorFlow.

TensorFlow Quantum focuses on quantum data and building hybrid quantum-classical models. It integrates quantum computing algorithms and logic designed in Cirq, and provides quantum computing primitives compatible with existing TensorFlow APIs, along with high-performance quantum circuit simulators. Read more in the TensorFlow Quantum white paper." [Source](https://www.tensorflow.org/quantum "Source")

&nbsp;

# COVID-19 Radiography Database

"A team of researchers from Qatar University, Doha, Qatar and the University of Dhaka, Bangladesh along with their collaborators from Pakistan and Malaysia in collaboration with medical doctors have created a database of chest X-ray images for COVID-19 positive cases along with Normal and Viral Pneumonia images. In our current release, there are 219 COVID-19 positive images, 1341 normal images and 1345 viral pneumonia images. We will continue to update this database as soon as we have new x-ray images for COVID-19 pneumonia patients." [Source](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database/data "Source")

In our project we will use the COVID-19 positive xrays dataset, and the normal xrays dataset. We will use 219 images from each dataset, using 9 images for additional testing.

&nbsp;

# Installation
Please follow the [COVID-19 AI Quantum Tensorflow Installation Guide](../../Documentation/Installation/Installation.md "COVID-19 AI Quantum Tensorflow Installation Guide") to install COVID-19 AI Quantum Tensorflow, and finally the [COVID-19 AI Quantum Tensorflow Project 1 Installation Guide](../../Documentation/Installation/Project-1.md "COVID-19 AI Quantum Tensorflow Project 1 Installation Guide").

&nbsp;

# Training the Quantum Convolutional Neural Network

Now you are ready to train your Quantum Convolutional Neural Network. As mentioned above, an Ubuntu machine was used. Using different machines/CPU may vary the results, if so please let us know your findings.

## Start The Training

Ensuring you have completed all previous steps, you can start training using the following commands from the project root.

```
cd Projects/1/
python QMNISTCOVID19.py Train
```

This tells the classifier to start in Train mode which will start the model training process.

### Data

First the data will be prepared.

```
2020-04-12 02:30:27,183 - Core - INFO - Helpers class initialization complete.
2020-04-12 02:30:27,183 - Core - INFO - QMNISTCOVID19 QNN (Quantum Neural Network) initialization complete.
2020-04-12 02:30:27,183 - OpenCV - INFO - OpenCV Helper Class initialization complete.
2020-04-12 02:30:27,183 - Data - INFO - Data Helper Class initialization complete.
2020-04-12 02:30:27,184 - Data - INFO - Data Paths: 418
2020-04-12 02:30:31,789 - Data - INFO - Data shuffled
2020-04-12 02:30:31,789 - Data - INFO - Data shape: (418, 4, 4, 3)
2020-04-12 02:30:31,790 - Data - INFO - Labels shape: (418, 2)
2020-04-12 02:30:31,790 - Data - INFO - Labels: (418, 2)
2020-04-12 02:30:31,790 - Data - INFO - Training data: (311, 4, 4, 3)
2020-04-12 02:30:31,791 - Data - INFO - Training labels: (311, 2)
2020-04-12 02:30:31,791 - Data - INFO - Validation data: (107, 4, 4, 3)
2020-04-12 02:30:31,791 - Data - INFO - Validation labels: (107, 2)
```

&nbsp;

# Contributing

The [Peter Moss COVID-19 AI Research Project](https://github.com/COVID-19-AI-Research-Project "Peter Moss COVID-19 AI Research Project") encourages, and welcomes, code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull requests. You will also find information about our code of conduct on this page.

## Contributors

- [Adam Milton-Barker](https://www.leukemiaresearchassociation.ai/team/adam-milton-barker "Adam Milton-Barker") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") Founder & Intel Software Innovator, Sabadell, Spain

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](../../issues "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.