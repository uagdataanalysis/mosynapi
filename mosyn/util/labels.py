#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Created on 28/07/2018
# Modified on 28/07/2018
# Modified by asaelt
#
# This class is based on the definition of the Eagles Labeling standard:
# http://www.cs.upc.edu/~nlp/tools/parole-sp.html
#
# Source:
# https://github.com/uagdataanalysis/mosynapi
#
# @author: torrar


from .eagles import AbstractMorphology

def get_category( eagles ):
    """
    Get a text representation of a category in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles category. 
    """
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
# --------------------------------------------------------------------------


def get_type(eagles):
    """
    Get a text representation of a type in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles type. 
    """
    aux = eagles.get_type()
    
    if aux == AbstractMorphology.TYPE_CALIFICATIVE:
        return "calificative"
    elif aux == AbstractMorphology.TYPE_PREPOSITION:
        return "preposition"
    elif aux == AbstractMorphology.TYPE_GENERAL:
        return "general"
    elif aux == AbstractMorphology.TYPE_DEFINED:
        return "defined"
    elif aux == AbstractMorphology.TYPE_DEMOSTRATIVE:
        return "demostrative"
    elif aux == AbstractMorphology.TYPE_POSESIVE:
        return "posesive"
    elif aux == AbstractMorphology.TYPE_INTERROGATIVE:
        return "interrogative"
    elif aux == AbstractMorphology.TYPE_EXCLAMATIVE:
        return "exclamative"
    elif aux == AbstractMorphology.TYPE_INDEFINIDO:
        return "indefinido"
    elif aux == AbstractMorphology.TYPE_COMMON:
        return "common"
    elif aux == AbstractMorphology.TYPE_PROPER:
        return "proper"
    elif aux == AbstractMorphology.TYPE_PRINCIPAL:
        return "principal"
    elif aux == AbstractMorphology.TYPE_AUXILIAR:
        return "auxiliar"
    elif aux == AbstractMorphology.TYPE_PERSONAL:
        return "personal"
    elif aux == AbstractMorphology.TYPE_RELATIVE:
        return "relative"
    elif aux == AbstractMorphology.TYPE_COORDINATED:
        return "coordinated"
    elif aux == AbstractMorphology.TYPE_SUBORDINATED:
        return "subordinated"
    elif aux == AbstractMorphology.TYPE_CARDINAL:
        return "cardinal"
    elif aux == AbstractMorphology.TYPE_ORDINAL:
        return "ordinal"
    else:
        return "unknown"
# --------------------------------------------------------------------------

def get_degree(eagles):
    """
    Get a text representation of a degree in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles degree. 
    """
    aux = eagles.get_degree()
    
    if aux == AbstractMorphology.DEGREE_APRECIATIVO:
        return "apreciativo"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_gender(eagles):
    """
    Get a text representation of a gender in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles gender. 
    """
    aux = eagles.get_gender()
    
    if aux == AbstractMorphology.GENDER_MALE:
        return "male"
    elif aux == AbstractMorphology.GENDER_FEMALE:
        return "female"
    elif aux == AbstractMorphology.GENDER_COMMON:
        return "common"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_number(eagles):
    """
    Get a text representation of a number in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles number. 
    """
    aux = eagles.get_number()

    if aux == AbstractMorphology.NUMBER_SINGULAR:
        return "singular"
    elif aux == AbstractMorphology.NUMBER_PLURAL:
        return "plural"
    elif aux == AbstractMorphology.NUMBER_INVARIABLE:
        return "invariable"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_case(eagles):
    """
    Get a text representation of a case in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles case. 
    """
    aux = eagles.get_case()
    
    if aux == AbstractMorphology.CASE_NO_VALUE:
        return "no_value"
    elif aux == AbstractMorphology.CASE_NOMINATIVE:
        return "nominative"
    elif aux == AbstractMorphology.CASE_ACUSATIVE:
        return "acusative"
    elif aux == AbstractMorphology.CASE_DATIVO:
        return "dativo"
    elif aux == AbstractMorphology.CASE_OBLICUO:
        return "oblicuo"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_form(eagles):
    """
    Get a text representation of a form in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles form. 
    """
    aux = eagles.get_label_form()
    
    if aux == AbstractMorphology.FORM_SIMPLE:
        return "simple"
    elif aux == AbstractMorphology.FORM_CONTRACTED:
        return "contracted"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_function(eagles):
    """
    Get a text representation of a function in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles function. 
    """
    cat = eagles.get_category
    if  (
            cat != AbstractMorphology.CAT_ADJECTIVE
        ):
        return "unknown"

    aux = eagles.get_function()
    
    if aux == AbstractMorphology.FUNCTION_PARTICIPLE:
        return "participle"
    elif aux == AbstractMorphology.FUNCTION_PRONOMINAL:
        return "pronominal"
    elif aux == AbstractMorphology.FUNCTION_DETERMINANTE:
        return "determinante"
    elif aux == AbstractMorphology.FUNCTION_ADJETIVO:
        return "adjetivo"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_person(eagles):
    """
    Get a text representation of a person in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles person. 
    """
    cat = eagles.get_category
    if  (
            cat not in (
                AbstractMorphology.CAT_DETERMINANT,
                AbstractMorphology.CAT_VERB, 
                AbstractMorphology.CAT_PRONOUN
            )
        ):
        return "unknown"

    aux = eagles.get_peson()
    
    if aux == AbstractMorphology.PERSON_FIRST:
        return "first"
    elif aux == AbstractMorphology.PERSON_SECOND:
        return "second"
    elif aux == AbstractMorphology.PERSON_THIRD:
        return "third"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_holder(eagles):
    """
    Get a text representation of a holder in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles holder. 
    """
    cat = eagles.get_category
    if  (
            cat not in (
                AbstractMorphology.CAT_DETERMINANT,
                AbstractMorphology.CAT_PRONOUN
            )
        ):
        return "unknown"

    aux = eagles.get_holder()
    
    if aux == AbstractMorphology.HOLDER_FIRST_PERSON_SINGLE:
        return "first_person_single"
    elif aux == AbstractMorphology.HOLDER_SECOND_PERSON_SINGLE:
        return "second_person_single"
    elif aux == AbstractMorphology.HOLDER_THIRD_PERSON:
        return "third_person"
    elif aux == AbstractMorphology.HOLDER_FIRST_PERSON_PLURAL:
        return "first_person_plural"
    elif aux == AbstractMorphology.HOLDER_SECOND_PERSON_PLURAL:
        return "second_person_plural"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_semantic_gender(eagles):
    """
    Get a text representation of a semantic gender in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles semantic gender. 
    """
    cat = eagles.get_category
    if  ( cat != AbstractMorphology.CAT_NAME ):
        return "unknown"

    aux = eagles.get_semantic_gender()
    
    if aux == AbstractMorphology.SEMANTIC_GENDER_NO_VALUE:
        return "gender_unknown"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_mode(eagles):
    """
    Get a text representation of a mode in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles mode. 
    """
    cat = eagles.get_category
    if  ( cat != AbstractMorphology.CAT_VERB ):
        return "unknown"

    aux = eagles.get_mode()
    
    if aux == AbstractMorphology.MODE_INDICATIVO:
        return "indicativo"
    elif aux == AbstractMorphology.MODE_SUBJUNTIVO:
        return "subjuntivo"
    elif aux == AbstractMorphology.MODE_IMPERATIVO:
        return "imperativo"
    elif aux == AbstractMorphology.MODE_CONDICIONAL:
        return "condicional"
    elif aux == AbstractMorphology.MODE_INFINITIVO:
        return "infinitivo"
    elif aux == AbstractMorphology.MODE_GERUNDIO:
        return "gerundio"
    elif aux == AbstractMorphology.MODE_PARTICIPIO:
        return "participio"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_time(eagles):
    """
    Get a text representation of a time in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles time. 
    """
    cat = eagles.get_category
    if  ( cat != AbstractMorphology.CAT_VERB ):
        return "undefined"

    aux = eagles.get_time()
    
    if aux == AbstractMorphology.TIME_PRESENT:
        return "present"
    elif aux == AbstractMorphology.TIME_IMPERFECT:
        return "imperfect"
    elif aux == AbstractMorphology.TIME_FUTURE:
        return "future"
    elif aux == AbstractMorphology.TIME_PAST:
        return "past"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_politeness(eagles):
    """
    Get a text representation of a politeness in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles politeness. 
    """
    cat = eagles.get_category
    if  ( cat != AbstractMorphology.CAT_PRONOUN ):
        return "undefined"

    aux = eagles.get_politeness()
    
    if aux == AbstractMorphology.POLITENESS_POLITE:
        return "polite"
    else:
        return "unknown"
# --------------------------------------------------------------------------


def get_role(eagles):
    """
    Get a text representation of a role in eagles label.
    :param eagles: An eagles label.
    :return: A string representation of the eagles role. 
    """
    aux = eagles.get_rol()
    
    if aux == AbstractMorphology.ROL_PRONOMINAL:
        return "pronominal"
    elif aux == AbstractMorphology.ROL_DETERMINANT:
        return "determinant"
    elif aux == AbstractMorphology.ROL_ADJECTIVE:
        return "adjective"
    else:
        return "unknown"
# --------------------------------------------------------------------------
