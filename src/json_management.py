from src.vacancy import Vacancy
from abc import ABC, abstractmethod
from src.hh import HH
import json


class ManageJSON(ABC):
    """Класс-шаблон для определения методов, а так же атрибутов"""
    def __init__(self, vacancy_list: [HH]) -> None:
        # Инициализация объекта класса HH (список с типом классов вакансии) и сохранение в JSON
        self.file_name = vacancy_list.file_worker
        self.vacancy_list = [Vacancy(**_) for _ in vacancy_list.vacancies]
        with open(self.file_name, mode='w', encoding='utf-8') as f:
            list_ = []
            for vacancy in self.vacancy_list:
                list_.append(vacancy.get_self_dict)
            s = json.dumps(list_, ensure_ascii=False)
            f.write(s)
        self.vacancy_list = []  #Обнуляем, чтобы не занимать память
        self.dict_list = []

    @abstractmethod
    def load_and_save_file(self):
        pass

    @abstractmethod
    def sort_by_salary(self):
        pass

    @abstractmethod
    def get_top(self, num):
        pass

    @abstractmethod
    def delete_vacancy(self, index):
        pass


class JSONManagement(ManageJSON):
    """Класс для управления данными, для записи, сортировки, обработки и """
    def __init__(self, vacancy_list: [HH]) -> None:
        super().__init__(vacancy_list)

    def load_and_save_file(func):
        """Функция-декоратор читает файл и преобразует список в ЭК Vacancy"""
        def wrapper(self, *args, **kwargs):
            with open(self.file_name, mode='r', encoding='utf-8') as file:
                self.dict_list = [Vacancy(**_) for _ in json.load(file)]
            func(self)
            with open(self.file_name, mode='w', encoding='utf-8') as file:
                list_ = []
                for vacancy in self.dict_list:
                    list_.append(vacancy.get_self_dict)
                s = json.dumps(list_, ensure_ascii=False)
                file.write(s)
        return wrapper

    @load_and_save_file
    def sort_by_salary(self):
        # Сортируем по убыванию
        self.dict_list.sort(reverse=True, key=lambda x: x.salary)
        # Печатаем сортировку
        print(f'ВЫВОЖУ РЕЗУЛЬТАТЫ СОРТИРОВКИ')
        [print(_) for _ in self.dict_list]


    def get_top(self, num):
        """Печатаем топ num вакансий, на вход получает количество вакансий, которые надо отобразить"""
        # Печатаем сортировку
        print(f'ВЫВОЖУ ТОП-{num}')
        [print(_) for _ in self.dict_list[:num]]
    def delete_vacancy(self, index):
        ...


