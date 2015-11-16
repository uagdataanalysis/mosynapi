#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Created on 01/11/2015
# Modified on 01/11/2015
# Modified by asaelt
#
# Source:
# https://github.com/uagdataanalysis/mosynapi
#
# @author: asaelt


def format_morphological_data(data, template=u' |{0[0]}|{0[1]}|'):
    """
    Converts a set of morphological data into string.
    :param data: The set of morphological data.
    :param template: The output template for |<root>|<eagles-code>| tuple.
    :return: A string representation of the morphological data.
    """
    formatted = u''
    for option in data[1]:
        formatted += template.format(option)

    return data[0] + formatted + u'\n'
