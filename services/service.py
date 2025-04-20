from creds import api_token, url
import requests



def result_place(place, city):
    places = []
    params = {
        'query': place,
        'near': city,
        'limit': 10,
    }
    headers = {
        'Authorization': api_token,
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        for place in data['results']:
            name = place['name']
            location = place['location']
            address = location.get('address', 'Адрес не указан')

            new_place = {'name': name, 'address': address, 'city': city}
            places.append(new_place)

        return places

    else:
         return f'Ошибка {response.status_code}'