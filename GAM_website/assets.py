# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

#add additional css files here if you have them seperate(like navbar, etc)
less = Bundle(
    'less/agency.less',
    'less/mixins.less',
    'less/variables.less',
    filters='less',
    output='agency.css'
)

css = Bundle(
    'libs/bootstrap/dist/css/bootstrap.css',
    'libs/font-awesome4/css/font-awesome.min.css',
    'css/style.css',
    'css/navbar.css',
    'css/footer.css',
    'css/public.css',
    'css/home.css',
    # 'css/agency.css',
    less,
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
#     'libs/jquery/dist/jquery.js',
    # "https://use.fontawesome.com/f5c804bdc2.js",
    'libs/bootstrap/dist/js/bootstrap.js',
    'js/plugins.js',
    'js/agency.js',
    'js/home.js',
    'js/jqBootstrapValidation.js',
    'js/contact_me.js',
    'js/waypoints.min.js',
    'js/jquery.easing.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
