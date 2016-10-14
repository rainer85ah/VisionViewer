# -*- coding: utf-8 -*-
__author__ = 'Rainer Arencibia'

"""
The MIT License (MIT)

Copyright (c) 2016 Rainer Arencibia

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

"""
Histogram Package contain the files HistogramBuilder.py, Histograms.py & Histograms.ui.
HistogramBuilder.py: have implemented the class HistogramBuilder.
This class will receive an image in (color/gray) and will show a new window with the Histogram of the image
IF is a color image will show:
    red histogram.
    green histogram.
    blue histogram.
    hue histogram
    saturation histogram.
    value histogram.

IF is a gray image will show only:
    value histogram (equalize)

An image histogram is a graphical representation of the tonal distribution
in a digital image. It plots the number of pixels for each tonal value.
By looking at the histogram for a specific image a viewer
will be able to judge the entire tonal distribution at a glance.

The file Histograms.ui it´s the windows create in Qt Designer, to show the histograms of the
different colors. (if you change anything you need to run PYUIC4 to see the new modifications.)
ie:
open a TERMINAL with ROOT privileges.
go to: cd C:\Python27\Lib\site-packages\PyQt4
run: pyuic4 C:\url\Histograms.ui > C:\url\Histograms.py
The file Histograms.py, DO NOT TOUCH. It´s the code generated by PYUIC4 program to translate
the Histogram window in python code.

A image histogram is graphical representation of the colors of the image. Will tell you how many
red, green and blue color have your image. Also can tell you more info about Hue, Saturation and
the Value.
If you want to check more info, you can go to:
http://learn.leighcotnoir.com/artspeak/elements-color/hue-value-saturation/
"""
