import unittest
from unittest.mock import patch, Mock
from requests.exceptions import RequestException
from src.job_search import Vacancys, HeadHunterAPI  # Замените your_module на имя вашего файла


class Test_Vacancys(unittest.TestCase):
    """Тесты для абстрактного класса Vacancys"""

    def test_abstract_method(self):
        """Тест, что абстрактный класс нельзя инстанциировать"""
        with self.assertRaises(TypeError):
            Vacancys()


class Test_HeadHunterAPI(unittest.TestCase):
    """Тесты для класса HeadHunterAPI"""

    def setUp(self):
        """Настройка перед каждым тестом"""
        self.hh_api = HeadHunterAPI()
        self.keyword = "Python"
        self.mock_response = {
            "items": [
                {
                    "name": "Python Developer",
                    "alternate_url": "https://hh.ru/vacancy/123",
                    "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
                    "snippet": {"requirement": "Опыт работы с Python", "responsibility": "Разработка"}
                }
            ]
        }

    def test_inheritance(self):
        """Тест, что HeadHunterAPI наследуется от Vacancys"""
        self.assertTrue(issubclass(HeadHunterAPI, Vacancys))

    @patch('src.job_search.requests.get')
    def test_successful_request(self, mock_get):
        """Тест успешного запроса к API"""
        # Мокируем ответ API
        mock_response = Mock()
        mock_response.json.return_value = self.mock_response
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Вызываем тестируемый метод
        result = self.hh_api.get_vacancies(self.keyword)

        # Проверяем, что запрос был выполнен с правильными параметрами
        mock_get.assert_called_once_with(
            "https://api.hh.ru/vacancies",
            params={
                "text": self.keyword,
                "per_page": 100,
                "page": 0

            }
        )

        # Проверяем, что возвращается правильный результат
        self.assertEqual(result, self.mock_response["items"])

    @patch('src.job_search.requests.get')  # Замените your_module на имя вашего файла
    def test_request_exception(self, mock_get):
        """Тест обработки исключения при запросе"""
        # Мокируем исключение при запросе
        mock_get.side_effect = RequestException("Network error")

        # Вызываем тестируемый метод
        result = self.hh_api.get_vacancies(self.keyword)

        # Проверяем, что возвращается пустой список при ошибке
        self.assertEqual(result, [])

    @patch('src.job_search.requests.get')  # Замените your_module на имя вашего файла
    def test_empty_response(self, mock_get):
        """Тест обработки пустого ответа от API"""
        # Мокируем пустой ответ
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Вызываем тестируемый метод
        result = self.hh_api.get_vacancies(self.keyword)

        # Проверяем, что возвращается пустой список
        self.assertEqual(result, [])

    @patch('src.job_search.requests.get')  # Замените your_module на имя вашего файла
    def test_no_items_in_response(self, mock_get):
        """Тест обработки ответа без ключа 'items'"""
        # Мокируем ответ без ключа 'items'
        mock_response = Mock()
        mock_response.json.return_value = {"other_data": "value"}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Вызываем тестируемый метод
        result = self.hh_api.get_vacancies(self.keyword)

        # Проверяем, что возвращается пустой список
        self.assertEqual(result, [])


