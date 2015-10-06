'''
Created on 05/10/2015

@author: axelg
'''
from base.PreposicionMorphology import PreposicionMorphology

class MorphologyFactory(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    #--------------------------------------------------------------------------
        
        
    @staticmethod
    def createMorphology(self, forma, lema, label_ ):
        """
        Use this method to create the specific Morphology objects; e.g.:
            MorphologyFactory.createMorphology( "SPCMS" )
            
        This method receives as parameter the Eagles label and returns the 
        proper Morphology object based on that.
        """
        if label_[0] == 'S':
            return PreposicionMorphology( forma, lema, label_ )
        else:
            raise NotImplementedError()
    #--------------------------------------------------------------------------