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
import nltk
import codecs
import os.path as path

from util.io import FileInput
from util.io import FileOutput
from util.io import SystemInput
from util.io import SystemOutput
from util.events import EventHook

__author__ = 'asaelt'
__version__ = '2015.1.0.1'


class MorphologicalAnalysis:
    """ Provides methods to perform a morphological analysis to a text entry.
    """

    def __init__(self, dictionary):
        """ Initializes a new instance of MorphologicalAnalysis.
        :param dictionary: A morphological dictionary.
        :return:
        """
        self.dictionary = dictionary
        self.on_process = EventHook()
        self._cache_dict = {}  # Output Dictionary Cache
        self._template = u' |{0[0]}|{0[1]}|'  # Output Format
        self._default_eagles = u'NP00000'

    def analyze_text(self, value):
        """ Analyzes a piece of text and returns their morphological information.
        :param value: The text to analyse.
        :return: An iterable collection of morphological representation of the text.
        """
        tokens = nltk.word_tokenize(value)

        for token in tokens:  # Iterate over all tokens in the line
            morpho_data = self._cache_dict.get(token)

            if not morpho_data:
                morpho_data = self.dictionary.get_word(token.lower(), [(token.lower(), u'NP00000')])
                self._cache_dict[token] = morpho_data

            formatted = u''
            for morpho_option in morpho_data:
                formatted += self._template.format(morpho_option)

            yield token + formatted + u'\n'


class AnalysisManager:
    """ Provides methods to perform automatic morphological analysis of a set of inputs.
    """

    def __init__(self, dictionary, input_manager, output_manager):
        """ Initializes a new instance of AnalysisManager.
        :param dictionary: A morphological dictionary.
        :param input_manager: An instance of mosyn.util.io.Input as input method.
        :param output_manager: An instance of mosyn.util.io.Output as output method.
        """
        self.on_process = EventHook()
        self.input_manager = input_manager
        self.output_manager = output_manager
        self.analysis = MorphologicalAnalysis(dictionary)

    def start_analysis(self):
        """ Starts the analysis of the input instance with the defined dictionary.
        """
        with self.input_manager, self.output_manager:
            for line in self.input_manager.read():
                for result in self.analysis.analyze_text(line):
                    self.output_manager.write(result)


class MorphologicalDictionary:
    """ Represents a morphological dictionary.
    """

    def __init__(self, filename):
        """ Initializes a new instance of MorphologicalDictionary.
        :param filename: The dictionary filename.
        """
        self.filename = filename
        self.dictionary = {}

    def load(self):
        """ Loads the dictionary filename.
        :return: An instance of mosyn.MorphologicalDictionary.
        """
        with codecs.open(self.filename, mode='r', encoding='utf-8') as f:
            ix = 0
            cache = []
            for line in f:
                if ix == 0:
                    ix += 1
                    continue

                temp = self._parse_line(line)

                if not cache or temp and temp[0] != cache[0]:
                    if cache:
                        self.dictionary[cache[0]] = cache[1]
                        cache = []
                    cache = [temp[0], [temp[1:3]]]
                elif temp and temp[0] == cache[0]:
                    cache[1].append(temp[1:3])

            if cache:
                self.dictionary[cache[0]] = cache[1]

        return self.dictionary

    def get_word(self, value, default=None):
        """ Gets the morphological information of the word.
        :param value: The word value to be find.
        :param default: The morphological information to return if the word is not found.
        :return: The morphological representation of the word.
        """
        temp = self.dictionary.get(value, default)

        if temp:
            return temp
        else:
            return default

    def _parse_line(self, text):
        """ Converts a text to an array of elements.
        :param text: The value to be converted.
        :return: The array representation of the text.
        :raise Exception: if the array does not agree with the dictionary format.
        """
        initial = True
        if initial and text.startswith(u','):
            initial = False
            temp = text.rstrip().split(',')
            items = [',', ',', temp[len(temp)-1]]
        else:
            items = text.rstrip().split(u',')

        if len(items) >= 3:
            return items[0], items[1], items[2]
        else:
            raise Exception('Error on dictionary format')


__dictionary_file = ''
__in_filename = ''
__out_filename = ''
__sys_input = True
__sys_output = True
__help = False


def get_parameters(argv):
    """ Extracts the parameters for an argument array and set them for global use.
    :param argv: The argument array.
    """
    global __dictionary_file
    global __in_filename
    global __out_filename
    global __sys_input
    global __sys_output
    global __help

    for arg in argv:

        if argv.index(arg)+1 < len(argv):
            item = argv[argv.index(arg)+1]
        else:
            item = ''

        if arg == '--dict' and item and not item.startswith('--'):
            __dictionary_file = item
        elif arg == '--ifile' and item and not item.startswith('--'):
            __in_filename = item
            __sys_input = False
        elif arg == '--ofile':
            __sys_output = False
            if item and not item.startswith('--'):
                __out_filename = item
            else:
                __out_filename = get_output_filename(__in_filename)
        elif arg == '--help':
            __help = True


def get_output_filename(filename):
    """ Sets a default name for the output file.
    :param filename: The base filename.
    :return: A filename for a output file.
    """
    ix = filename.rfind('.')
    if 0 >= ix < len(filename)-1:
        return filename[:ix] + '_morphological.' + filename[ix+1:]
    return filename + '_morphological'


def are_valid_parameters():
    """ Validates the input parameters.
    :return: True if parameters are valid
    :raise Exception: if dictionary input or file input are not found.
    """
    if __in_filename:
        if not path.isfile(__in_filename):
            raise Exception(u'Input file not found.')
    elif __dictionary_file:
        if not path.isfile(__dictionary_file):
            raise Exception(u'Dictionary file not found')
    return True


def show_help():
    """ Shows the available options.
    """
    print('----------- MoSyn Ver.'+__version__+' -----------')


def _execute():
    """ Executes the application with the selected parameters.
    """
    input_method = None
    output_method = None
    default_dictionary = ''

    if __sys_input:
        input_method = SystemInput()
    else:
        input_method = FileInput(__in_filename)

    if __sys_output:
        output_method = SystemOutput()
    else:
        output_method = FileOutput(__out_filename)

    if __dictionary_file:
        default_dictionary = __dictionary_file
    else:
        default_dictionary = u'dict\spanish_dict.csv'

    dictionary = MorphologicalDictionary(default_dictionary)
    dictionary.load()

    manager = AnalysisManager(
        dictionary,
        input_method,
        output_method
    )
    manager.start_analysis()


def main(argv):
    """ Main method.
    :param argv: The application arguments.
    """
    get_parameters(argv)

    if __help:
        show_help()
    else:
        try:
            if are_valid_parameters():
                _execute()
            else:
                sys.exit(1)  # If we detect an error then exit
        except Exception as e:
            print(e)

if __name__ == "__main__":  # The Application starts here.
    main(sys.argv)
