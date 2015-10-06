'''
Created on 04/10/2015

This class is based on the definition of the Eagles Labeling standard:
http://www.cs.upc.edu/~nlp/tools/parole-sp.html

@author: axelg
'''

class AbstractMorphology(object):
    '''
    '' Public "constants" for Eagles label Category:
    '''
    __CAT_INIT        = 0
    CAT_UNKNOWN       = __CAT_INIT + 1
    CAT_ADJETIVO      = __CAT_INIT + 2
    CAT_ADVERBIO      = __CAT_INIT + 3
    CAT_ARTICULOS     = __CAT_INIT + 4
    CAT_DETERMINANTES = __CAT_INIT + 5
    CAT_NOMBRES       = __CAT_INIT + 6
    CAT_VERBOS        = __CAT_INIT + 7
    CAT_PRONOMBRES    = __CAT_INIT + 8
    CAT_CONJUNCIONES  = __CAT_INIT + 9
    CAT_NUMERALES     = __CAT_INIT + 10
    CAT_INTERJECCIONES= __CAT_INIT + 11
    CAT_ABREVIATURAS  = __CAT_INIT + 12
    CAT_ADPOSICION = __CAT_INIT + 13
    CAT_PUNTUACION    = __CAT_INIT + 14
    #--------------------------------------------------------------------------
    
    '''
    '' Public "constants" for Eagles label Type:
    '''
    __TYPE_INIT = __CAT_INIT + 100
    TYPE_UKNOWN       = __TYPE_INIT + 1
    TYPE_CALIFICATIVO = __TYPE_INIT + 2
    TYPE_PREPOSICION  = __TYPE_INIT + 3
    #--------------------------------------------------------------------------
    
    '''
    '' Public "constants" for Eagles label Degree:
    '''
    __DEGREE_INIT = __TYPE_INIT + 100
    DEGREE_UKNOWN      = __DEGREE_INIT + 1
    DEGREE_APRECIATIVO = __DEGREE_INIT + 2
    #--------------------------------------------------------------------------
    
    '''
    '' Public "constants" for Eagles label Gender:
    '''
    __GENDER_INIT     = __DEGREE_INIT + 100
    GENDER_UKNOWN     = __GENDER_INIT + 1
    GENDER_MASCULINO  = __GENDER_INIT + 2
    GENDER_FEMENINO   = __GENDER_INIT + 3
    GENDER_COMUN      = __GENDER_INIT + 4
    #--------------------------------------------------------------------------
    
    '''
    '' Public "constants" for Eagles label Number:
    '''
    __NUMBER_INIT     = __GENDER_INIT + 100
    NUMBER_UKNOWN     = __NUMBER_INIT + 1
    NUMBER_SINGULAR   = __NUMBER_INIT + 2
    NUMBER_PLURAL     = __NUMBER_INIT + 3
    NUMBER_INVARIABLE = __NUMBER_INIT + 4
    #--------------------------------------------------------------------------
    
    '''
    '' Public "constants" for Eagles label Case:
    '''
    __CASE_INIT      = __NUMBER_INIT + 100
    CASE_UKNOWN      = __CASE_INIT + 1
    #--------------------------------------------------------------------------
    
    '''
    '' Public "constants" for Eagles label Forma:
    '''
    __FORMA_INIT     = __CASE_INIT + 100
    FORMA_UKNOWN     = __FORMA_INIT + 1
    FORMA_SIMPLE     = __FORMA_INIT + 2
    FORMA_CONTRAIDA  = __FORMA_INIT + 3
    #--------------------------------------------------------------------------
    


    def __init__(self, forma, lema, label):
        '''
        Constructor
        '''
        self.__forma = forma
        self.__lema = lema
        self.__label = label
    #--------------------------------------------------------------------------
      
        
    def getForm(self):
        """
        ' Returns the word being analyzed in its raw form; e.g.:
        '    alegres
        '
        'return String
        """
        return self.__forma
    #--------------------------------------------------------------------------
    
    
    
    def getLema(self):
        """
        ' Returns the root of the word being analyzed; e.g.:
        '    alegre
        '
        ' return String
        """
        return self.__lema
    #--------------------------------------------------------------------------
    
    
    
    def getEaglesLabel(self):
        """
        ' Returns the Eagles label that corresponds to the word being analyzed; e.g.:
        '    AQ0CP00
        '
        ' return String
        """
        return self.__label
    #--------------------------------------------------------------------------
    
    
    
    def getCategory(self):
        """
        ' Returns the category of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     CAT_ADJETIVO
        '
        ' If the category cannot be determined then CAT_UNKNOWN is returned.
        ' return Integer
        """
        return self.CAT_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def getType(self):
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
    
    
    
    
    def getDegree(self):
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
    
    
    
    
    def getGender(self):
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
    
    
    
    
    def getNumber(self):
        """
        ' Returns the Number of the word based on the Eagles label; e.g.:
        '    Eagles Label: AQ0CP00
        '    Category:     NUMBER_PLURAL
        '
        ' If the category cannot be determined then NUMBER_UNKNOWN is returned.
        ' return Integer
        """
        return self.NUMBER_UKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def getCase(self):
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
    
    
    
    
    def getForma(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORMA_CONTRAIDA
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
        ' return Integer
        """
        return self.FORMA_UNKNOWN
    #--------------------------------------------------------------------------
    
    '''
    '' Several methods pending to be defined. 
    '''