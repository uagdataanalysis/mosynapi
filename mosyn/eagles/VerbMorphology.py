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


class VerbMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0		# Char position for preposition "Categoria".
    __IDX_TYPE = 1		# Char position for preposition "Tipo".
    __IDX_MODE = 2		# Char position for preposition "Tipo".
    __IDX_TIME = 3		# Char position for preposition "Genero".
    __IDX_PERSON = 4		# Char position for preposition "Genero".
    __IDX_NUMBER = 5		# Char position for preposition "Numbero".
    __IDX_GENDER = 6		# Char position for preposition "Genero".
    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(VerbMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'V':
            return self.CAT_VERBOS
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
        if self.get_eagles_label()[self.__IDX_TYPE] == 'M':
            return self.TYPE_PRINCIPAL
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'A':
            return self.TYPE_AUXILIAR
        else:
            return self.TYPE_UKNOWN
    # --------------------------------------------------------------------------

    def get_mode(self):
        """
        ' Returns the Number of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     NUMBER_PLURAL
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_MODE] == 'I':
            return self.MODE_INDICATIVO
        elif self.get_eagles_label()[self.__IDX_MODE] == 'S':
            return self.MODE_SUBJUNTIVO
        elif self.get_eagles_label()[self.__IDX_MODE] == 'M':
            return self.MODE_IMPERATIVO
        elif self.get_eagles_label()[self.__IDX_MODE] == 'C':
            return self.MODE_CONDICIONAL
        elif self.get_eagles_label()[self.__IDX_MODE] == 'N':
            return self.MODE_INFINITIVO
        elif self.get_eagles_label()[self.__IDX_MODE] == 'G':
            return self.MODE_GERUNDIO
        elif self.get_eagles_label()[self.__IDX_MODE] == 'P':
            return self.MODE_PARTICIPIO
        else:
            return self.MODE_UKNOWN
    # --------------------------------------------------------------------------

    def get_time(self):
        """
        ' Returns the type of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     TYPE_CALIFICATIVO
        '
        ' If the category cannot be determined then TYPE_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_TIME] == 'P':
            return self.TIME_PRESENT
        elif self.get_eagles_label()[self.__IDX_TIME] == 'I':
            return self.TIME_IMPERFECT
        elif self.get_eagles_label()[self.__IDX_TIME] == 'F':
            return self.TIME_FUTURE
        elif self.get_eagles_label()[self.__IDX_TIME] == 'S':
            return self.TIME_PAST
        else:
            return self.TIME_UKNOWN
    # --------------------------------------------------------------------------

    def get_person(self):
        """
        ' Returns the type of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     TYPE_CALIFICATIVO
        '
        ' If the category cannot be determined then TYPE_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_PERSON] == '1':
            return self.PERSON_FIRST
        elif self.get_eagles_label()[self.__IDX_PERSON] == '2':
            return self.PERSON_SECOND
        elif self.get_eagles_label()[self.__IDX_PERSON] == '3':
            return self.PERSON_THIRD
        else:
            return self.PERSON_UKNOWN
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

    def get_gender(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORMA_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_GENDER] == 'M':
            return self.GENDER_MASCULINO
        elif self.get_eagles_label()[self.__IDX_GENDER] == 'F':
            return self.GENDER_FEMENINO
        else:
            return self.GENDER_UKNOWN
    # --------------------------------------------------------------------------