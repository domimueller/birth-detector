#!/usr/bin/python
#-*- coding: utf-8 -*-

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.reader = None
        self.writer = None
        self.brightenConfig = None
        self.colorspaceConvertConfig = None
        self.filterConfig = None
        self.threshConfig = None

    def brightenImage(self, image, config):
        pass

    def convertColorSpace(self, image, config):
        pass

    def filterImage(self, image, config):
        pass

    def segmentImage(self, image, config):
        pass

