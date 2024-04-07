import pytest
from data.hh import HH


def test_load_vacancies():
    """Функция проверки списка вакансий, что не равен нулю"""
    v = HH('file_worker')
    v.params['page'] = 19
    v.load_vacancies('Python-разработчик')
    assert len(v.vacancies) > 0