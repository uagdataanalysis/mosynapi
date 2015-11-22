#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Created on 07/10/2015
# Modified on 20/10/2015
# Modified by asaelt
#
# Source:
# https://github.com/uagdataanalysis/mosynapi
#
# This class is based on the definition of the Eagles Labeling standard:
# http://www.cs.upc.edu/~nlp/tools/parole-sp.html
#
# @author: asaelt

import sys
import codecs

from .format import format_morphological_data


class Input(object):
    """ Provides methods to read from an input.
    """
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def read(self):
        """ Read a value from the input.
        """
        pass


class Output(object):
    """ Provides methods to write to an output.
    """
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def write(self, value):
        """ Writes a value in the output.
        :param value: The value to be written.
        """
        pass


class FileInput(Input):
    """ Provides methods to read from a file input.
    """
    def __init__(self, filename):
        """ Initializes a new instance of FileInput.
        """
        super(Input, self).__init__()
        self.filename = filename

    def __enter__(self):
        self.input_file = codecs.open(self.filename, mode='r', encoding='utf-8')
        return self.input_file

    def __exit__(self, type, value, traceback):
        self.input_file.close()

    def read(self):
        """ Read a value from the file input.
        :return: An iterable collection of text lines read from the file input.
        """
        for line in self.input_file:
            yield line


class FileOutput(Output):
    """ Provides methods to write to a file output.
    """
    def __init__(self, filename):
        """ Initializes a new instance of FileOutput.
        """
        super(Output, self).__init__()
        self.filename = filename
        self.output_template = u' |{0[0]}|{0[1]}|'

    def __enter__(self):
        self.output_file = codecs.open(self.filename, mode='w', encoding='utf-8')
        return self.output_file

    def __exit__(self, type, value, traceback):
        self.output_file.close()

    def write(self, value):
        """ Writes a value in the file output.
        :param value: The value to be written.
        """
        self.output_file.write(format_morphological_data(value, self.output_template))


class SystemInput(Input):
    """ Provides methods to read from the standard input.
    """
    def __init__(self):
        """ Initializes a new instance of SystemInput.
        """
        super(Input, self).__init__()

    def read(self):
        """ Read a value from the standard input.
        :return: An iterable collection of text lines read from the standard input.
        """
        
        yield raw_input( "% " )


class SystemOutput(Output):
    """ Provides methods to write in the standard output.
    """
    def __init__(self):
        """ Initializes a new instance of SystemOutput.
        """
        super(Output, self).__init__()
        self.output_template = u' |{0[0]}|{0[1]}|'

    def write(self, value):
        """ Writes a value in the standard output.
        :param value: The value to be written.
        """
        sys.stdout.write(format_morphological_data(value, self.output_template))
