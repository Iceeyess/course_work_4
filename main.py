from src.hh import HH
from src.vacancy import Vacancy
import os
from src.json_management import JSONManagement
# Константы:
from src.links_constants import HH_API_CITIES, hh_API_vacancies, file_name, HEADERS


def data_insertion():
    """Функция для взаимодействия консоли и пользователя, для поискового запроса из hh.ru"""

    path_ = os.path.join('data', file_name)
    print(f"Уважаемый пользователь, представляем программу запроса свежих вакансий через API по {hh_API_vacancies}")
    print("Введите поисковые критерии:")

    vacancy = input(f"Введите интересующую Вас вакансию: ").title()

    # Объект класса city, вводим город, пока не найдем city_id по 'https://api.hh.ru/areas' это константа
    city_id = HH.get_city_id(HH_API_CITIES, input("Введите город, в котором хотите найти вакансию: ").replace(
        ' ', '').title())
    while not city_id:
        city = input(f"Извините, условие строгое. Вы должны ввести город, в котором хотите найти вакансии:\n").replace(
            ' ', '').title()
        city_id = HH.get_city_id(HH_API_CITIES, city)

    salary = int(input("Введите сумму ожидаемой заработной платы.\n"))
    vacancies_per_pages = int(input(f"Введите количество вакансий на 1 страницу.\n"))
    pages = int(input(f"Введите количество страниц для вывода.\n"))

    top_n_vacancies = int(input("Введите top-N вакансий по критериям отбора. Данные должны быть целыми числами.\n"))
    does_show_salary_only = input(
        "Необходимо ли показывать только вакансии с указанной заработной платой? Введите 'Да' или 'Нет'.\n").title()
    does_show_salary_only_dict = {'Да': True, 'Нет': False}
    is_only_included_salary = does_show_salary_only_dict[does_show_salary_only]
    params = {'text': '', 'page': 0, 'per_page': vacancies_per_pages, 'area': city_id,
              'only_with_salary': is_only_included_salary, 'salary': salary}

    h = HH(path_, hh_API_vacancies, HEADERS, params)
    h.load_vacancies(vacancy, pages)
    json_m = JSONManagement(h)
    json_m.sort_by_salary()
    # json_m.get_top(top_n_vacancies)


if __name__ == '__main__':
    data_insertion()
