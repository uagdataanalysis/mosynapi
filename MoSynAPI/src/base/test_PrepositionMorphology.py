'''
Created on 06/10/2015

@author: axelg
'''
import unittest
from base.eagles import *


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCategory(self):
        """ Test a valid Eagles label"""
        preposicion = PrepositionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_ADPOSITION, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testCategoryInvalid(self):
        """ Test an invalid Eagles label"""
        # CAT_ADPOSITION is expected here since PrepositionMorhology class is
        # meant to model prepositions only. Under that assumption there is no
        # need to add logic to handle non-preposition labels. If label is not 
        # a preposition please do not use this class.
        preposicion = PrepositionMorphology("forma", "lema", "xPCMS" )
        result = preposicion.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_ADPOSITION, 
                         result, 
                         "CAT_ADPOSITION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testType(self):
        """ Test a valid Eagles label"""
        preposicion = PrepositionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_type()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_PREPOSITION, 
                         result, 
                         "TYPE_PREPOSITION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testTypeInvalid(self):
        """ Test an invalid Eagles label"""
        preposicion = PrepositionMorphology("forma", "lema", "SxCMS" )
        result = preposicion.get_type()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_UNKNOWN, 
                         result, 
                         "TYPE_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testFormaContraida(self):
        """ Test a valid Eagles label"""
        preposicion = PrepositionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_label_form()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_CONTRACTED, 
                         result, 
                         "FORM_CONTRACTED is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testFormaSimple(self):
        """ Test a valid Eagles label"""
        preposicion = PrepositionMorphology("forma", "lema", "SPSMS" )
        result = preposicion.get_label_form()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_SIMPLE, 
                         result, 
                         "FORM_SIMPLE is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testFormaInvalid(self):
        """ Test an invalid Eagles label"""
        preposicion = PrepositionMorphology("forma", "lema", "SPxMS" )
        result = preposicion.get_label_form()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_UNKNOWN, 
                         result, 
                         "FORM_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testGender(self):
        """ Test a valid Eagles label"""
        preposicion = PrepositionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_MALE, 
                         result, 
                         "GENDER_MALE is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testGenderInvalid(self):
        """ Test an invalid Eagles Gender for Preposicion"""
        preposicion = PrepositionMorphology("forma", "lema", "SPCFS" )
        result = preposicion.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_UKNOWN, 
                         result, 
                         "GENDER_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testNumber(self):
        """ Test a valid Eagles label"""
        preposicion = PrepositionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_number()
        
        self.assertEqual( 
                         AbstractMorphology.NUMBER_SINGULAR, 
                         result, 
                         "NUMBER_SINGULAR is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testNumberInvalid(self):
        """ Test an invalid Eagles Number for Preposicion"""
        preposicion = PrepositionMorphology("forma", "lema", "SPCFP" )
        result = preposicion.get_number()
        
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