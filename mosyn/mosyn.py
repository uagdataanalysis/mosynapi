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
import pandas as pd
import os.path as path

from util.events import EventHook
from util.io import FileInput
from util.io import FileOutput
from util.io import SystemInput
from util.io import SystemOutput

__author__ = 'Arturo Asael'
__version__ = '1.0.0.0'


class MorphologicalAnalisys:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.on_process = EventHook()
        self._cache_dict = {}  # Output Dictionary Cache
        self._template = u' |{0[0]}|{0[1]}|'  # Output Format
        self._default_eagles = u'NP00000'

    def analyze_text(self, value):

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

    def __init__(self, dictionary, input_manager, output_manager):
        self.on_process = EventHook()
        self.input_manager = input_manager
        self.output_manager = output_manager
        self.analysis = MorphologicalAnalisys(dictionary)

    def start_analysis(self):
        with self.input_manager, self.output_manager:
            for line in self.input_manager.read():
                for result in self.analysis.analyze_text(line):
                    self.output_manager.write(result)


class DictionaryLoader:

    def __init__(self):
        pass

    @staticmethod
    def load_dictionary(filename):
        """
        A helper function to load our dictionary using pandas
         param csv_path path to csv dictionary

        returns a pandas dataframe object ready to do queries using 'get_word' method
        """
        dictionary = pd.read_csv(filename, quotechar=u"'", escapechar=u"\\", encoding=u'utf-8')
        dictionary.set_index(u'word', inplace=True)

        def get_word(value, default=None):
            try:
                default = dictionary.loc[value]
                if isinstance(default, pd.core.frame.DataFrame):
                    default = default.to_dict(u'list')
                    default = zip(default[u'root'], default[u'eagles'])
                else:
                    default = default.to_dict()
                    default = [(default[u'root'], default[u'eagles'])]
            except KeyError:
                pass

            return default

        dictionary.get_word = get_word
        return dictionary


__dictionary_file = ''
__in_filename = ''
__out_filename = ''
__sys_input = True
__sys_output = True
__help = False


def get_parameters(argv):
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
    ix = filename.rfind('.')
    if 0 >= ix < len(filename)-1:
        return filename[:ix] + '_morphological.' + filename[ix+1:]
    return filename + '_morphological'


def are_valid_parameters():
    if __in_filename:
        if not path.isfile(__in_filename):
            raise Exception(u'Input file not found.')
    elif __dictionary_file:
        if not path.isfile(__dictionary_file):
            raise Exception(u'Dictionary file not found')
    return True


def show_help():
    print('----------- MoSyn Ver.'+__version__+' -----------')


def execute():
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

    dictionary = DictionaryLoader.load_dictionary(default_dictionary)

    manager = AnalysisManager(
        dictionary,
        input_method,
        output_method
    )
    manager.start_analysis()


def main(argv):
    get_parameters(argv)

    if __help:
        show_help()
    else:
        try:
            if are_valid_parameters():
                execute()
            else:
                sys.exit(1)  # If we detect an error then exit
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main(sys.argv)
