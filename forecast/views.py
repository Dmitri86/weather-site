from django.shortcuts import render, redirect, reverse
from . import forecast, tomorrow
import time
from datetime import date, timedelta
from . import Form

def forecast_answ(request, city):
    answ = forecast.forc(city)
    if answ != []:
        day_0, day_1, day_2, day_3, day_4 = answ
        tm = time.localtime()
        fmt = '%A'
        t = time.strftime(fmt, tm)
        day0_day_of_week = t
        day1_day_of_week = tomorrow.tommorow(day0_day_of_week)
        day2_day_of_week = tomorrow.tommorow(day1_day_of_week)
        day3_day_of_week = tomorrow.tommorow(day2_day_of_week)
        day4_day_of_week = tomorrow.tommorow(day3_day_of_week)

        dt = date.today()
        day0_date = str(dt.day)+ '/' + str(dt.month) +'/' + str(dt.year)
        next_dt_1 = dt + timedelta(days=1)
        day1_date = str(next_dt_1.day) + '/' + str(next_dt_1.month) + '/' + str(next_dt_1.year)
        next_dt_2 = dt + timedelta(days=2)
        day2_date = str(next_dt_2.day) +'/' + str(next_dt_2.month) + '/' + str(next_dt_2.year)
        next_dt_3 = dt + timedelta(days=3)
        day3_date = str(next_dt_3.day) + '/'+ str(next_dt_3.month) + '/' + str(next_dt_3.year)
        next_dt_4 = dt + timedelta(days=4)
        day4_date = str(next_dt_4.day) + '/' + str(next_dt_4.month) + '/' + str(next_dt_4.year)







        data = {'day_0_d_t': round(day_0['day']['temp']),
                'day_0_d_i': "http://openweathermap.org/img/w/" + day_0['day']['icon']+ ".png" ,
                'day_0_d_d': day_0['day']['description'], 'day_0_d_h': day_0['day']['humidity'],
                'day_0_n_t': round(day_0['night']['temp']),
                'day_0_n_i': "http://openweathermap.org/img/w/" + day_0['night']['icon']+ ".png",
                'day_0_n_d': day_0['night']['description'], 'day_0_n_h': day_0['night']['humidity'],
                'day_1_d_t': round(day_1['day']['temp']),
                'day_1_d_i': "http://openweathermap.org/img/w/" + day_1['day']['icon']+ ".png",
                'day_1_d_d': day_1['day']['description'], 'day_1_d_h': day_0['day']['humidity'],
                'day_1_n_t': round(day_1['night']['temp']),
                'day_1_n_i': "http://openweathermap.org/img/w/" + day_1['night']['icon']+ ".png",
                'day_1_n_d': day_1['night']['description'], 'day_1_n_h': day_1['night']['humidity'],
                'day_2_d_t': round(day_2['day']['temp']),
                'day_2_d_i': "http://openweathermap.org/img/w/" + day_2['day']['icon']+ ".png",
                'day_2_d_d': day_0['day']['description'], 'day_2_d_h': day_2['day']['humidity'],
                'day_2_n_t': round(day_2['night']['temp']),
                'day_2_n_i': "http://openweathermap.org/img/w/" + day_2['night']['icon'] + ".png",
                'day_2_n_d': day_2['night']['description'], 'day_2_n_h': day_2['night']['humidity'],
                'day_3_d_t': round(day_3['day']['temp']),
                'day_3_d_i': "http://openweathermap.org/img/w/" + day_3['day']['icon']+ ".png",
                'day_3_d_d': day_3['day']['description'], 'day_3_d_h': day_3['day']['humidity'],
                'day_3_n_t': round(day_3['night']['temp']) ,
                'day_3_n_i': "http://openweathermap.org/img/w/" + day_3['night']['icon']+ ".png",
                'day_3_n_d': day_3['night']['description'], 'day_3_n_h': day_3['night']['humidity'],
                'day_4_d_t': round(day_4['day']['temp']),
                'day_4_d_i': "http://openweathermap.org/img/w/" + day_4['day']['icon']+ ".png",
                'day_4_d_d': day_4['day']['description'], 'day_4_d_h': day_4['day']['humidity'],
                'day_4_n_t': round(day_4['night']['temp']),
                'day_4_n_i': "http://openweathermap.org/img/w/" + day_4['night']['icon']+ ".png",
                'day_4_n_d': day_4['night']['description'], 'day_4_n_h': day_4['night']['humidity'],
                'city': city, 'day0_DOW': day0_day_of_week, 'day1_DOW': day1_day_of_week,
                'day2_DOW': day2_day_of_week, 'day3_DOW': day3_day_of_week, 'day4_DOW': day4_day_of_week,
                'day0_date': day0_date, 'day1_date': day1_date, 'day2_date': day2_date,
                'day3_date': day3_date, 'day4_date': day4_date,
                }



        return render(request, 'forecast/answer.html', data)


    else:
        return render(request, 'forecast/wrong.html')


def show(request):
    form = Form.NameCity()

    if request.method == "POST":
        form = Form.NameCity(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            return redirect(reverse('forecast_url', kwargs={'city': city}))

    return render(request, 'forecast/show.html', context={'form': form})