from django.shortcuts import render, redirect, reverse
from . import Form
from . import weather
import time
import re
from django.conf.urls import url

CITY = 0
# Create your views here.
def index(request):
    form = Form.NameCity()



    if request.method == "POST":
        form = Form.NameCity(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            return redirect(reverse('answer_url', kwargs={'city':city}))



    return render(request, 'weather_now/weather.html', context={'form': form})

def answer(request, city):
    answ = weather.weath(city)
    if answ != {}:
        town = answ['city']
        temp = round(answ['temperature'])
        humidity = answ['humidity']
        description = answ['description']
        icon = "http://openweathermap.org/img/w/" + answ['icon'] + ".png"
        wind = answ['wind']
        pressure = answ['pressure']
        if answ['direct'] != ' ':
            if answ['direct'] == 90:
                direct = 'north'
            elif answ['direct'] == 180:
                direct = 'west'
            elif answ['direct'] == 270:
                direct = 'south'
            elif answ['direct'] == 360 or answ['direct'] == 0:
                direct = 'east'
            elif 0 < answ['direct'] < 90:
                direct = 'north-east'
            elif 90 < answ['direct'] < 180:
                direct = 'north-west'
            elif 180 < answ['direct'] < 270:
                direct = 'south-west'
            elif 270 < answ['direct'] < 360:
                direct = 'south-east'
        else:
            direct = ''
        sunrise = re.findall(r"\d\d:\d\d:\d\d", time.ctime(answ['sunrise']))[0]
        sunset = re.findall(r"\d\d:\d\d:\d\d", time.ctime(answ['sunset']))[0]
        return render(request, 'weather_now/answer.html', context={'city': town,
                                                                   'temp': temp,
                                                                   'humidity': humidity,
                                                                   'description': description,
                                                                   'icon': icon,
                                                                   'wind': wind,
                                                                   'pressure': pressure,
                                                                   'direction': direct,
                                                                   'sunrise': sunrise,
                                                                   'sunset': sunset})
    else:
        return render(request, 'weather_now/wrong.html')

def enter(request):
    form = Form.NameCity()

    if request.method == "POST":
        form = Form.NameCity(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            return redirect(reverse('answer_url', kwargs={'city': city}))

    return render(request, 'weather_now/answ.html', context={'form': form})

