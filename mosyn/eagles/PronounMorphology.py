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


class PronounMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0    # Char position for preposition "Categoria".
    __IDX_TYPE = 1    # Char position for preposition "Tipo".
    __IDX_PERSON = 2
    __IDX_GENDER = 3    # Char position for preposition "Genero".
    __IDX_NUMBER = 4    # Char position for preposition "Numbero".
    __IDX_CASE = 5		# Char position for preposition "Genero".
    __IDX_HOLDER = 6		# Char position for preposition "Numbero".
    __IDX_POLITENESS = 7    # Char position for preposition "Forma".

    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(PronounMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'P':
            return self.CAT_PRONOMBRES
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
        if self.get_eagles_label()[self.__IDX_TYPE] == 'P':
            return self.TYPE_PERSONAL
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'D':
            return self.TYPE_DEMOSTRATIVO
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'X':
            return self.TYPE_POSESIVO
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'I':
            return self.TYPE_INDEFINIDO
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'T':
            return self.TYPE_INTERROGATIVO
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'R':
            return self.TYPE_RELATIVO
        else:
            return self.TYPE_UKNOWN
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
        elif self.get_eagles_label()[self.__IDX_NUMBER] == 'N':
            return self.NUMBER_INVARIABLE
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
        if self.get_eagles_label()[self.__IDX_CASE] == 'N':
            return self.CASE_NOMINATIVO
        elif self.get_eagles_label()[self.__IDX_CASE] == 'A':
            return self.CASE_ACUSATIVO
        elif self.get_eagles_label()[self.__IDX_CASE] == 'D':
            return self.CASE_DATIVO
        elif self.get_eagles_label()[self.__IDX_CASE] == 'O':
            return self.CASE_OBLICUO
        else:
            return self.CASE_UKNOWN
    # --------------------------------------------------------------------------

    def get_holder(self):
        """
        ' Returns the Number of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     NUMBER_PLURAL
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_HOLDER] == '1':
            return self.HOLDER_FIRST_PERSON_SINGLE
        elif self.get_eagles_label()[self.__IDX_HOLDER] == '2':
            return self.HOLDER_SECOND_PERSON_SINGLE
        elif self.get_eagles_label()[self.__IDX_HOLDER] == '0':
            return self.HOLDER_THIRD_PERSON
        elif self.get_eagles_label()[self.__IDX_HOLDER] == '4':
            return self.HOLDER_FIRST_PERSON_PLURAL
        elif self.get_eagles_label()[self.__IDX_HOLDER] == '5':
            return self.HOLDER_SECOND_PERSON_PLURAL
        else:
            return self.HOLDER_UKNOWN
    # --------------------------------------------------------------------------

    def get_politeness(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORMA_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_POLITENESS] == 'P':
            return self.POLITENESS_POLITE
        else:
            return self.POLITENESS_UKNOWN
    # --------------------------------------------------------------------------