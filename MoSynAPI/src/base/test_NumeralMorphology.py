'''
Created on 12/10/2015

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
        numeral = NumeralMorphology("forma", "lema", "MCCP00" )
        result = numeral.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_NUMERALS, 
                         result, 
                         "CAT_NUMERALS is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testCategoryInvalid(self):
        """ Test an invalid Eagles label"""
        # CAT_NUMERALS is expected here since NumeralMorphology class is
        # meant to model numerals only. Under that assumption there is no
        # need to add logic to handle non-numeral labels. If label is not 
        # a numeral please do not use NumeralMorphology class.
        numeral = NumeralMorphology("forma", "lema", "xCCP00" )
        result = numeral.get_category()
        
        self.assertEqual( 
                         AbstractMorphology.CAT_NUMERALS, 
                         result, 
                         "CAT_NUMERALS is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testTypeCardinal(self):
        """ Test the Cardinal Numeral type Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MCCP00" )
        result = numeral.get_type()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_CARDINAL, 
                         result, 
                         "TYPE_CARDINAL is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testTypeOrdinal(self):
        """ Test a valid Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MOCP00" )
        result = numeral.get_type()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_ORDINAL, 
                         result, 
                         "TYPE_ORDINAL is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testTypeInvalid(self):
        """ Test an invalid Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MxCP00" )
        result = numeral.get_type()
        
        self.assertEqual( 
                         AbstractMorphology.TYPE_UNKNOWN, 
                         result, 
                         "TYPE_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testFormaInvalid(self):
        """ Test an invalid Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MCMP00" )
        result = numeral.get_label_form()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_UNKNOWN, 
                         result, 
                         "FORM_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testGenderMale(self):
        """ Test Male Gender Eagles label"""
        numeral = NumeralMorphology("cuatrocientos", "cuatrocientos", "MCMP00" )
        result = numeral.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_MALE, 
                         result, 
                         "GENDER_MALE is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testGenderFemale(self):
        """ Test Female Gender Eagles label"""
        numeral = NumeralMorphology("cuatrocientas", "cuatrocientos", "MCFP00" )
        result = numeral.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_FEMALE, 
                         result, 
                         "GENDER_FEMALE is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testGenderCommon(self):
        """ Test Common Gender Eagles label"""
        numeral = NumeralMorphology("cuatro", "cuatro", "MCCP00" )
        result = numeral.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_COMMON, 
                         result, 
                         "GENDER_COMMON is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testGenderInvalid(self):
        """ Test Invalid Gender Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MCxP00" )
        result = numeral.get_gender()
        
        self.assertEqual( 
                         AbstractMorphology.GENDER_UKNOWN, 
                         result, 
                         "GENDER_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testNumberSingular(self):
        """ Test a valid Eagles label"""
        numeral = NumeralMorphology("uno", "uno", "MCFS00" )
        result = numeral.get_number()
        
        self.assertEqual( 
                         AbstractMorphology.NUMBER_SINGULAR, 
                         result, 
                         "NUMBER_SINGULAR is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testNumberPlural(self):
        """ Test a valid Eagles label"""
        numeral = NumeralMorphology("unos", "uno", "MCMP00" )
        result = numeral.get_number()
        
        self.assertEqual( 
                         AbstractMorphology.NUMBER_PLURAL, 
                         result, 
                         "NUMBER_PLURAL is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testNumberInvalid(self):
        """ Test an invalid Eagles Number for numeral"""
        numeral = NumeralMorphology("forma", "lema", "MCMx00" )
        result = numeral.get_number()
        
        self.assertEqual( 
                         AbstractMorphology.NUMBER_UNKNOWN, 
                         result, 
                         "NUMBER_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testCase(self):
        """ Test the Case Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MCMP00" )
        result = numeral.get_case()
        
        self.assertEqual( 
                         AbstractMorphology.CASE_UKNOWN, 
                         result, 
                         "CASE_UKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testForm(self):
        """ Test the Form in the Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MCMP00" )
        result = numeral.get_label_form()
        
        self.assertEqual( 
                         AbstractMorphology.FORM_UNKNOWN, 
                         result, 
                         "FORM_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------


    def testRolPronominal(self):
        """ Test the Rol specified in the Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MCMP0P" )
        result = numeral.get_rol()
        
        self.assertEqual( 
                         AbstractMorphology.ROL_PRONOMINAL, 
                         result, 
                         "ROL_PRONOMINAL is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testRolDeterminant(self):
        """ Test the Rol specified in the Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MCMP0D" )
        result = numeral.get_rol()
        
        self.assertEqual( 
                         AbstractMorphology.ROL_DETERMINANT, 
                         result, 
                         "ROL_DETERMINANT is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testRolAdjective(self):
        """ Test the Rol specified in the Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MCMP0A" )
        result = numeral.get_rol()
        
        self.assertEqual( 
                         AbstractMorphology.ROL_ADJECTIVE, 
                         result, 
                         "ROL_ADJECTIVE is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------


    def testRolInvalid(self):
        """ Test the Rol specified in the Eagles label"""
        numeral = NumeralMorphology("forma", "lema", "MCMP0x" )
        result = numeral.get_rol()
        
        self.assertEqual( 
                         AbstractMorphology.ROL_UNKNOWN, 
                         result, 
                         "ROL_UNKNOWN is expected but obtained: " + 
                             str(result) )
    #--------------------------------------------------------------------------
    #--------------------------------------------------------------------------
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCategory']
    unittest.main()