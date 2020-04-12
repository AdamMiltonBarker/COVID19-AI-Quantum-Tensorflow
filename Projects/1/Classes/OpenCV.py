############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    COVID-19 AI Quantum Tensorflow
# Project:       Leveraging Quantum MNIST to detect COVID-19
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         OpenCV Helper Class
# Description:   OpenCV functions for the Leveraging Quantum MNIST to detect COVID-19 QNN
#                (Quantum Neural Network).
# License:       MIT License
# Last Modified: 2020-04-12
#
############################################################################################

import cv2

from Classes.Helpers import Helpers

class OpenCV():
    """ OpenCV Helper Class

    OpenCV functions for the Leveraging Quantum MNIST to detect COVID-19 QNN (Quantum Neural Network).
    """

    def __init__(self):
        """ Initializes the class. """

        self.Helpers = Helpers("OpenCV", False)

        self.Helpers.logger.info("OpenCV Helper Class initialization complete.")

    def resize(self, path, dim):
        """ Resizes an image to the provided dimensions (dim). """

        return cv2.resize(cv2.imread(path), (dim, dim))
