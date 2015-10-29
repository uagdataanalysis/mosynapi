#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Created on 07/10/2015
# Modified on 20/10/2015
# Modified by asaelt
#
# This class is based on the definition of the Eagles Labeling standard:
# http://www.cs.upc.edu/~nlp/tools/parole-sp.html
#
# @author: asaelt


class EventHook(object):

    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self

    def fire(self, *args, **keywargs):
        for handler in self.__handlers:
            handler(*args, **keywargs)

    def clear_object_handlers(self, in_object):
        for the_handler in self.__handlers:
            if the_handler.im_self == in_object:
                self -= the_handler
