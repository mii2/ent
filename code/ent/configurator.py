# -*- coding: utf-8 -*-

from configobj import ConfigObj

class Configurator:
    def __init__(self, filename=u'../config/main.cfg'):
        '''The main configuration. Busines-logic do not use this class. It use config-files, but logic use DB'''
        self._filename = filename
        self.parser = ConfigObj(self._filename, default_encoding='utf-8', encoding='utf-8')