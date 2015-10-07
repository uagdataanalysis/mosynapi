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
    __IDX_CATEGORIA  = 0    # Char position for preposition "Categoria". 
    __IDX_TIPO       = 1    # Char position for preposition "Tipo". 
    __IDX_FORMA      = 2    # Char position for preposition "Forma". 
    __IDX_GENDER     = 3    # Char position for preposition "Genero". 
    __IDX_NUMBER     = 4    # Char position for preposition "Numbero". 
    #--------------------------------------------------------------------------
    

    def __init__(self, forma, lema, label_):
        '''
        Constructor
        '''
        super(PreposicionMorphology, self).__init__( forma, lema, label_)
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
        if self.getEaglesLabel()[ self.__IDX_CATEGORIA ] == 'S':
            return self.CAT_ADPOSICION
        else:
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
        if self.getEaglesLabel()[ self.__IDX_TIPO ] == 'P':
            return self.TYPE_PREPOSICION
        else:
            return self.TYPE_UKNOWN
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
        if self.getEaglesLabel()[ self.__IDX_FORMA ] == 'S':
            return self.FORMA_SIMPLE
        elif self.getEaglesLabel()[ self.__IDX_FORMA ] == 'C':
            return self.FORMA_CONTRAIDA
        else:
            return self.FORMA_UKNOWN
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
        if self.getEaglesLabel()[ self.__IDX_GENDER ] == 'M':
            return self.GENDER_MASCULINO
        else:
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
        if self.getEaglesLabel()[ self.__IDX_NUMBER ] == 'S':
            return self.NUMBER_SINGULAR
        else:
            return self.NUMBER_UKNOWN
    #--------------------------------------------------------------------------
    
    