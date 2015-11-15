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


class AbstractMorphology(object):
    '''
    '' Public "constants" for Eagles label Category:
    '''
    __CAT_INIT = 0
    CAT_UNKNOWN = __CAT_INIT + 1
    CAT_ADJETIVO = __CAT_INIT + 2
    CAT_ADVERBIO = __CAT_INIT + 3
    CAT_ARTICULOS = __CAT_INIT + 4
    CAT_DETERMINANTES = __CAT_INIT + 5
    CAT_NOMBRES = __CAT_INIT + 6
    CAT_VERBOS = __CAT_INIT + 7
    CAT_PRONOMBRES = __CAT_INIT + 8
    CAT_CONJUNCIONES = __CAT_INIT + 9
    CAT_NUMERALES = __CAT_INIT + 10
    CAT_INTERJECCIONES = __CAT_INIT + 11
    CAT_ABREVIATURAS = __CAT_INIT + 12
    CAT_ADPOSICION = __CAT_INIT + 13
    CAT_PUNTUACION = __CAT_INIT + 14
    # --------------------------------------------------------------------------

    '''
    '' Public "constants" for Eagles label Type:
    '''
    __TYPE_INIT = __CAT_INIT + 100
    TYPE_UKNOWN = __TYPE_INIT + 1
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
    NUMBER_UKNOWN = __NUMBER_INIT + 1
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
    FORMA_UKNOWN = __FORMA_INIT + 1
    FORMA_SIMPLE = __FORMA_INIT + 2
    FORMA_CONTRAIDA = __FORMA_INIT + 3
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
        return self.__forma
    # --------------------------------------------------------------------------

    def get_lema(self):
        """
        ' Returns the root of the word being analyzed; e.g.:
        '    alegre
        '
        ' return String
        """
        return self.__lema
    # --------------------------------------------------------------------------

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
        '    Category:     CAT_ADJETIVO
        '
        ' If the category cannot be determined then CAT_UNKNOWN is returned.
        ' return Integer
        """
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
        return self.TYPE_UNKNOWN
    # --------------------------------------------------------------------------

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
        return self.NUMBER_UKNOWN
    # --------------------------------------------------------------------------

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
    # --------------------------------------------------------------------------

    def get_forma(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORMA_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
        ' return Integer
        """
        return self.FORMA_UNKNOWN
    # --------------------------------------------------------------------------

    '''
    '' Several methods pending to be defined.
    '''