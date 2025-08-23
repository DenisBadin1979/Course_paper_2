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
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, keyword: str) -> list:
        """
        Получает вакансии с hh.ru по ключевому слову.

        :param keyword: Ключевое слово для поиска
        :return: Список вакансий в формате JSON
        """
        params = {
            "text": keyword,
            "per_page": 100,  # Количество результатов на странице
            "page": 0       # Номер страницы

        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Проверка на ошибки HTTP
            data = response.json()
            return data.get("items", [])
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к API hh.ru: {e}")
            return []







if __name__ == '__main__':

    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies("Python")

    if hh_vacancies:
        print(f"Найдено вакансий: {len(hh_vacancies)}")
        print(hh_vacancies[0])
    else:
        print("Вакансии не найдены.")