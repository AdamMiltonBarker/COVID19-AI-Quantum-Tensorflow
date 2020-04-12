############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    COVID-19 AI Quantum Tensorflow
# Project:       Leveraging Quantum MNIST to detect COVID-19
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         QMNISTCOVID19
# Description:   QMNISTCOVID19 is a wrapper class that creates the COVID-19 COVID-19
#                Tensorflow QNN (Quantum Neural Network).
# License:       MIT License
# Last Modified: 2020-04-11
#
############################################################################################

import sys

from Classes.Helpers import Helpers
from Classes.Data import Data
from Classes.QMNIST import QMNIST

class QMNISTCOVID19():
    """ QMNISTCOVID19

    QMNISTCOVID19 is a wrapper class that creates the COVID-19 Tensorflow QNN (Quantum Neural Network).
    """

    def __init__(self):
        """ Initializes the class. """

        self.Helpers = Helpers("Core")

        self.Helpers.logger.info("QMNISTCOVID19 QNN initialization complete.")

    def do_data(self):
        """ Sorts the training data """

        self.Data = Data()
        self.Data.get_paths_n_labels()
        self.Data.process_data()

    def do_train(self):
        """ Creates & trains the QNN. """

        self.QMNIST = QMNIST()

        X_train_bin, X_test_bin = self.QMNIST.encode_as_binary(self.Data.X_train, self.Data.X_test)
        X_train_circ, X__test_circ = self.QMNIST.do_circuit_conversion(X_train_bin, X_test_bin)
        x_train_tfcirc, x_test_tfcirc = self.QMNIST.convert_to_tensors(X_train_circ, X__test_circ)

    def do_load_model(self):
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
    elif sys.argv[1] not in QMNISTCOVID19.Helpers.confs["qnn"]["params"]:
        print("Mode not supported! Train or Classify")
        exit()

    mode = sys.argv[1]

    if mode == "Train":
        """ Creates and trains the classifier """
        QMNISTCOVID19.do_data()
        QMNISTCOVID19.do_train()

    elif mode == "Classify":
        """ Runs the classifier locally."""
        QMNISTCOVID19.do_classify()

    else:
        """ Incorrect argument."""
        exit()

if __name__ == "__main__":
    main()