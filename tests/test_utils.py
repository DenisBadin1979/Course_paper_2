import json
import os
import tempfile
import unittest

from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, sort_vacancies


class TestVacancyFunctions(unittest.TestCase):

    def setUp(self):
        # Создаем временные данные для тестирования
        self.vacancies_list = [
            {"name": "Python Developer", "pay_vac": 100000, "description_vac": "Разработка на Python и Django"},
            {"name": "Data Scientist", "pay_vac": 150000, "description_vac": "Анализ данных и машинное обучение"},
            {"name": "Web Developer", "pay_vac": 80000, "description_vac": "Разработка веб-приложений"},
            {"name": "DevOps Engineer", "pay_vac": 120000, "description_vac": "Настройка инфраструктуры и CI/CD"},
        ]

    def test_filter_vacancies_with_matching_words(self):
        """Тест фильтрации с совпадающими ключевыми словами"""
        filter_words = ["Python", "Django"]
        result = filter_vacancies(self.vacancies_list, filter_words)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Python Developer")

    def test_filter_vacancies_without_matching_words(self):
        """Тест фильтрации без совпадающих ключевых слов"""
        filter_words = ["Java", "Spring"]
        result = filter_vacancies(self.vacancies_list, filter_words)

        self.assertEqual(len(result), 0)

    def test_filter_vacancies_case_insensitive(self):
        """Тест фильтрации без учета регистра"""
        filter_words = ["python", "django"]
        result = filter_vacancies(self.vacancies_list, filter_words)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Python Developer")

    def test_sort_vacancies(self):
        """Тест сортировки вакансий по зарплате"""
        result = sort_vacancies(self.vacancies_list)

        # Проверяем порядок вакансий (от меньшей к большей зарплате)
        self.assertEqual(result[0]["pay_vac"], 80000)
        self.assertEqual(result[1]["pay_vac"], 100000)
        self.assertEqual(result[2]["pay_vac"], 120000)
        self.assertEqual(result[3]["pay_vac"], 150000)

    def test_get_top_vacancies(self):
        """Тест получения топ N вакансий"""
        result = get_top_vacancies(self.vacancies_list, 2)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Python Developer")
        self.assertEqual(result[1]["name"], "Data Scientist")

    def test_get_top_vacancies_more_than_available(self):
        """Тест получения топ N вакансий, когда N больше общего количества"""
        result = get_top_vacancies(self.vacancies_list, 10)

        self.assertEqual(len(result), 4)

    def test_get_vacancies_by_salary_valid_range(self):
        """Тест фильтрации по диапазону зарплат"""
        salary_range = "90000-130000"
        result = get_vacancies_by_salary(self.vacancies_list, salary_range)

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["name"], "Python Developer")
        self.assertEqual(result[1]["name"], "DevOps Engineer")

    def test_get_vacancies_by_salary_no_matches(self):
        """Тест фильтрации по диапазону зарплат без совпадений"""
        salary_range = "200000-300000"
        result = get_vacancies_by_salary(self.vacancies_list, salary_range)

        self.assertEqual(len(result), 0)

    def test_get_vacancies_by_salary_invalid_range(self):
        """Тест фильтрации по неверному формату диапазона"""
        salary_range = "invalid-range"

        with self.assertRaises(ValueError):
            get_vacancies_by_salary(self.vacancies_list, salary_range)

    def test_get_vacancies_by_salary_single_value(self):
        """Тест фильтрации по одному значению зарплаты"""
        salary_range = "100000"
        result = get_vacancies_by_salary(self.vacancies_list, salary_range)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Python Developer")


class TestUserInteraction(unittest.TestCase):

    def setUp(self):
        # Создаем временный файл с вакансиями
        self.temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json")
        self.vacancies_data = [
            {"name": "Python Developer", "pay_vac": 100000, "description_vac": "Разработка на Python и Django"},
            {"name": "Data Scientist", "pay_vac": 150000, "description_vac": "Анализ данных и машинное обучение"},
        ]
        json.dump(self.vacancies_data, self.temp_file)
        self.temp_file.close()

    def tearDown(self):
        # Удаляем временный файл
        os.unlink(self.temp_file.name)

    def test_user_interaction_integration(self):
        """Интеграционный тест user_interaction (требует мокирования ввода)"""
        # Этот тест требует мокирования функций input и проверки вывода
        # Для простоты можно пропустить или реализовать с помощью unittest.mock
        pass


if __name__ == "__main__":
    unittest.main()
