# -*- coding: utf-8 -*-
from os.path import dirname
from os.path import join as joinpath

from sanic import Blueprint
from sanic.response import json
from sanic_jinja2 import SanicJinja2
from sanic_session import InMemorySessionInterface

from . session import create_session

site = Blueprint('site')
jinja = SanicJinja2()

site.static('', joinpath(dirname(__file__), 'static'))

session = InMemorySessionInterface()


@site.middleware('request')
async def add_session_to_request(request):
    await session.open(request)

@site.middleware('response')
async def save_session(request, response):
    await session.save(request, response)

@site.route('/')
async def index(request):
    return jinja.render('index.html', request, greetings='Hello, sanic!')
