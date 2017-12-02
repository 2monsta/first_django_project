# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(req):
	my_dictionary={"insert_me":"Hello i'm from views.py"}
	return render(req, 'index.html', context=my_dictionary)
