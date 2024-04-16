from src.hh import HH


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
    __slots__ = ['name', 'alternate_url', '__salary', 'employer', 'city', 'city_id']
    index = 0

    def __init__(self, *args, **kwargs) -> None:
        # Если индекс приходит от class json_management, то оставляем старый, в противном случае, генерируем новый.
        if kwargs.get('index'):
            self.index = kwargs['index']
        else:
            self.index += 1
            Vacancy.index = self.index

        self.name = kwargs['name']
        self.alternate_url = kwargs['alternate_url']
        # Валидация данных о зарплате, если приходит объект HH, то он несёт, или словарь или False, если пришел
        # тип данных int, float, то пришел объект vacancy. Очень много условий, поэтому применил тернарный оператор
        if type(kwargs['salary']) is dict or type(kwargs['salary']) is False:
            self.__salary = round(self.get_salary_validator(**kwargs['salary'] if kwargs['salary'] else {}), 2)
        else:
            self.__salary = kwargs['salary'] if kwargs['salary'] else 0
        self.employer = kwargs['employer']['name'] if type(kwargs['employer']) is dict else kwargs['employer']
        self.city = kwargs['area']['name'] if kwargs.get('area') else kwargs['city']
        self.city_id = kwargs['area']['id'] if kwargs.get('area') else kwargs['city_id']

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

    def __str__(self):
        tuple_ = (f"Порядковый номер выгруженной вакансии - {self.index}", f"Название вакансии - "
        f"{self.name}", f"Ссылка на вакансию - {self.alternate_url}", f"Заработная плата - {self.salary}",
        f"Работодатель - {self.employer}", f"Город - {self.city}")
        glue_string = str()
        for str_ in tuple_:
            glue_string = glue_string + str_ + '\n'
        glue_string += '-' * 50
        return glue_string

    def __repr__(self):
        return f"Должность: {self.name}, зарплата: {self.salary}"

    def __gt__(self, other):
        try:
            return self.salary > other.salary
        except TypeError:
            raise VacancyWrongTypeException(self, other)

    def __lt__(self, other):
        try:
            return self.salary < other.salary
        except TypeError:
            raise VacancyWrongTypeException(self, other)

    def __eq__(self, other):
        try:
            return self.salary == other.salary
        except TypeError:
            raise VacancyWrongTypeException(self, other)

    @property
    def get_self_dict(self):
        """Определил метод-свойство для метода save_to_file в JSONManagement
        из-за экономии памяти и ускорения класса. Метод возвращает словарь атрибутов класса, т.к. __dict__
        мы не можем использовать"""
        return {'index': self.index, 'name': self.name, 'alternate_url': self.alternate_url, 'salary': self.salary,
                'employer': self.employer,
                'city': self.city, 'city_id': self.city_id}
