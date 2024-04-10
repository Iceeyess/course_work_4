from src.hh import HH
from src.vacancy import Vacancy
from src.city import City
import os


def data_insertion():
    """Функция для взаимодействия консоли и пользователя, для поискового запроса из hh.ru"""

    file_name = 'inquiry.json'
    path_ = os.path.join('data', file_name)
    hh_API_vacancies = 'https://api.hh.ru/vacancies'
    hh_API_ciies = 'https://api.hh.ru/areas'
    print(f"Уважаемый пользователь, представляем программу запроса свежих вакансий через API у hh.ru")
    print("Введите поисковые критерии:")

    # Объект класса city
    city_id = City(hh_API_ciies, input("Введите город, в котором хотите найти вакансию.\n").replace(
        ' ', '')).get_city_id()
    while not city_id:
        city = input(f"Извините, условие строгое. Вы должны ввести город, в котором хотите найти вакансии:\n").replace(' ', '')
        city_id = City(hh_API_ciies, city).get_city_id()

    salary = int(input(
        "Введите сумму ожидаемой заработной платы.\n"))

    vacancies_per_pages = int(input(f"Введите количество вакансий на 1 страницу.\n"))
    pages = int(input(f"Введите количество страниц для вывода.\n"))

    HEADERS = {'User-Agent': 'HH-User-Agent'}

    top_n_vacancies = int(input("Введите top-N вакансий по критериям отбора. Данные должны быть целыми числами.\n"))
    does_show_salary_only = input(
        "Необходимо ли показывать только вакансии с указанной заработной платой? Введите 'Да' или 'Нет'.\n")
    does_show_salary_only_dict = {'Да': True, 'Нет': False}
    is_only_included_salary = does_show_salary_only_dict[does_show_salary_only]
    params = {'text': '', 'page': 0, 'per_page': vacancies_per_pages, 'area': city_id,
              'only_with_salary': is_only_included_salary, 'salary': salary}

    h = HH(path_, hh_API_vacancies, HEADERS, params)
    h.load_vacancies('Python-developer', pages)
    with open(h.file_worker, mode='w', encoding='utf-8') as f:
        for i, x in enumerate(h.vacancies, 1):
            f.write(str(i) + str(x))
            # f.write(str(i) + str(Vacancy(**x)))


if __name__ == '__main__':
    data_insertion()
