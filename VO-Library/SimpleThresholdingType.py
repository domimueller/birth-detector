#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import Enum

class SimpleThresholdingType(Enum):
    THRESH_BINARY = 1
    THRESH_BINARY_INV = 2
    THRESH_TRUNC = 3
    THRESH_TOZERO = 4
    THRESH_TOZERO_INV = 5
    THRESH_BINARY+THRESH_OTSU = 6
