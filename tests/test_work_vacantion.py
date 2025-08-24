import unittest
from src.work__vacantion import Work_vacantion

class TestWorkVaction (unittest.TestCase):
    """Тесты для проверки класса work_vacation"""
    def test_valid_pay_vac_with_none(self):
        # Тест: зарплата None должна стать 0
        vac = Work_vacantion('Тест',
                             None,
                             'Desc',
                             'Req',
                             'http://test.com')
        self.assertEqual(vac.pay_vac, 0)

    def test_valid_pay_vac_with_zero(self):
        # Тест: Зарплата 0 должна оставаться 0
        vac = Work_vacantion('Тест',
                             0,
                             'Desc',
                             'Req',
                             'http://test.com')
        self.assertEqual(vac.pay_vac, 0)

    def test_valid_pay_vac_with_positive(self):
        # Тест: положительная заработная плата сохраниться
        vac = Work_vacantion('Тест',
                             50000,
                             'Desc',
                             'Req',
                             'http://test.com')
        self.assertEqual(vac.pay_vac, 50000)

    def test_lt_operation(self):
        # Тест: сравнение vac1 < vac2
        vac1 = Work_vacantion('Тест 1',
                              30000,
                              'Desc',
                              'Req',
                              'http://test1.com')
        vac2 = Work_vacantion('Тест 2',
                              50000,
                              'Desc',
                              'Req',
                              'http://test2.com')
        self.assertTrue(vac1 < vac2)

    def test_gt_operation(self):
        # Тест: сравнение vac1 > vac2
        vac1 = Work_vacantion('Тест 1',
                              70000,
                              'Desc',
                              'Req',
                              'htttp://test1.com')
        vac2 = Work_vacantion('Тест 2',
                              50000,
                              'Desc',
                              'Req',
                              'http://test2.com')
        self.assertTrue(vac1 > vac2)

    def test_attributes_existence(self):
        # Тест: проверка существования атрибутов
        vac = Work_vacantion('Тест',
                             50000,
                             'Desc',
                             'Req',
                             'http://test.com')

        self.assertTrue(hasattr(vac, 'name_vac'))
        self.assertTrue(hasattr(vac, 'pay_vac'))
        self.assertTrue(hasattr(vac, 'description_vac'))
        self.assertTrue(hasattr(vac, 'requirements_vac'))
        self.assertTrue(hasattr(vac, 'url_vac'))

    def test_slots_restriction(self):
        # Тест: проверка ограничений __slots__
        vac = Work_vacantion('Тест',
                             50000,
                             'Desc',
                             'Req',
                             'http://test.com')
        with self.assertRaises(AttributeError):
            vac.non_existent_attr = 'Value'







