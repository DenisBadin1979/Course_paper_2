from abc import ABC, abstractmethod
from typing import Any

import requests


class Vacancys(ABC):
    """Абстрактный класс для работы с API вакансий."""

    @abstractmethod
    def __connect_API(self) -> None:
        """Создан метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> None:
        """Получает вакансии по ключевому слову.
        :param keyword: Ключевое слово для поиска вакансий
        :return: Список вакансий
        """
        pass


class HeadHunterAPI(Vacancys):
    """Класс для работы с API HeadHunter."""

    def __init__(self) -> None:
        self.__base_url = "https://api.hh.ru/vacancies"

    def _Vacancys__connect_API(self) -> int | str:
        try:
            return requests.get(self.__base_url).status_code == 200
        except:
            raise Exception("Сервер не найден")

    def get_vacancies(self, keyword: str) -> Any:
        """
        Получает вакансии с hh.ru по ключевому слову.:param keyword: Ключевое слово для поиска
        :return: Список вакансий в формате JSON
        """
        params = {"text": keyword, "per_page": 100, "page": 0}  # Количество результатов на странице  # Номер страницы

        if self._Vacancys__connect_API():
            response = requests.get(self.__base_url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("items", [])
        else:
            return "error"
