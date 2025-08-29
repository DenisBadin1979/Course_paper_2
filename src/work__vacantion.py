from time import process_time


class Work_vacantion:
    """ Класс для работы с вакансиями."""
    __slots__ = ('name_vac', 'pay_vac', 'description_vac', 'requirements_vac', 'url_vac')
    def __init__(self, name_vac, pay_vac, description_vac, requirements_vac, url_vac):
        self.name_vac = name_vac
        self.pay_vac = self.__valid_pay_vac(pay_vac)
        self.description_vac = description_vac
        self.requirements_vac = requirements_vac
        self.url_vac = url_vac

    def __valid_pay_vac (self, pay_vac):
        """Валидация данных по заработной плате """
        if pay_vac == 0 or pay_vac == None:
            return 0
        else:
            return pay_vac


    def __lt__(self, other):
        """"Метод сравнения данных по заработной плате self < other"""
        return self.pay_vac < other.pay_vac

    def __gt__(self, other):
        """"Метод сравнения данных по заработной плате self > other"""
        return self.pay_vac > other.pay_vac

    def to_dict(self):
        return {"name_vac" : self.name_vac,
                    "pay_vac" : self.pay_vac ,
                    "description_vac" : self.description_vac,
                    "requirements_vac" : self.requirements_vac,
                    "url_vac" : self.url_vac}

    # @property
    # def upper_name(self):
    #     return self.name_vac.upper()

if __name__ == "__main__":
    vac = Work_vacantion('Тест',
                         5000,
                         'Описание',
                         'Требования',
                         'http://test.com')

    obj_dict = {attr: getattr(vac, attr) for attr in dir(vac)
                if not attr.startswith('__') and not callable(getattr(vac, attr))}

    print(obj_dict)  # {'name': 'test', 'upper_name': 'TEST'}