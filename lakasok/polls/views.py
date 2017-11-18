#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template import loader
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Adds
from .models import Users
from .models import Messages
from django.db import connection
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import AddForm
from django.contrib.auth.models import User



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
	getYear = request.GET.get('year')
	getFurnitured = request.GET.get('furnitured')
	getLift = request.GET.get('lift')
	getParking = request.GET.get('parking')
	getView = request.GET.get('view')
	getCity = request.GET.get('city')
	getStreet = request.GET.get('street')
	getNumber = request.GET.get('number')
	getDescriptions = request.GET.get('description')
	getAddress = getCity +" " + getStreet + " " + getNumber + "."
	MyAddForm = AddForm(request.GET, request.FILES)
	adds = Adds(owner = request.user, squaremeter = getsquaremeter, price = getPrice, type = getType, wall = getWall, heating = getHeating, state = getState, rooms = getRooms, parking = getParking, year = getYear, furnitured = getFurnitured, lift = getLift, view = getView, address = getAddress, country = getCountry, description = getDescriptions, picture=AddForm["picture"])
	#print("........picture.........",adds.picture)
	adds.save()
	return render(request, 'polls/created.html', {})

def searchHouse(request):
	getCountry = request.GET.getlist('megye')
	list = Adds.objects.filter(country)
	list=Adds.objects.filter(country="Lall")
	for a in getCountry:
		list.join(Adds.objects.filter(country=a)[:30])
	context = {
		'list': list
	}
	return render(request, 'polls/search.html', context)

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
	list = Adds.objects.order_by('owner')[:100]
	context = {
		'list': list
	}
	return render(request, 'polls/search.html', context)

def login(request):
	if request.user.is_authenticated:
		return render(request, 'polls/warning_a.html', {})
	else:
		return render(request, 'polls/login.html', {})


def addadd(request):
	if request.user.is_authenticated:
		return render(request, 'polls/addadd.html', {})
	else:
		return render(request, 'polls/warning_na.html', {})

def contact(request):
	add_id = request.GET.getlist('id')
	name = Adds.objects.filter(id = add_id[0])
	list = User.objects.filter(username = name[0].owner)
	context = {
		'list': list
	}
	return render(request, 'polls/connect.html', context)

def messages(request):
	list = Messages.objects.filter(Q(sender = request.user.username) | Q(receiver = request.user.username))
	context = {
		'list': list
	}
	return render(request, 'polls/messages.html', context)

def send_messages(request):
	if request.GET.get("sender") == request.user.username:
		name = request.GET.get("receiver")
	else:
		name = request.GET.get("sender")
	list = Messages.objects.filter(sender = name)[:1]
	context = {
		'list': list
	}
	return render(request, 'polls/send_messages.html', context)

def send_newmessages(request):
	getReceiver = request.GET.get('receiver')
	getSender = request.user.username
	getMessage = request.GET.get('message')
	mess = Messages(sender = getSender, receiver = getReceiver, message = getMessage, valid = 1, unread = 1)
	mess.save()
	return render(request, 'polls/sent.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'polls/signup.html', {'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'A jelszavadat sikeresen megváltoztattuk!')
            return redirect('change_password')
        else:
            messages.error(request, 'Hiba lépett fel.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'polls/change_password_2.html', {
        'form': form
    })