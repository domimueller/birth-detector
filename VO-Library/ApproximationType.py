#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import Enum

class ApproximationType(Enum):
    CHAIN_APPROX_NONE = 1
    CHAIN_APPROX_SIMPLE = 2
    CHAIN_APPROX_TC89_L1 = 3
    CHAIN_APPROX_TC89_KCOS = 4
