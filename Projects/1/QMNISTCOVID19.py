############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    COVID-19 AI Quantum Tensorflow
# Project:       Leveraging Quantum MNIST to detect COVID-19
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         QMNISTCOVID19
# Description:   QMNISTCOVID19 is a wrapper class that creates the COVID-19 Quantum Classifer.
# License:       MIT License
# Last Modified: 2020-04-11
#
############################################################################################

import sys

from Classes.Helpers import Helpers

class QMNISTCOVID19():
    """ QMNISTCOVID19

    QMNISTCOVID19 is a wrapper class that creates the COVID-19 Quantum Classifer.
    """

    def __init__(self):
        """ Initializes the class. """

        self.Helpers = Helpers("Core")

        self.Helpers.logger.info("QMNISTCOVID19 CNN initialization complete.")

    def do_data(self):
        """ Sorts the training data """
        print("TODO")

    def do_train(self):
        """ Creates & trains the model. """
        print("TODO")

    def do_load(self):
        """ Loads the trained model """
        print("TODO")

    def do_classify(self):
        """ Classifies the test data """
        print("TODO")

QMNISTCOVID19 = QMNISTCOVID19()

def main():

    if len(sys.argv) < 2:
        print("You must provide an argument")
        exit()
    elif sys.argv[1] not in QMNISTCOVID19.Helpers.confs["cnn"]["core"]:
        print("Mode not supported! Train or Classify")
        exit()

    mode = sys.argv[1]

    if mode == "Train":
        """ Creates and trains the classifier """
        QMNISTCOVID19.do_train()

    elif mode == "Classify":
        """ Runs the classifier locally."""
        QMNISTCOVID19.do_classify()

    else:
        """ Incorrect argument."""
        exit()

if __name__ == "__main__":
    main()