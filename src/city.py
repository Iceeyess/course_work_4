import requests


class City:
    """Класс для определения параметра id города по API"""
    def __init__(self, url: str, city: str) -> None:
        self.url, self.city = url, city
        self.common_cities_dict = requests.get(self.url).json()

    def get_city_id(self) -> str:
        """Метод парсит все населенные пункты hh API и по поисковому значению
        self.city возвращает id города """

        cities_dictionary = {}
        for d_country in self.common_cities_dict:
            if not d_country['areas']:
                cities_dictionary.setdefault(d_country['name'], int(d_country['id']))
            for d_area in d_country['areas']:
                if not d_area['areas']:
                    cities_dictionary.setdefault(d_area['name'], int(d_area['id']))
                for d_city in d_area['areas']:
                    if not d_city['areas']:
                        cities_dictionary.setdefault(d_city['name'], int(d_city['id']))
                    for d in d_city['areas']:
                        cities_dictionary.setdefault(d['name'], int(d['id']))
        return cities_dictionary.get(self.city)

