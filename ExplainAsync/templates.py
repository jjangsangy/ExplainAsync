from sanic_jinja2 import SanicJinja2
from dateutil.parser import parser as dateparser

__all__ = 'create_template_env', 'datetimefilter'

def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    p = dateparser()
    dt = p.parse(value)
    return dt.strftime(format)

def create_template_env():
    jinja = SanicJinja2()
    jinja.env.filters['datetimefilter'] = datetimefilter
    return jinja
