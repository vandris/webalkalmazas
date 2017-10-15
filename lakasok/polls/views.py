#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Adds

def index(request):
	list = Adds.objects.order_by('id')
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': list,
	}
	return HttpResponse(template.render(context, request))

def adds(request, id):
	response = "You are searchingfor the %s"
	return HttpResponse(response % id)