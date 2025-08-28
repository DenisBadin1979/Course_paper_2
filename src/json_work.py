from abc import ABC, abstractmethod

class Json_work(ABC):
    """ Абстрактный класс для работы с файлам"""
    @abstractmethod
    def read_json(self):
        """Метод получения данных из файла"""
        pass

    @abstractmethod
    def add_json(self):
        """метод получения добавления данных в файл"""
        pass

    @abstractmethod
    def delete_json (self):
        """метод удаления данных из файла."""
        pass

class Json_file (Json_work):
    def __init__(self, file_name = 'data/po.json'):
        self.__file_name = file_name
        self.vac_list = []
        # self.vac_dict = {}


    def read_json(self):
        """Метод получения данных из файла"""
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            a = file.read()
        return a


    def add_json(self):
        """метод получения добавления данных в файл"""
        pass


    def delete_json(self):
        """метод удаления данных из файла."""
        pass



if __name__ == '__main__':

    jas1 = Json_file()
    print(jas1.read_json())



