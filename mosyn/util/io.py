#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Created on 07/10/2015
# Modified on 20/10/2015
# Modified by asaelt
#
# This class is based on the definition of the Eagles Labeling standard:
# http://www.cs.upc.edu/~nlp/tools/parole-sp.html
#
# @author: asaelt

import sys
import codecs

from eagles import MorphologyFactory

__author__ = 'Arturo Asael'


class Input(object):
    """description of class"""
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def read(self):
        pass


class Output(object):
    """description of class"""
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def write(self, value):
        pass


class FileInput(Input):

    """description of class"""
    def __init__(self, filename):
        super(Input, self).__init__()
        self.filename = filename

    def __enter__(self):
        self.input_file = codecs.open(self.filename, mode='r', encoding='utf-8')
        return self.input_file

    def __exit__(self, type, value, traceback):
        self.input_file.close()

    def read(self):
        for line in self.input_file:
            yield line


class FileOutput(Output):
    """description of class"""
    def __init__(self, filename):
        super(Output, self).__init__()
        self.filename = filename

    def __enter__(self):
        self.output_file = codecs.open(self.filename, mode='w', encoding='utf-8')
        return self.output_file

    def __exit__(self, type, value, traceback):
        self.output_file.close()

    def write(self, value):
        self.output_file.write(value)


class SystemInput(Input):

    def __init__(self):
        pass

    def read(self):
        for line in sys.stdin:
            yield line


class SystemOutput(Output):

    def __init__(self):
        super(Output, self).__init__()

    def write(self, value):
        sys.stdout.write(value)
