# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

#add additional css files here if you have them seperate(like navbar, etc)
css = Bundle(
    'libs/bootstrap/dist/css/bootstrap.css',
    'css/style.css',
    'css/navbar.css',
    'css/footer.css',
    'css/public.css',
    'css/home.css',
    'css/agency.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'libs/jQuery/dist/jquery.js',
    'libs/bootstrap/dist/js/bootstrap.js',
    'js/plugins.js',
    'js/home.js',
    'js/scripts/jquery.counterup.min.js',
    'js/scripts/waypoints.min.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
