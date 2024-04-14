from src.vacancy import Vacancy
from abc import ABC, abstractmethod
from src.hh import HH
import json


class ManageJSON(ABC):
    """Класс-шаблон для определения методов, а так же атрибутов
    Внимание! Работаем с методами, которые забирают данные из JSON-file и возвращают их обратно туда
    после всех действий. И что важно, что все действия производим не со словарями, а с ЭК класса Vacancy"""

    def __init__(self, dict_list: [HH]) -> None:
        # Инициализация объекта класса HH (список с типом классов вакансии) и сохранение в JSON
        self.file_name = dict_list.file_worker
        self.dict_list = [Vacancy(**_) for _ in dict_list.vacancies]
        with open(self.file_name, mode='w', encoding='utf-8') as f:
            list_ = []
            for vacancy in self.dict_list:
                list_.append(vacancy.get_self_dict)
            s = json.dumps(list_, ensure_ascii=False, indent=4)
            f.write(s)

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

    def __init__(self, dict_list: [HH]) -> None:
        super().__init__(dict_list)

    def load_and_save_file(func):
        """Функция-декоратор читает файл, преобразует список в ЭК Vacancy, выполняет функцию func,
        сохраняет данные обратно в файл"""

        def wrapper(self, *args, **kwargs):
            with open(self.file_name, mode='r', encoding='utf-8') as file:
                self.dict_list = [Vacancy(**_) for _ in json.load(file)]
            func(self, *args, *kwargs)
            with open(self.file_name, mode='w', encoding='utf-8') as file:
                list_ = []
                for vacancy in self.dict_list:
                    list_.append(vacancy.get_self_dict)
                s = json.dumps(list_, ensure_ascii=False, indent=4)
                file.write(s)
        return wrapper

    @load_and_save_file
    def sort_by_salary(self):
        # Сортируем по убыванию
        self.dict_list.sort(reverse=True, key=lambda x: x.salary)
        # Печатаем сортировку
        print(f'ВЫВОЖУ РЕЗУЛЬТАТЫ СОРТИРОВКИ')
        print('-' * 50)
        [print(_) for _ in self.dict_list]

    @load_and_save_file
    def get_top(self, num):
        """Печатаем топ num вакансий, на вход получает количество вакансий, которые надо отобразить"""
        self.dict_list.sort(reverse=True, key=lambda x: x.salary)
        print(f'ВЫВОЖУ ТОП-{num}')
        print('-' * 50)
        [print(_) for _ in self.dict_list[:num]]

    @load_and_save_file
    def delete_vacancy(self):
        """Удаляет элемент из JSON-file по ключу index, если удаление не требуется, то возвращает, что
        'Ничего не удалено'"""
        print(f"Вы действительно хотите удалить вакансию из файла {self.file_name}? \n")
        flag = True
        while flag:
            answer = input(f"Выберите 'Да' или 'Нет', а затем 'ENTER' для подтверждения:\n").title()
            if answer == 'Да':
                print(f"Введите номер вакансии для удаления:\n")
                user_del_index = int(input())
                for i, vacancy in enumerate(self.dict_list):
                    if vacancy.index == user_del_index:
                        self.dict_list.pop(i)
                        flag = False
            elif answer == 'Нет':
                flag = False
                return f"Ничего не удалено"
            else:
                print(f"Вы ввели неверный ответ. Попробуйте еще раз.")
