#from django.shortcuts import render

# Create your views here.
from django.http import HttsResponse

def index(request):
	return HttpResponse("Hello itt vagyok!")
