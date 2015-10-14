'''
Created on 13/10/2015

@author: axelg
'''
from base.AbstractMorphology import AbstractMorphology

class InterjectionMorphology(AbstractMorphology):
    '''
    classdocs
    '''


    def __init__(self, form, lema, label_):
        '''
        Constructor
        '''
        super(InterjectionMorphology, self).__init__( form, lema, label_)
    #--------------------------------------------------------------------------
    
    
    
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
    #--------------------------------------------------------------------------