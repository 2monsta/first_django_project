# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
	return HttpResponse("<em>My SECOND project </em>")

def help(req):
	mydictionary = {'insert_me': "HELP PAGE"}
	return render(req, 'AppTwo/help.html', context=mydictionary)

def hello(req):
	mydictionary = {"hello_world": "Hello WORLD"}
	return render(req, 'AppTwo/hello.html', context=mydictionary)