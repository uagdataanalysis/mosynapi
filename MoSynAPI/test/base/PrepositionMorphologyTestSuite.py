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
        result = preposicion.getCategory()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_ADPOSICION, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testCategoryInvalid(self):
        """ Test an invalid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "xPCMS" )
        result = preposicion.getCategory()
        
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
        result = preposicion.getType()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_PREPOSICION, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testTypeInvalid(self):
        """ Test an invalid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SxCMS" )
        result = preposicion.getType()
        
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
        result = preposicion.getForma()
        
        self.assertEqual( 
                         AbstractMorphology.FORMA_CONTRAIDA, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testFormaSimple(self):
        """ Test a valid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPSMS" )
        result = preposicion.getForma()
        
        self.assertEqual( 
                         AbstractMorphology.FORMA_SIMPLE, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testFormaInvalid(self):
        """ Test an invalid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPxMS" )
        result = preposicion.getForma()
        
        self.assertEqual( 
                         AbstractMorphology.FORMA_UKNOWN, 
                         result, 
                         "CAT_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testGender(self):
        """ Test a valid Eagles label"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCMS" )
        result = preposicion.getGender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_MASCULINO, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testGenderInvalid(self):
        """ Test an invalid Eagles Gender for Preposicion"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCFS" )
        result = preposicion.getGender()
        
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
        result = preposicion.getNumber()
        
        self.assertEqual( 
                         AbstractMorphology.NUMBER_SINGULAR, 
                         result, 
                         "CAT_ADPOSICION is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testNumberInvalid(self):
        """ Test an invalid Eagles Number for Preposicion"""
        preposicion = PreposicionMorphology("forma", "lema", "SPCFP" )
        result = preposicion.getNumber()
        
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