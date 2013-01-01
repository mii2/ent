# -*- coding: utf-8 -*-

from bottle import run, route, template
import ent

config = ent.Configurator()

@route('/')
def root_dir():
    return unicode(config.parser['sqlite']).decode('unicode-escape')
    #return template('../templ/index.tpl')
    
run(reloader=True)