#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template import loader
from django.shortcuts import render
from .models import Adds
from django.db import connection

def addHouse():
	adds = Adds(owner = "lom", squaremeter = 14, price = 500, type = "tegla", wall = "tegla", heating = "meleg", state = "jo", rooms = 2, parking = "van", year = 1995, furnitured = "ja", lift = "ja", view = "van", address = "lalala", country = "newYork")
	adds.save()

def index(request):
	list = Adds.objects.order_by('owner')[:5]
	'''output = ', '.join([a.owner for a in list])
	return HttpResponse(output)'''
	context = {
		'list': list
	}
	return render(request, 'polls/index1.html', context)

def adds(request, id):
	response = "You are searchingfor the %s"
	return HttpResponse(response % id)

def search(request):
	list = Adds.objects.order_by('owner')[:5]
	'''output = ', '.join([a.owner for a in list])
	return HttpResponse(output)'''
	context = {
		'list': list
	}
	return render(request, 'polls/search.html', context)

def login(request):
	adds = Adds(owner = "lom", squaremeter = 14, price = 500, type = "tegla", wall = "tegla", heating = "meleg", state = "jo", rooms = 2, parking = "van", year = 1995, furnitured = "ja", lift = "ja", view = "van", address = "lalala", country = "newYork")
	adds.save()
	return render(request, 'polls/login.html', {})

def addadd(request):
	adds = Adds(owner = "looom", squaremeter = 14, price = 500, type = "tegla", wall = "tegla", heating = "meleg", state = "jo", rooms = 2, parking = "van", year = 1995, furnitured = "ja", lift = "ja", view = "van", address = "lalala", country = "newYork")
	adds.save()
	return render(request, 'polls/addadd.html', {})