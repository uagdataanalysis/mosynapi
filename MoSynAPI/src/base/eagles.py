#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Created on 07/10/2015
# Modified on 20/10/2015
# Modified by asaelt
#
# This class is based on the definition of the Eagles Labeling standard:
# http://www.cs.upc.edu/~nlp/tools/parole-sp.html
#
# @author: axelg

__author__ = 'axelg'


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


class AbstractMorphology(object):
    '''
    '' Public "constants" for Eagles label Category:
    '''
    __CAT_INIT = 0
    CAT_UNKNOWN = __CAT_INIT + 1
    CAT_ADJECTIVE = __CAT_INIT + 2
    CAT_ADVERB = __CAT_INIT + 3
    CAT_ARTICLE = __CAT_INIT + 4
    CAT_DETERMINANT = __CAT_INIT + 5
    CAT_NAMES = __CAT_INIT + 6
    CAT_VERBS = __CAT_INIT + 7
    CAT_PRONOUNS = __CAT_INIT + 8
    CAT_CONJUNCTIONS = __CAT_INIT + 9
    CAT_NUMERALS = __CAT_INIT + 10
    CAT_INTERJECTION = __CAT_INIT + 11
    CAT_ABBREVIATIONS = __CAT_INIT + 12
    CAT_ADPOSITION = __CAT_INIT + 13
    CAT_PUNCTUATION = __CAT_INIT + 14
    #--------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Type:
    '''
    __TYPE_INIT = __CAT_INIT + 100
    TYPE_UNKNOWN = __TYPE_INIT + 1
    TYPE_CALIFICATIVO = __TYPE_INIT + 2
    TYPE_PREPOSICION = __TYPE_INIT + 3
    TYPE_GENERAL = __TYPE_INIT + 4
    TYPE_DEFINIDO = __TYPE_INIT + 5
    TYPE_DEMOSTRATIVO = __TYPE_INIT + 6
    TYPE_POSESIVO = __TYPE_INIT + 7
    TYPE_INTERROGATIVO = __TYPE_INIT + 8
    TYPE_EXCLAMATIVO = __TYPE_INIT + 9
    TYPE_INDEFINIDO = __TYPE_INIT + 10
    TYPE_COMUN = __TYPE_INIT + 11
    TYPE_PROPIO = __TYPE_INIT + 12
    TYPE_PRINCIPAL = __TYPE_INIT + 13
    TYPE_AUXILIAR = __TYPE_INIT + 14
    TYPE_PERSONAL = __TYPE_INIT + 15
    TYPE_RELATIVO = __TYPE_INIT + 16
    TYPE_COORDINADA = __TYPE_INIT + 17
    TYPE_SUBORDINADA = __TYPE_INIT + 18
    TYPE_CARDINAL = __TYPE_INIT + 19
    TYPE_ORDINAL =__TYPE_INIT + 20
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Degree:
    '''
    __DEGREE_INIT = __TYPE_INIT + 100
    DEGREE_UKNOWN = __DEGREE_INIT + 1
    DEGREE_APRECIATIVO = __DEGREE_INIT + 2
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Gender:
    '''
    __GENDER_INIT = __DEGREE_INIT + 100
    GENDER_UKNOWN = __GENDER_INIT + 1
    GENDER_MASCULINO = __GENDER_INIT + 2
    GENDER_FEMENINO = __GENDER_INIT + 3
    GENDER_COMUN = __GENDER_INIT + 4
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Number:
    '''
    __NUMBER_INIT = __GENDER_INIT + 100
    NUMBER_UNKNOWN = __NUMBER_INIT + 1
    NUMBER_SINGULAR = __NUMBER_INIT + 2
    NUMBER_PLURAL = __NUMBER_INIT + 3
    NUMBER_INVARIABLE = __NUMBER_INIT + 4
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Case:
    '''
    __CASE_INIT = __NUMBER_INIT + 100
    CASE_UKNOWN = __CASE_INIT + 1
    CASE_NO_VALUE = __CASE_INIT + 2
    CASE_NOMINATIVO = __CASE_INIT + 3
    CASE_ACUSATIVO = __CASE_INIT + 4
    CASE_DATIVO = __CASE_INIT + 5
    CASE_OBLICUO = __CASE_INIT + 6
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Forma:
    '''
    __FORMA_INIT = __CASE_INIT + 100
    FORM_UNKNOWN = __FORMA_INIT + 1
    FORM_SIMPLE = __FORMA_INIT + 2
    FORM_CONTRAIDA = __FORMA_INIT + 3
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Function:
    '''
    __FUNCTION_INIT = __FORMA_INIT + 100
    FUNCTION_UKNOWN = __FUNCTION_INIT + 1
    FUNCTION_PARTICIPLE = __FUNCTION_INIT + 2
    FUNCTION_PRONOMINAL = __FUNCTION_INIT + 3
    FUNCTION_DETERMINANTE = __FUNCTION_INIT + 4
    FUNCTION_ADJETIVO = __FUNCTION_INIT + 5
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Function:
    '''
    __PERSON_INIT = __FUNCTION_INIT + 100
    PERSON_UKNOWN = __PERSON_INIT + 1
    PERSON_FIRST = __PERSON_INIT + 2
    PERSON_SECOND = __PERSON_INIT + 3
    PERSON_THIRD = __PERSON_INIT + 4
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Function:
    '''
    __HOLDER_INIT = __PERSON_INIT + 100
    HOLDER_UKNOWN = __HOLDER_INIT + 1
    HOLDER_FIRST_PERSON_SINGLE = __HOLDER_INIT + 2
    HOLDER_SECOND_PERSON_SINGLE = __HOLDER_INIT + 3
    HOLDER_THIRD_PERSON = __HOLDER_INIT + 4
    HOLDER_FIRST_PERSON_PLURAL = __HOLDER_INIT + 5
    HOLDER_SECOND_PERSON_PLURAL = __HOLDER_INIT + 6
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Function:
    '''
    __SEMANTIC_GENDER_INIT = __HOLDER_INIT + 100
    SEMANTIC_GENDER_UKNOWN = __SEMANTIC_GENDER_INIT + 1
    SEMANTIC_GENDER_NO_VALUE = __SEMANTIC_GENDER_INIT + 2
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Function:
    '''
    __MODE_INIT = __SEMANTIC_GENDER_INIT + 100
    MODE_UKNOWN = __MODE_INIT + 1
    MODE_INDICATIVO = __MODE_INIT + 2
    MODE_SUBJUNTIVO = __MODE_INIT + 3
    MODE_IMPERATIVO = __MODE_INIT + 4
    MODE_CONDICIONAL = __MODE_INIT + 5
    MODE_INFINITIVO = __MODE_INIT + 6
    MODE_GERUNDIO = __MODE_INIT + 7
    MODE_PARTICIPIO = __MODE_INIT + 8
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Function:
    '''
    __TIME_INIT = __MODE_INIT + 100
    TIME_UKNOWN = __TIME_INIT + 1
    TIME_PRESENT = __TIME_INIT + 2
    TIME_IMPERFECT = __TIME_INIT + 3
    TIME_FUTURE = __TIME_INIT + 4
    TIME_PAST = __TIME_INIT + 5
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Function:
    '''
    __POLITENESS_INIT = __TIME_INIT + 100
    POLITENESS_UKNOWN = __POLITENESS_INIT + 1
    POLITENESS_POLITE = __POLITENESS_INIT + 2
    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label):
        '''
        Constructor
        '''
        self.__forma = forma
        self.__lema = lema
        self.__label = label
    # --------------------------------------------------------------------------

    def __str__(self):
        return self.__forma + " " + self.__lema + "" + self.__label
    # --------------------------------------------------------------------------

    def get_form(self):
        """
        ' Returns the word being analyzed in its raw form; e.g.:
        '    alegres
        '
        'return String
        """
        return self.__form
    #--------------------------------------------------------------------------
    
    
    
    def get_lema(self):
        """
        ' Returns the root of the word being analyzed; e.g.:
        '    alegre
        '
        ' return String
        """
        return self.__lema
    #--------------------------------------------------------------------------
    
    
    
    def get_eagles_label(self):
        """
        ' Returns the Eagles label that corresponds to the word being analyzed; e.g.:
        '    AQ0CP00
        '
        ' return String
        """
        return self.__label
    #--------------------------------------------------------------------------
    
    
    
    def get_category(self):
        """
        ' Returns the category of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     CAT_ADJECTIVE
        '
        ' If the category cannot be determined then CAT_UNKNOWN is returned.
        ' return Integer
        """
        return self.CAT_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_type(self):
        """
        ' Returns the type of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     TYPE_CALIFICATIVO
        '
        ' If the category cannot be determined then TYPE_UNKNOWN is returned.
        ' return Integer
        """
        return self.TYPE_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_degree(self):
        """
        ' Returns the Degree of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     DEGREE_UNKNOWN
        '
        ' If the category cannot be determined then DEGREE_UNKNOWN is returned.
        ' return Integer
        """
        return self.DEGREE_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_gender(self):
        """
        ' Returns the Gender of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     GENDER_COMMON
        '
        ' If the category cannot be determined then GENDER_UNKNOWN is returned.
        ' return Integer
        """
        return self.GENDER_UKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_number(self):
        """
        ' Returns the Number of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     NUMBER_PLURAL
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        return self.NUMBER_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_case(self):
        """
        ' Returns the Case of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     NUMBER_PLURAL
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        return self.CASE_UKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_label_form(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORMA_CONTRAIDA
        '
        ' If the category cannot be determined then FORM_UNKNOWN is returned.
        ' return Integer
        """
        return self.FORM_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_rol(self):
        """
        ' Returns the type of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     TYPE_CALIFICATIVO
        '
        ' If the category cannot be determined then TYPE_UNKNOWN is returned.
        ' return Integer
        """
        return self.ROL_UNKNOWN
    #--------------------------------------------------------------------------
    
    '''
    '' Several methods pending to be defined. 
    '''


'''
Created on 13/10/2015

This class is meant to be used when parsing Abbreviation Eagles labels.

@author: axelg
'''

class AbbreviationMorphology(AbstractMorphology):
    '''
    classdocs
    '''


    def __init__(self, form, lema, label_):
        '''
        Constructor
        '''
        super(AbbreviationMorphology, self).__init__( form, lema, label_)
    #--------------------------------------------------------------------------
    
    
    
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
    #--------------------------------------------------------------------------


class AdjectiveMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0		# Char position for preposition "Categoria".
    __IDX_TYPE = 1		# Char position for preposition "Tipo".
    __IDX_DEGREE = 2		# Char position for preposition "Genero".
    __IDX_GENDER = 3		# Char position for preposition "Genero".
    __IDX_NUMBER = 4		# Char position for preposition "Numbero".
    __IDX_CASE = 5		# Char position for preposition "Genero".
    __IDX_FUNCTION = 6		# Char position for preposition "Numbero".
    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(AdjectiveMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'A':
            return self.CAT_ADJETIVO
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
        if self.get_eagles_label()[self.__IDX_TYPE] == 'Q':
            return self.TYPE_CALIFICATIVO
        else:
            return self.TYPE_UNKNOWN
    # --------------------------------------------------------------------------

    def get_degree(self):
        """
        ' Returns the type of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     TYPE_CALIFICATIVO
        '
        ' If the category cannot be determined then TYPE_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_DEGREE] == 'A':
            return self.DEGREE_APRECIATIVO
        else:
            return self.DEGREE_UKNOWN
    # --------------------------------------------------------------------------

    def get_gender(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORM_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
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
            return self.NUMBER_UNKNOWN
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
            return self.FUNCTION_PARTICIPLE
        else:
            return self.FUNCTION_UKNOWN
    # --------------------------------------------------------------------------


class AdverbMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0		# Char position for preposition "Categoria".
    __IDX_TYPE = 1		# Char position for preposition "Tipo".
    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(AdverbMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'R':
            return self.CAT_ADVERBIO
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
        if self.get_eagles_label()[self.__IDX_TYPE] == 'G':
            return self.TYPE_GENERAL
        else:
            return self.TYPE_UNKNOWN
    # --------------------------------------------------------------------------


class ArticleMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0		# Char position for preposition "Categoria".
    __IDX_TYPE = 1		# Char position for preposition "Tipo".
    __IDX_GENDER = 2		# Char position for preposition "Genero".
    __IDX_NUMBER = 3		# Char position for preposition "Numbero".
    __IDX_CASE = 4		# Char position for preposition "Genero".
    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(ArticleMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'T':
            return self.CAT_ARTICULOS
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
        if self.get_eagles_label()[self.__IDX_TYPE] == 'D':
            return self.TYPE_DEFINIDO
        else:
            return self.TYPE_UNKNOWN
    # --------------------------------------------------------------------------

    def get_gender(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORM_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
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
            return self.NUMBER_UNKNOWN
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


class ConjunctionMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0    # Char position for preposition "Categoria".
    __IDX_TYPE = 1    # Char position for preposition "Tipo".

    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(ConjunctionMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'C':
            return self.CAT_CONJUNCIONES
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
            return self.TYPE_COORDINADA
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'S':
            return self.TYPE_SUBORDINADA
        else:
            return self.TYPE_UNKNOWN
    # --------------------------------------------------------------------------


class DeterminantMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0		# Char position for preposition "Categoria".
    __IDX_TYPE = 1		# Char position for preposition "Tipo".
    __IDX_PERSON = 2		# Char position for preposition "Genero".
    __IDX_GENDER = 3		# Char position for preposition "Genero".
    __IDX_NUMBER = 4		# Char position for preposition "Numbero".
    __IDX_CASE = 5		# Char position for preposition "Genero".
    __IDX_HOLDER = 6		# Char position for preposition "Numbero".
    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(DeterminantMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'D':
            return self.CAT_DETERMINANTES
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
        if self.get_eagles_label()[self.__IDX_TYPE] == 'D':
            return self.TYPE_DEMOSTRATIVO
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'P':
            return self.TYPE_POSESIVO
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'T':
            return self.TYPE_INTERROGATIVO
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'E':
            return self.TYPE_EXCLAMATIVO
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'I':
            return self.TYPE_INDEFINIDO
        else:
            return self.TYPE_UNKNOWN
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
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORM_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
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
            return self.NUMBER_UNKNOWN
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


class InterjectionMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    def __init__(self, form, lema, label_):
        '''
        Constructor
        '''
        super(InterjectionMorphology, self).__init__(form, lema, label_)
    # --------------------------------------------------------------------------

    def get_category(self):
        """
        ' Returns the category of the word based on the Eagles label; e.g.:
        '    Eagles Label: I0000
        '    Category:     CAT_INTERJECTION
        '
        ' CAT_INTERJECTION is returned all the time since InterjectionMorphology
        '  class is meant to model interjections only. If the label is not
        ' an abbreviation please do not use this class.
        """
        return self.CAT_INTERJECTION
    # --------------------------------------------------------------------------


class NameMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0		# Char position for preposition "Categoria".
    __IDX_TYPE = 1		# Char position for preposition "Tipo".
    __IDX_GENDER = 2 	# Char position for preposition "Genero".
    __IDX_NUMBER = 3		# Char position for preposition "Numbero".
    __IDX_CASE = 4		# Char position for preposition "Genero".
    __IDX_SEMANTIC_GENDER = 5		# Char position for preposition "Numbero".
    __IDX_DEGREE = 6		# Char position for preposition "Genero".
    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(NameMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'N':
            return self.CAT_NOMBRES
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
            return self.TYPE_COMUN
        elif self.get_eagles_label()[self.__IDX_TYPE] == 'P':
            return self.TYPE_PROPIO
        else:
            return self.TYPE_UNKNOWN
    # --------------------------------------------------------------------------

    def get_gender(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORM_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
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
            return self.NUMBER_UNKNOWN
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

    def get_semantic_gender(self):
        """
        ' Returns the Number of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     NUMBER_PLURAL
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_SEMANTIC_GENDER] == '0':
            return self.SEMANTIC_GENDER_NO_VALUE
        else:
            return self.SEMANTIC_GENDER_UKNOWN
    # --------------------------------------------------------------------------

    def get_degree(self):
        """
        ' Returns the type of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     TYPE_CALIFICATIVO
        '
        ' If the category cannot be determined then TYPE_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_DEGREE] == 'A':
            return self.DEGREE_APRECIATIVO
        else:
            return self.DEGREE_UKNOWN
    # --------------------------------------------------------------------------


'''
Created on 20/10/2015

@author: axelg
'''
class NumeralMorphology(AbstractMorphology):
    '''
    classdocs
    '''
    
    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0  # Char position for "Categoria". 
    __IDX_TYPE = 1      # Char position for "Tipo". 
    __IDX_GENDER = 2    # Char position for "Genero". 
    __IDX_NUMBER = 3    # Char position for "Numbero". 
    __IDX_CASE = 4      # Char position for "Forma". 
    __IDX_ROL = 5       # Char position for "Funcion". 
    #--------------------------------------------------------------------------


    def __init__(self, form, lema, label_):
        '''
        Constructor
        '''
        super(NumeralMorphology, self).__init__( form, lema, label_)
    #--------------------------------------------------------------------------
    
    
    
    def get_category(self):
        """
        ' Returns the category of the word based on the Eagles label; e.g.:
        '    Eagles Label: MCCP00
        '    Category:     CAT_NUMERALS
        '
        ' CAT_NUMERALS is returned all the time since NumeralMorphology
        '  class is meant to model numerals only. If the label is not 
        ' an abbreviation please do not use this class.
        """
        return self.CAT_NUMERALS
    #--------------------------------------------------------------------------
    
    
    
    
    def get_type(self):
        """
        ' Returns the type of the word based on the Eagles label; e.g.:
        '    Eagles Label: MCCP00
        '    Category:     TYPE_CARDINAL
        '
        ' Possible return values are:
        '    - TYPE_CARDINAL
        '    - TYPE_ORDINAL
        '
        ' If the category cannot be determined then TYPE_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[ self.__IDX_TYPE ] == 'C':
            return self.TYPE_CARDINAL
        elif self.get_eagles_label()[ self.__IDX_TYPE ] == 'O':
            return self.TYPE_ORDINAL
        else:
            return self.TYPE_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_rol(self):
        """
        ' Returns the type of the word based on the Eagles label; e.g.:
        '    Eagles Label: MCCP0D
        '    Category:     ROL_DETERMINANT
        '
        ' Possible return values are:
        '    - ROL_ADJECTIVE
        '    - ROL_DETERMINANT
        '    - ROL_PRONOMINAL
        '    - ROL_UNKNOWN
        '
        ' If the category cannot be determined then TYPE_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[ self.__IDX_ROL ] == 'A':
            return self.ROL_ADJECTIVE
        elif self.get_eagles_label()[ self.__IDX_ROL ] == 'D':
            return self.ROL_DETERMINANT
        elif self.get_eagles_label()[ self.__IDX_ROL ] == 'P':
            return self.ROL_PRONOMINAL
        else:
            return self.ROL_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_case(self):
        """
        ' Returns the Case of the word based on the Eagles label; e.g.:
        '    Eagles Label: MCCP00
        '    Category:     CASE_UKNOWN
        '
        ' CASE_UKNOWN is returned all the time.
        ' return Integer
        """
        return self.CASE_UKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_label_form(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: MCCP00
        '    Category:     FORM_UNKNOWN
        '
        ' FORM_UNKNOWN is returned all the time.
        ' return Integer
        """
        return self.FORM_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_gender(self):
        """
        ' Returns the Gender of the word based on the Eagles label; e.g.:
        '    Eagles Label: MCMP00
        '    Category:     GENDER_MALE
        '
        ' Possible return values are:
        '    - GENDER_MALE
        '    - GENDER_FEMALE
        '    - GENDER_COMMON
        '    - GENDER_UKNOWN
        '
        ' If the category cannot be determined then GENDER_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[ self.__IDX_GENDER ] == 'M':
            return self.GENDER_MALE
        elif self.get_eagles_label()[ self.__IDX_GENDER ] == 'F':
            return self.GENDER_FEMALE
        elif self.get_eagles_label()[ self.__IDX_GENDER ] == 'C':
            return self.GENDER_COMMON
        else:
            return self.GENDER_UKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_number(self):
        """
        ' Returns the Number of the word based on the Eagles label; e.g.:
        '    Eagles Label: MCMP00
        '    Category:     NUMBER_PLURAL
        '
        ' Possible return values are:
        '    - NUMBER_SINGULAR
        '    - NUMBER_PLURAL
        '    - NUMBER_UKNOWN
        '
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[ self.__IDX_NUMBER ] == 'S':
            return self.NUMBER_SINGULAR
        elif self.get_eagles_label()[ self.__IDX_NUMBER ] == 'P':
            return self.NUMBER_PLURAL
        else:
            return self.NUMBER_UKNOWN
    #--------------------------------------------------------------------------


class PrepositionMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0    # Char position for preposition "Categoria".
    __IDX_TYPE = 1    # Char position for preposition "Tipo".
    __IDX_FORM = 2    # Char position for preposition "Forma".
    __IDX_GENDER = 3    # Char position for preposition "Genero".
    __IDX_NUMBER = 4    # Char position for preposition "Numbero".
    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(PrepositionMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'S':
            return self.CAT_ADPOSICION
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
            return self.TYPE_PREPOSICION
        else:
            return self.TYPE_UNKNOWN
    # --------------------------------------------------------------------------

    def get_label_form(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORM_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_FORM] == 'S':
            return self.FORM_SIMPLE
        elif self.get_eagles_label()[self.__IDX_FORM] == 'C':
            return self.FORM_CONTRAIDA
        else:
            return self.FORM_UNKNOWN
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
        else:
            return self.NUMBER_UNKNOWN
    # --------------------------------------------------------------------------


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
            return self.TYPE_UNKNOWN
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
            return self.NUMBER_UNKNOWN
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
        '    Category:     FORM_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[self.__IDX_POLITENESS] == 'P':
            return self.POLITENESS_POLITE
        else:
            return self.POLITENESS_UKNOWN
    # --------------------------------------------------------------------------


class PunctuationMarkMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0    # Char position for preposition "Categoria".

    # --------------------------------------------------------------------------

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(PunctuationMarkMorphology, self).__init__(forma, lema, label_)
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
        if self.get_eagles_label()[self.__IDX_CATEGORY] == 'F':
            return self.CAT_PUNTUACION
        else:
            return self.CAT_UNKNOWN
    # --------------------------------------------------------------------------


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
            return self.TYPE_UNKNOWN
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
            return self.NUMBER_UNKNOWN
    # --------------------------------------------------------------------------

    def get_gender(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORM_CONTRAIDA
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
