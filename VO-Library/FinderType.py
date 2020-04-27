#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import Enum

class FinderType(Enum):
    RETR_EXTERNAL = 1
    RETR_LIST = 2
    RETR_CCOMP = 3
    RETR_TREE = 4
    RETR_FLOODFILL = 5
