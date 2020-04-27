#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import Enum

class ColorSpaceConversionType(Enum):
    COLOR_BGR2GRAY = 1
    COLOR_BGR2HSV = 2
    COLOR_HSV2BGR = 3
    COLOR_GRAY2BGR = 4
    COLOR_BGR2YUV = 5
    COLOR_YUV2BGR = 6
