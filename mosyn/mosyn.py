#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Created on 07/10/2015
# Modified on 20/10/2015
# Modified by asaelt
#
# Source:
# https://github.com/uagdataanalysis/mosynapi
#
# @author: asaelt

import sys
import os
import nltk
import codecs
import os.path as path

from util.io import FileInput
from util.io import FileOutput
from util.io import SystemInput
from util.io import SystemOutput
from util.events import EventHook

__version__ = '1.0.3'


class MorphologicalAnalysis:
    """ Provides methods to perform a morphological analysis to a text entry.
    """

    def __init__(self, dictionary):
        """ Initializes a new instance of MorphologicalAnalysis.
        :param dictionary: A morphological dictionary.
        """
        self.dictionary = dictionary
        self.on_process = EventHook()
        self._cache_dict = {}  # Output Dictionary Cache
        self._default_eagles = u'NP00000'

        self.on_start = EventHook()
        self.on_completed = EventHook()

    def analyze_text(self, value):
        """ Analyzes a piece of text and returns their morphological information.
        :param value: The text to analyse.
        :return: An iterable collection of morphological representation of the text.
        """
        self.on_start.fire(self)

        tokens = nltk.word_tokenize(value)

        for token in tokens:  # Iterate over all tokens in the line
            data = self._cache_dict.get(token)

            if not data:
                data = self.dictionary.get_word(token.lower(), self._default_eagles)
                self._cache_dict[token] = data

            yield [token, data]

        self.on_completed.fire(self)


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

        self.on_start = EventHook()
        self.on_completed = EventHook()

    def start_analysis(self):
        """ Starts the analysis of the input instance with the defined dictionary.
        """
        self.on_start.fire(self)

        with self.input_manager, self.output_manager:
            for line in self.input_manager.read():
                for result in self.analysis.analyze_text(line):
                    self.output_manager.write(result)

        self.on_completed.fire(self)


class MorphologicalDictionary:
    """ Represents a morphological dictionary.
    """

    def __init__(self, filename):
        """ Initializes a new instance of MorphologicalDictionary.
        :param filename: The dictionary filename.
        """
        self.filename = filename
        self.dictionary = {}

        self.on_loaded = EventHook()

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

        self.on_loaded.fire(self)

        return self.dictionary

    def get_word(self, value, default=u'NP00000'):
        """ Gets the morphological information of the word.
        :param value: The word value to be find.
        :param default: The eagles default classification if the word is not found.
        :return: The morphological representation of the word.
        """
        return self.dictionary.get(value, [(value.lower(), default)])

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

        if (arg == '--dictionary' or arg == '-dict') and item and not item.startswith('-'):
            __dictionary_file = item
        elif (arg == '--input-file' or arg == '-in') and item and not item.startswith('-'):
            __in_filename = item
            __sys_input = False
        elif arg == '--output-file' or arg == '-out':
            __sys_output = False
            if item and not item.startswith('-'):
                __out_filename = item
            else:
                __out_filename = get_output_filename(__in_filename)
        elif arg == '--help' or arg == '-h':
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
    print('-------------- MoSyn Ver.'+__version__+' --------------')
    print('Usage:')
    print('  mosyn [options]\n')
    print('General Options:')
    print('  -h, --help             Show help.')
    print('  -in, --input-file      Sets the input file.')
    print('  -out, --input-file     Sets the output file.')
    print('  -dict, --dictionary    Sets a dictionary file.')


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
        d = os.path.dirname(sys.modules['__main__'].__file__)
        resource = os.path.join(d, os.path.join(u'dict', u'spanish_dict.csv'))
        default_dictionary = resource

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
            print(e.message)

if __name__ == "__main__":  # The Application starts here.
    main(sys.argv)
