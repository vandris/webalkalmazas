#from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template import loader
from django.shortcuts import render
from .models import Adds

def index(request):
	list = Adds.objects
	context = {
		'list': list,
	}
	return render(request, 'polls/index.html', context)

def adds(request, id):
	response = "You are searchingfor the %s"
	return HttpResponse(response % id)