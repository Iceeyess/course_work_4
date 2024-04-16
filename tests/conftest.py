import pytest


@pytest.fixture
def get_dictionary():
    return {'id': '94354526', 'premium': False, 'name': 'Стажер-разработчик Python', 'department': None,
            'has_test': False, 'response_letter_required': False,
            'area': {'id': '76', 'name': 'Ростов-на-Дону', 'url': 'https://api.hh.ru/areas/76'},
            'salary': {'from': 100000, 'to': 150000, 'currency': 'RUR', 'gross': False},
            'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
            'sort_point_distance': None, 'published_at': '2024-04-08T10:52:47+0300',
            'created_at': '2024-04-08T10:52:47+0300', 'archived': False,
            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=94354526',
            'show_logo_in_search': None, 'insider_interview': None,
            'url': 'https://api.hh.ru/vacancies/94354526?host=hh.ru',
            'alternate_url': 'https://hh.ru/vacancy/94354526',
            'relations': [],
            'employer': {'id': '2071925', 'name': 'Додо Пицца', 'url': 'https://api.hh.ru/employers/2071925',
                         'alternate_url': 'https://hh.ru/employer/2071925',
                         'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/524506.jpg',
                                       '240': 'https://img.hhcdn.ru/employer-logo/2539502.jpeg',
                                       '90': 'https://img.hhcdn.ru/employer-logo/2539501.jpeg'},
                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=2071925',
                         'accredited_it_employer': False, 'trusted': True}, 'snippet': {
            'requirement': 'Мы ищем <highlighttext>Python</highlighttext>-<highlighttext>разработчика</highlighttext>, уровнем от Junior и выше, желательно с опытом развития новых продуктов. Уверенные знания Python 3.8...',
            'responsibility': None}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'},
            'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
            'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
            'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'},
            'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False,
            'adv_context': None}
