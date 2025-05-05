from creds import api_token, url
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)



def result_place(place, city) -> list:
    """Функция по работе с APi и выводу мест"""

    logger.info(f"Поиск мест по запросу: '{place}' в городе: '{city}'")

    places = []
    params = {
        'query': place,
        'near': city,
        'limit': 10,
    }
    headers = {
        'Authorization': api_token,
    }


    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        logger.info("Запрос выполнен успешно")

    except requests.exceptions.HTTPError as e:
        logger.info(f'Ошибка при запросе {e}')
        return e

    else:
        data = response.json()

        for place in data['results']:
            name = place['name']
            location = place['location']
            address = location.get('address', 'Адрес не указан')

            new_place = {'name': name, 'address': address, 'city': city}
            places.append(new_place)

        logger.info(f"Места найдены успешно")
        return places