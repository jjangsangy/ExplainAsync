# -*- coding: utf-8 -*-
from os.path import dirname
from os.path import join as joinpath

from sanic import Blueprint
from sanic.response import json
from sanic_jinja2 import SanicJinja2

from . session import create_session

site = Blueprint('site')
jinja = SanicJinja2()
session = create_session()

site.static('', joinpath(dirname(__file__), 'static'))

@site.middleware('request')
async def add_session_to_request(request):
    await session.open(request)

@site.middleware('response')
async def save_session(request, response):
    await session.save(request, response)

@site.route('/')
async def index(request):
    return jinja.render('index.html', request, greetings='Hello, sanic!')
