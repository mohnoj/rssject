from django.shortcuts import render
from . import forms
from . import models
from django.http import HttpResponse
import feedparser
import re



def index(request):
    return render( request, 'rssfeed/index.html')

def results(request):
    if 'ln' in request.GET:
    	try:
    			feed = feedparser.parse(request.GET['ln'])
    			for entry in feed.entries:
    				s=(entry.description)
    				r=(entry.summary)
    				r= re.sub('<.*?>','',entry.summary)
    			for entry in feed.entries:
    				r=r+entry.link
    			models.link(url=request.GET['ln']).save()
    			return HttpResponse(r)
    	except KeyError:
    			return HttpResponse("invalid rss feed")
    else:
    	k='empty'
    	return HttpResponse(k)							



