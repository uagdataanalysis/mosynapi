#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Created on 14/11/2015
# Modified on 14/11/2015
# Modified by asaelt
#
# This class is based on the definition of the Eagles Labeling standard:
# http://www.cs.upc.edu/~nlp/tools/parole-sp.html
#
# Source:
# https://github.com/uagdataanalysis/mosynapi
#
# @author: axelg

from .AbstractMorphology import AbstractMorphology


class AbbreviationMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    def __init__(self, form, lema, label_):
        '''
        Constructor
        '''
        super(AbbreviationMorphology, self).__init__(form, lema, label_)
    # --------------------------------------------------------------------------

    def get_category(self):
        """
        ' Returns the category of the word based on the Eagles label; e.g.:
        '    Eagles Label: Y0000
        '    Category:     CAT_ABBREVIATIONS
        '
        ' CAT_ADPOSITION is returned all the time since AbbreviationMorphology
        '  class is meant to model abbreviations only. If the label is not
        ' an abbreviation please do not use this class.
        """
        return self.CAT_ABBREVIATIONS
    # --------------------------------------------------------------------------
