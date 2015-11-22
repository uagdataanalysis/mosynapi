# -*- coding: iso-8859-15 -*-
'''
Created on 21/11/2015

@author: axelg
'''
from util.eagles import AbstractMorphology
from mosyn import MorphologicalDictionary, AnalysisManager

def test_example():
    dictionary = MorphologicalDictionary("../mosyn/dict/spanish_dict.csv")
    dictionary.load()
    manager = AnalysisManager( dictionary, None, None )
    
    pdata = manager.parse_string_to_eagles( u"La PUEDO escribir los versos más tristes esta noche." )
    
    print("Processing: PUEDO escribir los versos más tristes esta noche.")
    print(".............................................................")
    for labels in pdata:
        print "\"", labels[0].get_form(), "\" ( lema:", labels[0].get_lema(), ")"
        for label in labels:
            print "\t", label.get_eagles_label(), "->",
            describe( label )
            print ""
        print("----------------------------------------------------")
        print("")



def describe( eagles ):
    catname = get_category_name(eagles)
    
    aux = eagles.get_number()
    if aux == AbstractMorphology.NUMBER_SINGULAR:
        print "singular",
    elif aux == AbstractMorphology.NUMBER_PLURAL:
        print "plural",
    elif aux == AbstractMorphology.NUMBER_INVARIABLE:
        print "invariable",
    elif aux == AbstractMorphology.NUMBER_UNKNOWN:
        print "undefined number",
    else:
        print str(aux),
        
    aux = eagles.get_type()
    
    if aux == AbstractMorphology.TYPE_GENERAL:
        print ", it is of general type",
    elif aux == AbstractMorphology.TYPE_CALIFICATIVE:
        print ", it is of calificative type",
    
    aux = eagles.get_gender()
    
    if aux == AbstractMorphology.GENDER_MALE:
        print "male", catname,
    elif aux == AbstractMorphology.GENDER_FEMALE:
        print "female", catname,
    else:
        print catname, "without gender",
        
    

def get_category_name( eagles ):
    aux = eagles.get_category()
    
    if aux == AbstractMorphology.CAT_ARTICLE:
        return "article"
    elif aux == AbstractMorphology.CAT_DETERMINANT:
        return "determinant"
    elif aux == AbstractMorphology.CAT_ABBREVIATION:
        return "abbreviation"
    elif aux == AbstractMorphology.CAT_ADJECTIVE:
        return "adjective"
    elif aux == AbstractMorphology.CAT_ADVERB:
        return "adverb"
    elif aux == AbstractMorphology.CAT_CONJUNCTION:
        return "conjunction"
    elif aux == AbstractMorphology.CAT_INTERJECTION:
        return "interjection"
    elif aux == AbstractMorphology.CAT_NAME:
        return "name"
    elif aux == AbstractMorphology.CAT_NUMERAL:
        return "numeral"
    elif aux == AbstractMorphology.CAT_ADPOSITION: # Preposition
        return "adposition/preposition"
    elif aux == AbstractMorphology.CAT_PRONOUN:
        return "pronoun"
    elif aux == AbstractMorphology.CAT_PUNCTUATION:
        return "punctuation"
    elif aux == AbstractMorphology.CAT_VERB:
        return "verb"
    else:
        return "unknown"



if __name__ == '__main__':
    test_example()