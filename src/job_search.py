from abc import ABC, abstractmethod

import requests


class Vacancys (ABC):
    """Абстрактный класс для работы с API вакансий."""
    @abstractmethod
    def get_vacancies(self, keyword):
        """Получает вакансии по ключевому слову.
                :param keyword: Ключевое слово для поиска вакансий
                :return: Список вакансий
                """
        pass

class HeadHunterAPI(Vacancys):
    """Класс для работы с API HeadHunter."""
    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []



    def get_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1



hh_api = HeadHunterAPI()

hh_vacancies = hh_api.get_vacancies("Бухгалтерия")

if hh_vacancies:
    print(f"Найдено вакансий: {len(hh_vacancies)}")
    print(hh_vacancies[0])
else:
    print("Вакансии не найдены.")