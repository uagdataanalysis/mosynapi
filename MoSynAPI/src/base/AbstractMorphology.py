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
    TYPE_CALIFICATIVO = __TYPE_INIT + 2 # Not sure if Calificativo<->Qualifying
    TYPE_PREPOSITION  = __TYPE_INIT + 3
    #--------------------------------------------------------------------------
    
    '''
    '' Public "constants" for Eagles label Degree:
    '''
    __DEGREE_INIT = __TYPE_INIT + 100
    DEGREE_UKNOWN = __DEGREE_INIT + 1
    DEGREE_APPRECIATIVE = __DEGREE_INIT + 2
    #--------------------------------------------------------------------------
    
    '''
    '' Public "constants" for Eagles label Gender:
    '''
    __GENDER_INIT = __DEGREE_INIT + 100
    GENDER_UKNOWN = __GENDER_INIT + 1
    GENDER_MALE = __GENDER_INIT + 2
    GENDER_FEMALE = __GENDER_INIT + 3
    GENDER_COMMON = __GENDER_INIT + 4
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
    __FORMA_INIT = __CASE_INIT + 100
    FORM_UNKNOWN = __FORMA_INIT + 1
    FORM_SIMPLE = __FORMA_INIT + 2
    FORM_CONTRACTED = __FORMA_INIT + 3
    #--------------------------------------------------------------------------
    


    def __init__(self, form, lema, label):
        '''
        Constructor
        '''
        self.__form = form
        self.__lema = lema
        self.__label = label
    #--------------------------------------------------------------------------
      
        
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
        return self.NUMBER_UKNOWN
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
    
    '''
    '' Several methods pending to be defined. 
    '''