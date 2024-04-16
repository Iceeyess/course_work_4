import pytest
from src.vacancy import Vacancy
from src.json_management import JSONManagement
import os
from tests.test_hh import test_load_vacancies


s = os.path.join('data', 'test.json')


@pytest.fixture
def get_vacancies_list():
    attr_ = test_load_vacancies()
    attr_.file_worker = os.path.join('/home/dima/PycharmProjects/course_work_4/course_work_4/data/test.json')
    return attr_


def test_sort_by_salary(get_vacancies_list):
    json_man = JSONManagement(get_vacancies_list)
    assert isinstance(json_man.dict_list[0], Vacancy)
