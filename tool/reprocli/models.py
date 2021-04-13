#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class CompendiumPack:
    """Class to represent a processed Research Compendium
    """
    def __init__(self, file, metadata):
        self._file = file
        self._metadata = metadata
        
    @property
    def file(self):
        return self._file
    
    @property
    def metadata(self):
        return self._metadata
