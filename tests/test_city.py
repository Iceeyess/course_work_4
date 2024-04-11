import pytest
from src.city import City
from src.links_constants import hh_API_cities


def test_get_city_id() -> None:
    city_list = ['Москва', 'Санкт-Петербург', 'Казань', 'Уфа']
    city_list_id = [1, 2, 88, 99]
    for _ in range(len(city_list)):
        id_ = City(hh_API_cities, city_list[_]).get_city_id()
        assert id_ == city_list_id[_]
