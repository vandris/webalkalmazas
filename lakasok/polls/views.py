#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello itt vagyok!")

def adds(request, id):
	response = "You are searchingfor the %s"
	return HttpResponse(response % id)