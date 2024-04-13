from src.vacancy import Vacancy
from abc import ABC, abstractmethod
from src.hh import HH
import json


class ManageJSON(ABC):
    """Класс-шаблон для определения методов, а так же атрибутов"""
    def __init__(self, vacancy_list: [HH]) -> None:
        # Инициализация объекта класса HH (список с типом классов вакансии)
        self.vacancy_list = [Vacancy(**_) for _ in vacancy_list.vacancies]
        self.file_name = vacancy_list.file_worker

    @abstractmethod
    def save_to_file(self):
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

    def save_to_file(func):
        """Функция-декоратор открытия файла на чтение и занесение в файл данных, то есть преобразование
        ЭК Vacancy в обычный словарь и сохранение в файл"""
        def wrapper(self, *args, **kwargs) -> None:
            func(self, *args, **kwargs)
            with open(self.file_name, mode='w', encoding='utf-8') as file:
                list_ = []
                for vacancy in self.vacancy_list:
                    list_.append(vacancy.get_self_dict)
                s = json.dumps(list_, ensure_ascii=False)
                file.write(s)
        return wrapper

    def save_to_file_separately(self):
        """вынужден был создать класс, да знаю, что не по DRY поскольку есть такой же save_to_file, но он отдельно не
        вызывался без класса, который должен декорировать, если можешь, то посоветуй как быть при условии если JSON
        файла еще нет и он не создан"""
        with open(self.file_name, mode='w', encoding='utf-8') as file:
            list_ = []
            for vacancy in self.vacancy_list:
                list_.append(vacancy.get_self_dict)
            s = json.dumps(list_, ensure_ascii=False)
            file.write(s)
    @save_to_file
    def sort_by_salary(self):
        with open(self.file_name, mode='r', encoding='utf-8') as file:
            # Преобразуем список словарей в ЭК Vacancy
            dict_list = [Vacancy(**_) for _ in json.load(file)]
            # Сортируем по убыванию
            dict_list.sort(reverse=True, key=lambda x: x.salary)
            # Печатаем сортировку
            print(f'ВЫВОЖУ РЕЗУЛЬТАТЫ СОРТИРОВКИ')
            [print(_) for _ in dict_list]

    def get_top(self, num):
        """Печатаем топ 10 вакансий, на вход получает количество вакансий, которые надо отобразить"""
        with open(self.file_name, mode='r', encoding='utf-8') as file:
            # Преобразуем список словарей в ЭК Vacancy
            dict_list = [Vacancy(**_) for _ in json.load(file)]
            # Сортируем по убыванию
            dict_list.sort(reverse=True, key=lambda x: x.salary)
            # Печатаем сортировку
            print(f'ВЫВОЖУ ТОП-10')
            [print(_) for _ in dict_list[:10]]
    def delete_vacancy(self, index):
        ...


