import unittest
import json
import os

from src.json_work import Json_file
from src.work__vacantion import Work_vacantion

class TestJsonFile(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом"""
        self.test_file = 'test.json'
        self.json_file = Json_file(self.test_file)
        # Создаем тестовые данные
        self.test_data = [
            {"name_vac": "Test1", "pay_vac": "1000", "description_vac": "Desc1",
             "requirements_vac": "Req1", "url_vac": "http://test1.com"},
            {"name_vac": "Test2", "pay_vac": "2000", "description_vac": "Desc2",
             "requirements_vac": "Req2", "url_vac": "http://test2.com"}
        ]

    def tearDown(self):
        """Очистка после каждого теста"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_json_existing_file(self):
        """Тест чтения существующего JSON файла"""
        # Создаем тестовый файл с данными
        with open(self.test_file, 'w', encoding='utf-8') as f:
            json.dump(self.test_data, f, ensure_ascii=False, indent=4)

        # Читаем и проверяем данные
        result = self.json_file.read_json()
        self.assertEqual(result, self.test_data)

    def test_read_json_nonexistent_file(self):
        """Тест чтения несуществующего файла"""
        # Убедимся, что файла нет
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        # Должен вернуть пустой список или вызвать исключение
        # В зависимости от реализации, может потребоваться адаптация
        with self.assertRaises(FileNotFoundError):
            self.json_file.read_json()

    def test_add_json_new_vacancy(self):
        """Тест добавления новой вакансии"""
        # Создаем мок-объект вакансии
        mock_vacancy = Work_vacantion(
            "Test1", "1000", "Desc1", "Req1", "http://test1.com"
        )

        # Добавляем вакансию
        self.json_file.add_json(mock_vacancy)

        # Проверяем, что файл создан и содержит данные
        with open(self.test_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name_vac"], "Test1")

    def test_add_json_duplicate_vacancy(self):
        """Тест добавления дублирующей вакансии"""
        # Создаем мок-объекты вакансий
        mock_vacancy1 = Work_vacantion(
            "Test1", "1000", "Desc1", "Req1", "http://test1.com"
        )
        mock_vacancy2 = Work_vacantion(
            "Test1", "1000", "Desc1", "Req1", "http://test1.com"  # Та же вакансия
        )

        # Добавляем вакансии
        self.json_file.add_json(mock_vacancy1)
        self.json_file.add_json(mock_vacancy2)  # Не должна добавиться

        # Проверяем, что в файле только одна запись
        with open(self.test_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.assertEqual(len(data), 1)

    def test_delete_json(self):
        """Тест удаления всех данных из файла"""
        # Сначала добавляем данные
        mock_vacancy = Work_vacantion(
            "Test1", "1000", "Desc1", "Req1", "http://test1.com"
        )
        self.json_file.add_json(mock_vacancy)

        # Убеждаемся, что данные есть
        with open(self.test_file, 'r', encoding='utf-8') as f:
            data_before = json.load(f)
        self.assertEqual(len(data_before), 1)

        # Удаляем данные
        self.json_file.delete_json()

        # Проверяем, что файл пустой
        with open(self.test_file, 'r', encoding='utf-8') as f:
            data_after = json.load(f)
        self.assertEqual(data_after, [])

    def test_init_default_filename(self):
        """Тест инициализации с именем файла по умолчанию"""
        json_file = Json_file()
        self.assertEqual(json_file._Json_file__file_name, 'data/po.json')

    def test_init_custom_filename(self):
        """Тест инициализации с пользовательским именем файла"""
        custom_file = 'custom.json'
        json_file = Json_file(custom_file)
        self.assertEqual(json_file._Json_file__file_name, custom_file)