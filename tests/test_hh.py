import pytest
from src.hh import HH
from src.links_constants import HH_API_CITIES

def test_load_vacancies():
    """Функция проверки списка вакансий, что не равен нулю"""
    params = {'text': '', 'page': 0, 'per_page': 20}
    hh_API_vacancies = 'https://api.hh.ru/vacancies'
    HEADERS = {'User-Agent': 'HH-User-Agent'}
    v = HH('file_worker', hh_API_vacancies, HEADERS, params)
    v.params['page'] = 19
    v.load_vacancies('Python-разработчик', 20)
    assert len(v.vacancies) > 0


def test_get_city_id() -> None:
    city_list = ['Москва', 'Санкт-Петербург', 'Казань', 'Уфа']
    city_list_id = [1, 2, 88, 99]
    for _ in range(len(city_list)):
        id_ = HH.get_city_id(HH_API_CITIES, city_list[_])
        assert id_ == city_list_id[_]