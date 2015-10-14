'''
Created on 06/10/2015

@author: axelg
'''
import unittest
from base.AbstractMorphology import AbstractMorphology
from base.PreposicionMorphology import PreposicionMorphology


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testCategory(self):
        """ Test a valid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_ADPOSITION, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testCategoryInvalid(self):
        """ Test an invalid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "xPCMS" )
        result = preposicion.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_UNKNOWN, 
                         result, 
                         "CAT_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testType(self):
        """ Test a valid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_type()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_PREPOSITION, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testTypeInvalid(self):
        """ Test an invalid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SxCMS" )
        result = preposicion.get_type()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_UKNOWN, 
                         result, 
                         "CAT_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testFormaContraida(self):
        """ Test a valid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_forma()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_CONTRACTED, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testFormaSimple(self):
        """ Test a valid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPSMS" )
        result = preposicion.get_forma()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_SIMPLE, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testFormaInvalid(self):
        """ Test an invalid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPxMS" )
        result = preposicion.get_forma()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_UKNOWN, 
                         result, 
                         "CAT_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testGender(self):
        """ Test a valid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_MALE, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testGenderInvalid(self):
        """ Test an invalid Eagles Gender for Preposicion"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCFS" )
        result = preposicion.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_UKNOWN, 
                         result, 
                         "CAT_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testNumber(self):
        """ Test a valid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.get_number()
        
        self.assertEqual( 
                         AbstractMorphology.NUMBER_SINGULAR, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testNumberInvalid(self):
        """ Test an invalid Eagles Number for Preposicion"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCFP" )
        result = preposicion.get_number()
        
        self.assertEqual( 
                         AbstractMorphology.NUMBER_UKNOWN, 
                         result, 
                         "CAT_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCategory']
    unittest.main()