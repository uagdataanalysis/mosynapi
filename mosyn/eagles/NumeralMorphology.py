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


class NumeralMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0    # Char position for preposition "Categoria".
    __IDX_TYPE = 1    # Char position for preposition "Tipo".
    __IDX_GENDER = 2    # Char position for preposition "Genero".
    __IDX_NUMBER = 3    # Char position for preposition "Numbero".
    __IDX_CASE = 4		# Char position for preposition "Genero".
    __IDX_FUNCTION = 5		# Char position for preposition "Numbero".

    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(NumeralMorphology, self).__init__(forma, lema, label_)
    # --------------------------------------------------------------------------

    def get_category(self):
        """
        ' Returns the category of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     CAT_ADJETIVO
        '
        ' If the category cannot be determined then CAT_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'M':
            return self.CAT_NUMERALES
        else:
            return self.CAT_UNKNOWN
    # --------------------------------------------------------------------------

    def get_type(self):
        """
        ' Returns the type of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     TYPE_CALIFICATIVO
        '
        ' If the category cannot be determined then TYPE_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_TYPE] == 'C':
            return self.TYPE_CARDINAL
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'O':
            return self.TYPE_ORDINAL
        else:
            return self.TYPE_UKNOWN
    # --------------------------------------------------------------------------

    def get_gender(self):
        """
        ' Returns the Gender of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     GENDER_COMMON
        '
        ' If the category cannot be determined then GENDER_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_GENDER] == 'M':
            return self.GENDER_MASCULINO
        elif self.get_eagles_label()[self.__IDX_GENDER] == 'F':
            return self.GENDER_FEMENINO
        elif self.get_eagles_label()[self.__IDX_GENDER] == 'C':
            return self.GENDER_COMUN
        else:
            return self.GENDER_UKNOWN
    # --------------------------------------------------------------------------

    def get_number(self):
        """
        ' Returns the Number of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     NUMBER_PLURAL
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_NUMBER] == 'S':
            return self.NUMBER_SINGULAR
        elif self.get_eagles_label()[self.__IDX_NUMBER] == 'P':
            return self.NUMBER_PLURAL
        else:
            return self.NUMBER_UKNOWN
    # --------------------------------------------------------------------------

    def get_case(self):
        """
        ' Returns the Number of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     NUMBER_PLURAL
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_CASE] == '0':
            return self.CASE_NO_VALUE
        else:
            return self.CASE_UKNOWN
    # --------------------------------------------------------------------------

    def get_function(self):
        """
        ' Returns the Number of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     NUMBER_PLURAL
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_FUNCTION] == 'P':
            return self.FUNCTION_PRONOMINAL
        elif self.get_eagles_label()[self.__IDX_FUNCTION] == 'D':
            return self.FUNCTION_DETERMINANTE
        elif self.get_eagles_label()[self.__IDX_FUNCTION] == 'A':
            return self.FUNCTION_ADJETIVO
        else:
            return self.FUNCTION_UKNOWN
    # --------------------------------------------------------------------------