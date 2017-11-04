#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template import loader
from django.shortcuts import render
from .models import Adds
from django.db import connection

def addHouse(request):
	getCountry = request.GET.get('country')
	#getOwner = request.GET.get('owner')
	getsquaremeter = request.GET.get('squaremeter')
	getPrice = request.GET.get('price')
	getType = request.GET.get('type')
	getWall = request.GET.get('wall')
	getHeating = request.GET.get('heating')
	getState = request.GET.get('state')
	getRooms = request.GET.get('rooms')
	getParking = request.GET.get('parking')
	getYear = request.GET.get('year')
	getFurnitured = request.GET.get('furnitured')
	getLift = request.GET.get('lift')
	getParking = request.GET.get('parking')
	getView = request.GET.get('view')
	getCity = request.GET.get('city')
	getStreet = request.GET.get('street')
	getNumber = request.GET.get('number')
	getAddress = getCity +" " + getStreet + " " + getNumber + "."
	adds = Adds(owner = "Nori", squaremeter = getsquaremeter, price = getPrice, type = getType, wall = getWall, heating = getHeating, state = getState, rooms = getRooms, parking = getParking, year = getYear, furnitured = getFurnitured, lift = getLift, view = getView, address = getAddress, country = getCountry)
	adds.save()
	return render(request, 'polls/felvesz.html', {})

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
	return render(request, 'polls/login.html', {})

def addadd(request):
	return render(request, 'polls/addadd.html', {})