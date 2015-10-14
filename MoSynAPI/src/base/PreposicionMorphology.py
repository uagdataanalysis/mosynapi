'''
Created on 05/10/2015

@author: axelg
'''
from base.AbstractMorphology import AbstractMorphology

class PreposicionMorphology(AbstractMorphology):
    '''
    classdocs
    '''

    '''
    '' Private "constants":
    '''
    __IDX_CATEGORY = 0  # Char position for preposition "Categoria". 
    __IDX_TYPE = 1      # Char position for preposition "Tipo". 
    __IDX_FORM = 2      # Char position for preposition "Forma". 
    __IDX_GENDER = 3    # Char position for preposition "Genero". 
    __IDX_NUMBER = 4    # Char position for preposition "Numbero". 
    #--------------------------------------------------------------------------
    

    def __init__(self, form, lema, label_):
        '''
        Constructor
        '''
        super(PreposicionMorphology, self).__init__( form, lema, label_)
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
        return self.CAT_ADPOSITION
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
        if self.get_eagles_label()[ self.__IDX_TYPE ] == 'P':
            return self.TYPE_PREPOSITION
        else:
            return self.TYPE_UNKNOWN
    #--------------------------------------------------------------------------
    
    
    
    
    def get_forma(self):
        """
        ' Returns the Form of the word based on the Eagles label; e.g.:
        '    Eagles Label: SPCMS
        '    Category:     FORM_CONTRACTED
        '
        ' If the category cannot be determined then FORMA_UNKNOWN is returned.
        ' return Integer
        """
        if self.get_eagles_label()[ self.__IDX_FORM ] == 'S':
            return self.FORM_SIMPLE
        elif self.get_eagles_label()[ self.__IDX_FORM ] == 'C':
            return self.FORM_CONTRACTED
        else:
            return self.FORM_UNKNOWN
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
        if self.get_eagles_label()[ self.__IDX_GENDER ] == 'M':
            return self.GENDER_MALE
        else:
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
        if self.get_eagles_label()[ self.__IDX_NUMBER ] == 'S':
            return self.NUMBER_SINGULAR
        else:
            return self.NUMBER_UKNOWN
    #--------------------------------------------------------------------------
    
    