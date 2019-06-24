def forc(city):
    import requests
    url = 'http://api.openweathermap.org/data/2.5/forecast/'
    params = {
        'q': city,
        'appid': '11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric'}
    res = requests.get(url, params=params)
    data = res.json()
    forcas = []
    if res.status_code == 200:
        forcas.append(data['list'][0])
        for x in range(40):
            if data['list'][x]['dt_txt'].endswith('00:00:00') or data['list'][x]['dt_txt'].endswith('12:00:00'):
                forcas.append(data['list'][x])
        if forcas[-1]['dt_txt'].endswith('12:00:00'):
            forcas.pop(-1)
        if forcas[1]['dt_txt'].endswith('12:00:00'):
            forcas.pop(0)


        day = {'temp': forcas[0]['main']['temp'], 'icon': forcas[0]['weather'][0]['icon'],
                         'description': forcas[0]['weather'][0]['description'],
                        'humidity': forcas[0]['main']['humidity']}
        night = {'temp': forcas[1]['main']['temp'], 'icon': forcas[1]['weather'][0]['icon'],
                         'description': forcas[1]['weather'][0]['description'],
                        'humidity': forcas[1]['main']['humidity']}

        today = {'day': day, 'night': night}

        day = {'temp': forcas[2]['main']['temp'], 'icon': forcas[2]['weather'][0]['icon'],
                         'description': forcas[2]['weather'][0]['description'],
                        'humidity': forcas[2]['main']['humidity']}
        night = {'temp': forcas[3]['main']['temp'], 'icon': forcas[3]['weather'][0]['icon'],
                         'description': forcas[3]['weather'][0]['description'],
                        'humidity': forcas[3]['main']['humidity']}
        tomorrow = {'day': day, 'night': night}

        day = {'temp': forcas[4]['main']['temp'], 'icon': forcas[4]['weather'][0]['icon'],
                         'description': forcas[4]['weather'][0]['description'],
                        'humidity': forcas[4]['main']['humidity']}
        night = {'temp': forcas[5]['main']['temp'], 'icon': forcas[5]['weather'][0]['icon'],
                         'description': forcas[5]['weather'][0]['description'],
                        'humidity': forcas[5]['main']['humidity']}
        day_3 = {'day': day, 'night': night}

        day = {'temp': forcas[6]['main']['temp'], 'icon': forcas[6]['weather'][0]['icon'],
                         'description': forcas[6]['weather'][0]['description'],
                        'humidity': forcas[6]['main']['humidity']}
        night = {'temp': forcas[7]['main']['temp'], 'icon': forcas[7]['weather'][0]['icon'],
                         'description': forcas[7]['weather'][0]['description'],
                        'humidity': forcas[7]['main']['humidity']}
        day_4 = {'day': day, 'night': night}

        day = {'temp': forcas[8]['main']['temp'], 'icon': forcas[8]['weather'][0]['icon'],
                         'description': forcas[8]['weather'][0]['description'],
                        'humidity': forcas[8]['main']['humidity']}
        night = {'temp': forcas[9]['main']['temp'], 'icon': forcas[9]['weather'][0]['icon'],
                         'description': forcas[9]['weather'][0]['description'],
                        'humidity': forcas[9]['main']['humidity']}
        day_5 = {'day': day, 'night': night}

        result = [today, tomorrow, day_3, day_4, day_5]
        return result
    else:
        return forcas



if __name__ == '__main__':
    city = input()
    print(forecas(city))



