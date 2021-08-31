from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
import requests
import json

from .models import Clothing


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


def signupfunc(request):
    # formから受けとったデータを取ってくるためのコード
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some': 100})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザはすでに登録されています。'})
    return render(request, 'signup.html', {'some': 100})


def loginfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('top')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {})
    # postではなく、getメソッドが入ったとき
    return render(request, 'login.html', {'context': 'get method'})


def logoutfunc(request):
   logout(request)
   return redirect('login')


class TopView(ListView, LoginRequiredMixin):
    template_name = 'top.html'
    model = Clothing


class ClothingList(ListView, LoginRequiredMixin):
    template_name = 'clothinglist.html'
    model = Clothing


class ClothingDetail(DetailView, LoginRequiredMixin):
    template_name = 'clothingdetail.html'
    model = Clothing


class ClothingRegister(CreateView, LoginRequiredMixin):
    template_name = 'clothingregister.html'
    model = Clothing
    fields = ('sleeve', 'thick', 'color', 'brand')
    success_url = reverse_lazy('top')


class ClothingDelete(DeleteView, LoginRequiredMixin):
    template_name = 'clothingdelete.html'
    model = Clothing
    success_url = reverse_lazy('top')


class ClothingUpdate(UpdateView, LoginRequiredMixin):
    template_name = 'clothingupdate.html'
    model = Clothing
    fields = ('sleeve', 'thick', 'color', 'brand')
    success_url = reverse_lazy('top')


def forecast(request):
    params = {
        'city': '',
        'msg': '今日の天気は？',
        'weather': '',
    }
    return render(request, 'top.html', params)


def form(request):
    if request.POST['city']:

        city = request.POST['city']
        OpenWeatherAPI_Key = '取得したAPIKey'
        # 選択できるようにしたいけど、とりあえず東京で設定しておく
        API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}&lang=ja'

        url = API_URL.format(q=city, key=OpenWeatherAPI_Key)
        res = requests.get(url)
        data = json.loads(res.text)
        city = data["name"]
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        icon = data["weather"][0]["icon"]
        weatherID = data["weather"][0]["id"]

        # if temperature >= 24:
        #     todaysClothing = '半袖'
        # elif 20 < temperature < 24:
        #     if weatherID == 800:
        #         todaysClothing = '半袖'
        #     else:
        #         todaysClothing = '長袖'
        # elif 20 > temperature:
        #     todaysClothing = '長袖'

        params = {
            'city': city,
            'msg': '',
            'weather': weather,
            'temperature': int(temperature - 273.15),
            'icon': icon,
            # 'todaysClothing': todaysClothing,
        }

    else:
        params = {
            'city': '',
            'msg': '街を選んでください',
            'weather': '',
            'temperature': '',
            'icon': '',
            'todaysClothing': '',
        }

    return render(request, 'top.html', params)


