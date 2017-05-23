# -*- coding: utf-8 -*-
from sanic import Sanic
from dateutil.parser import parser


def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    p = parser()
    dt = p.parse(value)
    return dt.strftime(format)

def create_app(cfg=None):
    app = Sanic(__name__, log_config=None)
    from . views import site, jinja
    jinja.init_app(app)
    app.jinja_env.filters['datetimefilter'] = datetimefilter
    app.blueprint(site)
    return app
