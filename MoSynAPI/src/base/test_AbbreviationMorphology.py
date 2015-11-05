'''
Created on 13/10/2015

@author: axelg
'''
import unittest
from base.eagles import AbbreviationMorphology
from base.eagles import AbstractMorphology


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass
    

    def testCategory(self):
        """ Test a valid Eagles label"""
        preposicion = AbbreviationMorphology("forma", "lema", "Y0000" )
        result = preposicion.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_ABBREVIATIONS,
                         result, 
                         "CAT_ABBREVIATIONS is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testCategoryInvalid(self):
        """ Test an invalid Eagles label"""
        # CAT_ADPOSITION is expected here since PrepositionMorhology class is
        # meant to model prepositions only. Under that assumption there is no
        # need to add logic to handle non-preposition labels. If label is not 
        # an abbreviation please do not use this class.
        preposicion = AbbreviationMorphology("forma", "lema", "x0000" )
        result = preposicion.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_ABBREVIATIONS, 
                         result, 
                         "CAT_ABBREVIATIONS is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testTypeInvalid(self):
        """ Test an invalid Eagles label"""
        abbreviation = AbbreviationMorphology("forma", "lema", "Y0000" )
        result = abbreviation.get_type()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_UNKNOWN,
                         result, 
                         "TYPE_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    
    def testFormaInvalid(self):
        """ Test an invalid Eagles label"""
        abbreviation = AbbreviationMorphology("forma", "lema", "Y0000" )
        result = abbreviation.get_label_form()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_UNKNOWN,
                         result, 
                         "FORMA_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testGenderInvalid(self):
        """ Test an invalid Eagles Gender for abbreviation"""
        abbreviation = AbbreviationMorphology("forma", "lema", "Y0000" )
        result = abbreviation.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_UNKNOWN, 
                         result, 
                         "GENDER_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testNumberInvalid(self):
        """ Test an invalid Eagles Number for abbreviation"""
        abbreviation = AbbreviationMorphology("forma", "lema", "Y0000" )
        result = abbreviation.get_number()
        
        self.assertEqual( 
                         AbstractMorphology.NUMBER_UNKNOWN, 
                         result, 
                         "NUMBER_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCategory']
    unittest.main()