from data.vacancy import Vacancy
from tests.conftest import get_dictionary


def test_vacancy(get_dictionary):
    v = Vacancy(**get_dictionary)
    assert v.name == 'Стажер-разработчик Python'
    assert v.vacancy_url == 'https://hh.ru/vacancy/94354526'
    assert v.salary == round((100_000 + 150_000) / 2, 2)
    assert v.employer == 'Додо Пицца'
    assert v.city == 'Ростов-на-Дону'
    assert v.city_id == '76'
