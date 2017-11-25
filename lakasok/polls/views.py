# from django.shortcuts import render

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
from .forms import AddForm, AddsForm
from django.contrib.auth.models import User

"""""
def addHouse(request):
    getCountry = request.GET.get('country')
    # getOwner = request.GET.get('owner')
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
    getAddress = getCity + " " + getStreet + " " + getNumber + "."
    MyAddForm = AddForm(request.GET, request.FILES)
    adds = Adds(owner=request.user, squaremeter=getsquaremeter, price=getPrice, type=getType, wall=getWall,
                heating=getHeating, state=getState, rooms=getRooms, parking=getParking, year=getYear,
                furnitured=getFurnitured, lift=getLift, view=getView, address=getAddress, country=getCountry,
                description=getDescriptions, picture=AddForm["picture"])
    # print("........picture.........",adds.picture)
    adds.save()
    return render(request, 'polls/created.html', {})
"""
def addHouse(request):
    getCountry = request.POST.get('country')
    # getOwner = request.GET.get('owner')
    getsquaremeter = request.POST.get('squaremeter')
    getPrice = request.POST.get('price')
    getType = request.POST.get('type')
    getWall = request.POST.get('wall')
    getHeating = request.POST.get('heating')
    getState = request.POST.get('state')
    getRooms = request.POST.get('rooms')
    getYear = request.POST.get('year')
    getFurnitured = request.POST.get('furnitured')
    getLift = request.POST.get('lift')
    getParking = request.POST.get('parking')
    getView = request.POST.get('view')
    getCity = request.POST.get('city')
    getStreet = request.POST.get('street')
    getNumber = request.POST.get('number')
    getDescriptions = request.POST.get('description')
    getAddress = getCity + " " + getStreet + " " + getNumber + "."
    MyAddForm = AddForm(request.POST, request.FILES)
    adds = Adds(owner=request.user, squaremeter=getsquaremeter, price=getPrice, type=getType, wall=getWall,
                heating=getHeating, state=getState, rooms=getRooms, parking=getParking, year=getYear,
                furnitured=getFurnitured, lift=getLift, view=getView, address=getAddress, country=getCountry,
                description=getDescriptions,
                picture=request.FILES["picture"])
    # print("........picture.........",adds.picture)
    adds.save()
    return render(request, 'polls/created.html', {})

def searchHouse(request):
    getCountry = request.GET.getlist('country')
    getType = request.GET.getlist('type')
    getWall = request.GET.getlist('wall')
    getLift = request.GET.get('lift')
    getSquaremeter = request.GET.get('squaremeter')
    getPrice = request.GET.get('price')
    getYear = request.GET.get('year')
    getOrder = request.GET.get('order')
    talal = 'false'
    megyek = ['Budapest', 'Bács-Kiskun', 'Baranya', 'Békés', 'Borsod-Abaúj-Zemplén', 'Csongrád', 'Fejér',
              'Győr-Moson-Sopron', 'Hajdú-Bihar', 'Heves', 'Jász-Nagykun-Szolnok', 'Komárom-Esztergom', 'Nógrád',
              'Pest', 'Somogy', 'Szabolcs-Szatmár-Bereg', 'Tolna', 'Vas', 'Veszprém', 'Zala']
    haz = ['családi', 'társas', 'panel', 'iker', 'egyéb']
    falak = ['panel', 'tégla', 'vályog', 'ytong', 'fa', 'rönk', 'kő', 'egyéb']
    list = Adds.objects.exclude(country='alma')
    if len(getCountry) > 0:
        for i in megyek:
            talal = 'false'
            for j in getCountry:
                if i == j:
                    talal = 'true'
            if talal == 'false':
                list = list.exclude(country=i)
    if len(getType) > 0:
        for i in haz:
            talal = 'false'
            for j in getType:
                if i == j:
                    talal = 'true'
            if talal == 'false':
                list = list.exclude(type=i)
    if len(getWall) > 0:
        for i in falak:
            talal = 'false'
            for j in getWall:
                if i == j:
                    talal = 'true'
            if talal == 'false':
                list = list.exclude(wall=i)
    if getLift == 'van' or getLift == 'nincs':
        list = list.filter(lift=getLift)
    if getSquaremeter != '':
        list = list.filter(squaremeter__gte=getSquaremeter)
    if getPrice != '':
        list = list.filter(price__gte=getPrice)
    if getYear != '':
        list = list.filter(year__gte=getYear)
    if getOrder != 'ures':
        list = list.order_by(getOrder)
    # list = Adds.objects.exclude(country = 'Fejer')
    # list = list.filter(country= 'Budapest')
    # for a in getCountry:
    # list.join(Adds.objects.filter(country=a)[:30])
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
        if request.method == 'POST':
            form = AddsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = AddsForm()
        return render(request, 'polls/addadd.html', {'form': form})

    else:
        return render(request, 'polls/warning_na.html', {})


def contact(request):
    add_id = request.GET.getlist('id')
    name = Adds.objects.filter(id=add_id[0])
    list = User.objects.filter(username=name[0].owner)
    context = {
        'list': list
    }
    return render(request, 'polls/connect.html', context)


def messages(request):
    list = Messages.objects.filter(Q(sender=request.user.username) | Q(receiver=request.user.username))
    context = {
        'list': list
    }
    return render(request, 'polls/messages.html', context)


def search_owner(request):
    list = Adds.objects.filter(owner=request.user.username)
    context = {
        'list': list
    }
    return render(request, 'polls/search_owner.html', context)


def send_messages(request):
    if request.GET.get("sender") == request.user.username:
        name = request.GET.get("receiver")
    else:
        name = request.GET.get("sender")
    list = Messages.objects.filter(sender=name)[:1]
    context = {
        'list': list
    }
    return render(request, 'polls/send_messages.html', context)


def send_newmessages(request):
    getReceiver = request.GET.get('receiver')
    getSender = request.user.username
    getMessage = request.GET.get('message')
    mess = Messages(sender=getSender, receiver=getReceiver, message=getMessage, valid=1, unread=1)
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
        # return render(request, 'polls/signup.html', {'form': form})
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


def delete_user(request):
    getUsername = request.GET.get('name')
    user = User.objects.filter(username=getUsername)
    try:
        user.is_active = True
        # user.save()
        user.delete()
        return render(request, 'polls/user_deleted.html', {'deleted': True})
    except Exception as e:
        print(e.message)
        return render(request, 'front.html', {'err': e.message})


def delete_add(request):
    getId = request.GET.get('id')
    add = Adds.objects.filter(id=getId)
    add.delete()
    return render(request, 'polls/add_deleted.html', {})


def modify(request):
    getId = request.GET.get('id')
    list = Adds.objects.filter(id=getId)
    context = {
        'list': list
    }
    return render(request, 'polls/modify.html', context)


def modify_add(request):
    getId = request.GET.get('id')
    getCountry = request.GET.get('country')
    getAddress = request.GET.get('address')
    getSquaremeter = request.GET.get('squaremeter')
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
    getDescription = request.GET.get('description')
    add = Adds.objects.filter(id=getId)
    add.update(country=getCountry, address=getAddress, squaremeter=getSquaremeter, price=getPrice,
               type=getType, wall=getWall, heating=getHeating, state=getState, rooms=getRooms,
               year=getYear, furnitured=getFurnitured, lift=getLift, parking=getParking,
               view=getView, description=getDescription)
    return render(request, 'polls/modified_add.html', {})


def users(request):
    list = User.objects.exclude(username=request.user.username).order_by('username')
    context = {
        'list': list
    }
    return render(request, 'polls/users.html', context)
