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

from .AbbreviationMorphology import AbbreviationMorphology
from .AdjectiveMorphology import AdjectiveMorphology
from .AdverbMorphology import AdverbMorphology
from .ArticleMorphology import ArticleMorphology
from .ConjunctionMorphology import ConjunctionMorphology
from .DeterminantMorphology import DeterminantMorphology
from .InterjectionMorphology import InterjectionMorphology
from .NameMorphology import NameMorphology
from .NumeralMorphology import NumeralMorphology
from .PrepositionMorphology import PrepositionMorphology
from .PronounMorphology import PronounMorphology
from .PunctuationMarkMorphology import PunctuationMarkMorphology
from .VerbMorphology import VerbMorphology


class MorphologyFactory(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    # --------------------------------------------------------------------------

    @staticmethod
    def create_morphology(self, forma, lema, label_):
        """
        Use this method to create the specific Morphology objects; e.g.:
            MorphologyFactory.createMorphology( "SPCMS" )

        This method receives as parameter the Eagles label and returns the
        proper Morphology object based on that.
        """
        if label_[0] == 'A':
            return AdjectiveMorphology(forma, lema, label_)
        elif label_[0] == 'R':
            return AdverbMorphology(forma, lema, label_)
        elif label_[0] == 'T':
            return ArticleMorphology(forma, lema, label_)
        elif label_[0] == 'D':
            return DeterminantMorphology(forma, lema, label_)
        elif label_[0] == 'N':
            return NameMorphology(forma, lema, label_)
        elif label_[0] == 'V':
            return VerbMorphology(forma, lema, label_)
        elif label_[0] == 'P':
            return PronounMorphology(forma, lema, label_)
        elif label_[0] == 'C':
            return ConjunctionMorphology(forma, lema, label_)
        elif label_[0] == 'M':
            return NumeralMorphology(forma, lema, label_)
        elif label_[0] == 'I':
            return InterjectionMorphology(forma, lema, label_)
        elif label_[0] == 'Y':
            return AbbreviationMorphology(forma, lema, label_)
        elif label_[0] == 'S':
            return PrepositionMorphology(forma, lema, label_)
        elif label_[0] == 'F':
            return PunctuationMarkMorphology(forma, lema, label_)
        else:
            raise NotImplementedError()
    # --------------------------------------------------------------------------