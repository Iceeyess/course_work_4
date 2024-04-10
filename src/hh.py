import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """Класс-шаблон для определения вакансий"""
    def __init__(self, file_worker):
        self.file_worker = file_worker

    @abstractmethod
    def load_vacancies(self):
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

