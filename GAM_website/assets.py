# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

#add additional css files here if you have them seperate(like navbar, etc)
css = Bundle(
    'libs/bootstrap/dist/css/bootstrap.css',
    'css/style.css',
    'css/navbar.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'libs/jQuery/dist/jquery.js',
    'libs/bootstrap/dist/js/bootstrap.js',
    'js/plugins.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
