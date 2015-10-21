'''
Created on 20/10/2015

@author: axelg
'''
from base.AbstractMorphology import AbstractMorphology

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