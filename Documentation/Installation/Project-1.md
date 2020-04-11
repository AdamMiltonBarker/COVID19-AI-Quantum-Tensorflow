# Peter Moss COVID-19 AI Research Project

## COVID-19 AI Quantum Tensorflow

### Leveraging Quantum MNIST to detect COVID-19

[![GeniSysAI Server](../../Media/Images/covid-19-ai-research-qtf.png)](https://github.com/COVID-19-AI-Research-Project/COVID19-AI-Quantum-Tensorflow)

# Prerequisites
- Please follow the [Installation Guide](../../Documentation/Installation/Installation.md "Installation Guide") to install COVID-19 AI Quantum Tensorflow. Steps to clone the repository are also provided in this installation guide.
- Please download the [COVID-19 Radiography Database](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database/data "COVID-19 Radiography Database")

# Installation & setup
Here you will find all of the required setup steps to get all required packages installed.

## Quick install
You can follow the installation steps manually on this page, or you can use the "quick install" scripts provided. To do a quick install, navigate to the project root and use the following command:

```
sh Scripts/Installation/Shell/Project-1/Install.sh
```

&nbsp;

# Install required packages
These commands will install the required Python dependencies.

```
pip install opencv-python
pip install matplotlib
pip install numpy
pip install scipy
pip install Pillow
pip install jsonpickle
pip install scikit-learn
pip install scikit-image
```

&nbsp;

# Prepare dataset
Assuming you have downloaded the [COVID-19 Radiography Database](https://www.kaggle.com/tawsifurrahman/covid19-radiography-database/data "COVID-19 Radiography Database"), use the following commands, replacing **PathToDataset** with the absolute path to the extracted dataset directory and **PathToProjectRoot** with the absolute path to the location of your project root.

These commands will copy 219 files from the **COVID-19** & **NORMAL** directories of the **COVID-19 Radiography Database** to the project training data folders, and then move 10 images from each class to the project testing data folder.

```
DFOLDER="COVID-19 Radiography Database"
RDFOLDER="COVID19-AI-Quantum-Tensorflow/Projects/1/Data"

FDPPATH="PathToDataset/$DFOLDER/COVID-19"
FDNPATH="PathToDataset/$DFOLDER/NORMAL"

FRDPPATH="PathToProjectRoot/$RDFOLDER/Train/1/"
FRDNPATH="PathToProjectRoot/$RDFOLDER/Train/0/"
FRDTSTPATH="PathToProjectRoot/$RDFOLDER/Test/"

ls -Q "$FDPPATH" | head -219 | xargs -i cp "$FDPPATH"/{} $FRDPPATH
ls -Q "$FDNPATH" | head -219 | xargs -i cp "$FDNPATH"/{} $FRDNPATH

ls -Q "$FRDPPATH" | head -10 | xargs -i mv "$FRDPPATH"/{} $FRDTSTPATH
ls -Q "$FRDNPATH" | head -10 | xargs -i mv "$FRDNPATH"/{} $FRDTSTPATH
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