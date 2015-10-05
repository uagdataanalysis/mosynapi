'''
Created on 04/10/2015

This class is based on the definition of the Eagles Labeling standard:
http://www.cs.upc.edu/~nlp/tools/parole-sp.html

@author: axelg
'''

class AbstractMorphology(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
    '''
    ' Returns the word being analyzed in its raw form; e.g.:
    '    alegres
    '
    'return String
    '''
    def getForm(self):
        raise NotImplementedError()
    
    
    
    '''
    ' Returns the root of the word being analyzed; e.g.:
    '    alegre
    '
    ' return String
    '''
    def getLema(self):
        raise NotImplementedError()
    
    
    
    '''
    ' Returns the Eagles label that corresponds to the word being analyzed; e.g.:
    '    AQ0CP00
    '
    ' return String
    '''
    def getEaglesLabel(self):
        raise NotImplementedError()