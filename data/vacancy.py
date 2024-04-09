from data.hh import HH, Parser


class VacancyWrongTypeException(Exception):
    """Класс для отображения ошибки, если сравниваются разные типы данных"""

    def __init__(self, *args) -> None:
        """Инициализируем типы данных"""
        self.type_1, self.type_2 = args


    def __str__(self) -> None:
        """Для отображения"""
        return (f"Вы пытаетесь сравнить данные {self.type_1} с {self.type_2}.\n"
                f"Так нельзя, используйте только тип данных класса Vacancy")


class Vacancy(HH):
    """Для вакансий определения таких полей, как:
    название вакансии, ссылка на вакансию, зарплата, работодатель на hh.ru, город"""
    __slots__ = ['name', 'vacancy_url', '__salary', 'employer', 'city', 'city_id']

    def __init__(self, *args, **kwargs) -> None:
        self.name = kwargs['name']
        self.vacancy_url = kwargs['alternate_url']
        # Валидация данных о зарплате
        self.__salary = self.get_salary_validator(**kwargs['salary'] if kwargs['salary'] else {})
        self.employer = kwargs['employer']['name']
        self.city = kwargs['area']['name']
        self.city_id = kwargs['area']['id']

    @staticmethod
    def get_salary_validator(**data: (dict, None)) -> (int, float):
        """Функция принимает набор данных, который может содержать 4 варианта зарплаты: не указана, указано только 'от',
        указано только 'до', указано 'от' и 'до'. Возвращает тип данных int or float, в зависимости от вводных данных"""
        if not data:
            return 0
        elif data['from'] and data['to']:
            # если вилка указана от и до, то берем среднее значение
            return round((data['from'] + data['to']) / 2, 2)
        elif data['from'] and not data['to']:
            # если не указана до, то просто берем значение от.
            return data['from']
        elif not data['from'] and data['to']:
            # если не указана до, то просто берем значение до.
            return data['to']

    @property
    def salary(self) -> (int, float):
        """Свойство атрибута зарплата"""
        return self.__salary

    def __le__(self, other):
        """Магический метод для сравнения ЭК между собой с помощью вакансий"""
        if type(other) is type(self):
            return self.salary <= other.salary
        raise VacancyWrongTypeException(type(self).__name__, type(other).__name__)


h = HH('inquiry')
h.load_vacancies('Python-developer')
with open(h.file_worker, mode='w', encoding='utf-8') as f:
    for i, x in enumerate(h.vacancies, 1):
        f.write(str(i) + str(x))
        # f.write(str(i) + str(Vacancy(**x)))
