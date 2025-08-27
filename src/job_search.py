from abc import ABC, abstractmethod

import requests


class Vacancys (ABC):
    """Абстрактный класс для работы с API вакансий."""

    @abstractmethod
    def __connect_API (self):
        """Создан метод для подключения к API"""
        pass

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
        self.__base_url = "https://api.hh.ru/vacancies"

    def _Vacancys__connect_API(self):
        try:
            return requests.get(self.__base_url).status_code == 200
        except:
            raise Exception ("Сервер не найден")


    def get_vacancies(self, keyword: str) -> list:
        """
        Получает вакансии с hh.ru по ключевому слову.:param keyword: Ключевое слово для поиска
        :return: Список вакансий в формате JSON
        """
        params = {
            "text": keyword,
            "per_page": 100,  # Количество результатов на странице
            "page": 0       # Номер страницы
        }

        if self._Vacancys__connect_API():
            response = requests.get(self.__base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("items", [])
        else:
            return 'error'







if __name__ == '__main__':

    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies("водитель")


    if hh_vacancies:
        print(f"Найдено вакансий: {len(hh_vacancies)}")
        print(type(hh_vacancies))
        print(hh_vacancies)
    else:
        print("Вакансии не найдены.")


