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
    CAT_UNKNOWN       = 0
    CAT_ADJETIVO      = 1
    CAT_ADVERBIO      = 2 
    CAT_ARTICULOS     = 3
    CAT_DETERMINANTES = 4
    CAT_NOMBRES       = 5
    CAT_VERBOS        = 6
    CAT_PRONOMBRES    = 7
    CAT_CONJUNCIONES  = 8
    CAT_NUMERALES     = 9
    CAT_INTERJECCIONES= 10
    CAT_ABREVIATURAS  = 11
    CAT_PREPOSICIONES = 12
    CAT_PUNTUACION    = 13


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
    
    
    
    '''
    ' Returns the category of the word based on the Eagles label; e.g.:
    '    Eagles Label: AQ0CP00
    '    Category:     CAT_ADJETIVO
    '
    ' If the category cannot be determined then CAT_UNKNOWN is returned.
    ' return Integer
    '''
    def getCategory(self):
        raise NotImplementedError()
    
    '''
    '' Several methods pending to be defined. 
    '''