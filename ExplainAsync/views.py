# -*- coding: utf-8 -*-
from os.path import dirname
from os.path import join as joinpath

from sanic import Blueprint
from sanic.response import json
from sanic.exceptions import NotFound
from sanic_session import InMemorySessionInterface

from . session import create_redis_session
from . templates import create_template_env

site = Blueprint('site')

site.static('', joinpath(dirname(__file__), 'static'))

jinja = create_template_env()
session = InMemorySessionInterface()

@site.middleware('request')
async def add_session_to_request(request):
    await session.open(request)

@site.middleware('response')
async def save_session(request, response):
    await session.save(request, response)

@site.exception(NotFound)
async def error(request, exception):
    return jinja.render('404.html', request)

@site.route('/')
async def index(request):
    return jinja.render('index.html', request)
