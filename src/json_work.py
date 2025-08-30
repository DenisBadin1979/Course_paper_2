import json
from abc import ABC, abstractmethod
from typing import Any


class JsonWork(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def read_json(self) -> None:
        """Метод получения данных из файла"""
        pass

    @abstractmethod
    def add_json(self, data_vac: Any) -> None:
        """метод получения добавления данных в файл"""
        pass

    @abstractmethod
    def delete_json(self) -> None:
        """метод удаления данных из файла."""
        pass


class JsonFile(JsonWork):
    def __init__(self, file_name: str = "data/po.json") -> None:
        self.__file_name = file_name
        self.list_vac = []

    def read_json(self) -> Any:
        """Метод получения данных из файла"""
        with open(self.__file_name, "r", encoding="utf-8") as file:
            a = json.load(file)
        return a

    def get_dict(self, vac: Any) -> dict:
        """Объект класса вакансии переводит в словарь"""
        obj_dict = {
            attr: getattr(vac, attr) for attr in dir(vac) if not attr.startswith("__") and not callable(getattr(vac, attr))
        }
        return obj_dict

    def add_json(self, data_vac: Any) -> Any:
        """метод получения добавления данных в файл"""
        # list_vac = self.read_json()
        dict_vac = self.get_dict(data_vac)

        if dict_vac not in self.list_vac:
            self.list_vac.append(dict_vac)
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(self.list_vac, file, ensure_ascii=False, indent=4)

    def delete_json(self) -> Any:
        """метод удаления данных из файла."""
        a = []
        with open(self.__file_name, "w", encoding="utf-8") as file:
            json.dump(a, file, ensure_ascii=False, indent=4)
