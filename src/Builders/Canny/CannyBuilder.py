# -*- coding: utf-8 -*-
__author__ = 'Rainer Arencibia'
from PyQt4 import QtGui, QtCore
#  *************************** from src.Operators.Configurator import Ui_Configurator
import cv2
import numpy as np


class WindowConfigurator(QtGui.QDialog):
    """
    This class it´s the window for the configurator,
    object that allow us to select and change the settings
    for the canny filter.
    """
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = self                          # ********************Ui_Configurator()
        self.ui.setupUi(self)


class CannyBuilder:
    """
    This class it´s the Canny builder, witch receive an image in color or gray and
    :return an image only with the edges of objects of the original image.
    """
    def __init__(self, img):
        """
        :param img: receive a picture/video frame
        :return: self.edge_image, an image with only the edges of objects of image received.
        """
        img_read = cv2.imread(img)
        self.rgb_image = cv2.cvtColor(img_read, cv2.COLOR_BGR2RGB)
        self.gray_image = cv2.cvtColor(self.rgb_image, cv2.COLOR_RGB2GRAY)

        self.sigma = 0.33  # 33% good value for a lots of images
        self.value = np.median(self.gray_image)  # median value of the image [0, 255]
        self.edge_image = np.zeros_like(self.gray_image)  # we save the result image with the edges.
        self.low_threshold = int(max(0, (1.0 - self.sigma) * self.value))  # generic parameter low threshold
        self.max_threshold = int(min(255, (1.0 + self.sigma) * self.value))  # generic parameter max threshold
        self.lower = self.upper = 0  # we gonna save low threshold & max threshold values if the user changed.

        #  self.window_config = WindowConfigurator()
        #  QtCore.QObject.connect(self.window_config.ui.slider1, QtCore.SIGNAL('valueChanged(int)'), self.slider1)
        #  QtCore.QObject.connect(self.window_config.ui.slider2, QtCore.SIGNAL('valueChanged(int)'), self.slider2)

    def slider1(self, value):
        """
        :param value: will be the number selected by the user for the low threshold.
        :return: save the value selected by the user.
        """
        self.lower = value

    def slider2(self, value):
        """
        :param value: will be the number selected by the user for the max threshold.
        :return: save the value selected by the user.
        """
        self.upper = value

    def canny(self):
        """ The Canny method apply the canny algorithms to the image received on __init__
        :return: an image with the edges with some setting by default.
        """
        if self.lower == 0 and self.upper == 0:
            blur = cv2.GaussianBlur(self.gray_image, (3, 3), 0)
            self.edge_image = cv2.Canny(blur, self.low_threshold, self.max_threshold)
            return self.edge_image
        else:
            return self.__canny2()

    def __canny2(self):
        """
        :return: an image with the edges. If the user select some setting call a private method
        to do the same process with the new values.
        """
        blur = cv2.GaussianBlur(self.gray_image, (3, 3), 0)
        self.edge_image = cv2.Canny(blur, self.lower, self.upper)
        return self.edge_image
