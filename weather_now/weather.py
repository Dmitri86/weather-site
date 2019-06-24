# import requests
# url = 'http://api.openweathermap.org/data/2.5/weather'
#
# while True:
#     city = input('Enter current city: ')
#     if city == 'q':
#         break
#     params = {
#         'q': city,
#         'appid': '11c0d3dc6093f7442898ee49d2430d20',
#         'units': 'metric'}
#     res = requests.get(url, params=params)
#     print(res.status_code)
#     data = res.json()
#     print('Current temperature in {} is {} with humidity {}%. It\'s {}'.format(city,
#             data['main']['temp'], data['main']['humidity'], data['weather'][0]['main']))
#     print('Coordinates:  longitude: {}, latitude: {}'.format(data['coord']['lon'], data['coord']['lat']))
#     print('International cod {} is {}'.format(city, data['id']))
#

def weath(city):
    import requests
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': '11c0d3dc6093f7442898ee49d2430d20',
        'units': 'metric'}
    res = requests.get(url, params=params)
    if res.status_code == 200:
        data = res.json()
        return {'city' : city, 'temperature': data['main']['temp'], 'humidity': data['main']['humidity'], 'description': data['weather'][0]['description'], 'icon': data['weather'][0]['icon'], 'wind':
                data['wind']['speed'], 'pressure': data['main']['pressure'],
                'direct': data.get('wind').get('deg', " "),
                'sunrise': data['sys']['sunrise'], 'sunset': data['sys']['sunset']}
    else:
        return {}
    # return 'Current temperature in {} is {} with humidity \
    #  {}%. It\'s {}'.format(city, data['main']['temp'], data['main']['humidity'], data['weather'][0]['main'])
