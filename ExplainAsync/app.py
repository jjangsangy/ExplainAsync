# -*- coding: utf-8 -*-
from sanic import Sanic

def create_app(cfg=None):
    app = Sanic(__name__, log_config=None)
    from . views import site, jinja
    jinja.init_app(app)
    app.blueprint(site)
    return app
