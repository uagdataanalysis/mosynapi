'''
Created on 13/10/2015

This class is meant to be used when parsing Abbreviation Eagles labels.

@author: axelg
'''
from base.AbstractMorphology import AbstractMorphology

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
        