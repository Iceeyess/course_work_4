import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """Класс-шаблон для определения вакансий"""
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self):
        pass

    @staticmethod
    @abstractmethod
    def get_city_id(url: str, city: str):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker, url, headers, params) -> None:
        self.url = url
        self.headers = headers
        self.params = params
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword: str, page_quantity: int) -> None:
        """Функция запрашивает по API вакансии и сохраняет их в self.vacancies атрибут"""
        self.params['text'] = keyword
        while self.params.get('page') != page_quantity:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    @staticmethod
    def get_city_id(url: str, city: str) -> str:
        """Метод парсит все населенные пункты hh по API и возвращает id города
        Константа url приходит из модуля констант(links_constants)"""

        common_cities_dict = requests.get(url).json()
        cities_dictionary = {}
        for d_country in common_cities_dict:
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
        return cities_dictionary.get(city)

