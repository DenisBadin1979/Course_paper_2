from abc import ABC, abstractmethod
import json

from work__vacantion import Work_vacantion


class Json_work(ABC):
    """ Абстрактный класс для работы с файлами"""
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
        self.list_vac = []
        # self.vac_dict = {}


    def read_json(self):
        """Метод получения данных из файла"""
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            a = json.load(file)
        return a


    def add_json(self, data_vac):
        """метод получения добавления данных в файл"""
        # list_vac = self.read_json()
        dict_vac = data_vac.to_dict
        if dict_vac not in self.list_vac:
            self.list_vac.append(dict_vac)
        with open(self.__file_name, 'w', encoding='utf-8') as file:
            json.dump(self.list_vac, file, ensure_ascii=False, indent=4)



    def delete_json(self):
        """метод удаления данных из файла."""
        a = []
        with open (self.__file_name, 'w', encoding='utf-8') as file:
            json.dump(a, file, ensure_ascii=False, indent=4)



if __name__ == '__main__':

    jas1 = Json_file('output.json')


    vac = Work_vacantion('Тест',
                         None,
                         'Desc',
                         'Req',
                         'http://test.com')

    vac2 = Work_vacantion('Тест 2',
                         5000,
                         'Desc 3',
                         'Req 2',
                         'http://test2.com')
    vac3 = Work_vacantion('Тест 2',
                          70000,
                          'Desc 2',
                          'Req 2',
                          'http://test2.com')
    jas1.add_json(vac)
    jas1.add_json(vac2)
    jas1.add_json(vac3)









