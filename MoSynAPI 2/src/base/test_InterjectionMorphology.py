'''
Created on 13/10/2015

@author: axelg
'''
import unittest
from base.InterjectionMorphology import InterjectionMorphology
from base.AbstractMorphology import AbstractMorphology


class Test(unittest.TestCase):
    
    def testCategory(self):
        """ Test a valid Eagles label"""
        interjection = InterjectionMorphology("form", "lema", "I0000" )
        result = interjection.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_INTERJECTION, 
                         result, 
                         "CAT_INTERJECTION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testCategoryInvalid(self):
        """ Test an invalid Eagles label"""
        # CAT_ADPOSITION is expected here since PrepositionMorhology class is
        # meant to model prepositions only. Under that assumption there is no
        # need to add logic to handle non-preposition labels. If label is not 
        # an interjection please do not use this class.
        interjection = InterjectionMorphology("form", "lema", "x0000" )
        result = interjection.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_INTERJECTION, 
                         result, 
                         "CAT_INTERJECTION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testTypeInvalid(self):
        """ Test an invalid Eagles label"""
        interjection = InterjectionMorphology("form", "lema", "I0000" )
        result = interjection.get_type()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_UNKNOWN, 
                         result, 
                         "TYPE_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    
    def testformInvalid(self):
        """ Test an invalid Eagles label"""
        interjection = InterjectionMorphology("form", "lema", "x0000" )
        result = interjection.get_label_form()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_UNKNOWN, 
                         result, 
                         "FORM_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testGenderInvalid(self):
        """ Test an invalid Eagles Gender for interjection"""
        interjection = InterjectionMorphology("form", "lema", "I0000" )
        result = interjection.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_UKNOWN, 
                         result, 
                         "GENDER_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testNumberInvalid(self):
        """ Test an invalid Eagles Number for interjection"""
        interjection = InterjectionMorphology("form", "lema", "I0000" )
        result = interjection.get_number()
        
        self.assertEqual( 
                         AbstractMorphology.NUMBER_UKNOWN, 
                         result, 
                         "NUMBER_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCategory']
    unittest.main()