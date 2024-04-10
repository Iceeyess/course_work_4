import pytest
from src.hh import HH


def test_load_vacancies():
    """Функция проверки списка вакансий, что не равен нулю"""
    params = {'text': '', 'page': 0, 'per_page': 20}
    hh_API_vacancies = 'https://api.hh.ru/vacancies'
    HEADERS = {'User-Agent': 'HH-User-Agent'}
    v = HH('file_worker', hh_API_vacancies, HEADERS, params)
    v.params['page'] = 19
    v.load_vacancies('Python-разработчик', 20)
    assert len(v.vacancies) > 0