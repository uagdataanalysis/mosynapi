# -*- coding: iso-8859-15 -*-
'''
Created on 21/11/2015

@author:  Axel Garcia

Version for Python versions 3.x (e.g. 3.4, 3.5)

This is an example of how the Mosyn API can be used to parse a plain text file. Mosyn 
takes the Spanish corpus from the dictionary specified by the "MorphologicalDictionary" 
class which takes a .csv file as argument; it is possible to use a different dictionary
for the processing.

After specifying and loading the dictionary, this example uses "parse_file_to_eagles" 
function to do the actual morphosyntactic analysis. That function will parse the entire
file at once. Depending on the file size it may be recommended to split the text file
into several short sections as required.

After loading the dictionary by using the load() function of "MorphologicalDictionary"
class the parse_file_to_eagles function can be used on the split files without having 
to specify a new dictionary or loading it again.

Thanks to the Universidad Autonoma de Guadalajara for providing the dictionary 
used in this example.'''
import mosyn
from mosyn.util import AbstractMorphology


def analyze():
    """Use Mosyn API to perform the morphosyntactic analysis on a text written in Spanish 
    which is contained in a plain text file.
    
    This method will print(to the screen an example of the morphosyntactic analysis that
    can be done."""
    dictionary = mosyn.MorphologicalDictionary("../dict/spanish_dict.csv")
    dictionary.load()
    manager = mosyn.AnalysisManager(dictionary)
    
    processed_data = manager.parse_file_to_eagles("Poema20.txt")
    
    print("Processing: Poema20.txt.")
    print(".............................................................")
    #
    # Below, each one of the eagles labels are processed. There is an element
    # generated for each word...
    for labels in processed_data:
        print("\"", labels[0].get_form(), "\" ( lema:", labels[0].get_lema(), ")")
        # ... and for each word more than one eagles label may be generated 
        # depending on how many usages that given word may have.
        for label in labels:
            print("\t", label.get_eagles_label(), "->", end=" ")
            describe(label)
            print("")
        print("----------------------------------------------------")
        print("")


def describe(eagles):
    """Using Mosyn API the script can decide based on built in functions.
    
    This function uses some of the build-in functions to describe the Eagles label
    passed as parameter."""
    catname = get_category_name(eagles)
    
    aux = eagles.get_number()
    if aux == AbstractMorphology.NUMBER_SINGULAR:
        print("singular", end=" ")
    elif aux == AbstractMorphology.NUMBER_PLURAL:
        print("plural", end=" ")
    elif aux == AbstractMorphology.NUMBER_INVARIABLE:
        print("invariable", end=" ")
    elif aux == AbstractMorphology.NUMBER_UNKNOWN:
        print("undefined number", end=" ")
    else:
        print(str(aux), end=" ")
        
    aux = eagles.get_type()
    
    if aux == AbstractMorphology.TYPE_GENERAL:
        print(", it is of general type", end=" ")
    elif aux == AbstractMorphology.TYPE_CALIFICATIVE:
        print(", it is of calificative type", end=" ")
    
    aux = eagles.get_gender()
    
    if aux == AbstractMorphology.GENDER_MALE:
        print("male", catname, end=" ")
    elif aux == AbstractMorphology.GENDER_FEMALE:
        print("female", catname, end=" ")
    else:
        print(catname, "without gender", end=" ")


def get_category_name( eagles ):
    """Mosyn API provides standard word categories based on eagles specification. 
    
    See more details about the Eagles labeling and their categories in the 
    following link: http://www.cs.upc.edu/~nlp/tools/parole-sp.html"""
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
    analyze()
