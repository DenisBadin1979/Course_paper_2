import unittest
from unittest.mock import patch, Mock

from requests.exceptions import HTTPError, RequestException


from src.job_search import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        self.api = HeadHunterAPI()

    # Тест успешного подключения
    @patch('requests.get')
    def test_connect_api_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        result = self.api._Vacancys__connect_API()
        self.assertTrue(result)

    # Тест неуспешного подключения (ошибка сети)
    @patch('requests.get')
    def test_connect_api_network_error(self, mock_get):
        mock_get.side_effect = RequestException("Сервер не найден")

        with self.assertRaises(Exception) as context:
            self.api._Vacancys__connect_API()
        self.assertEqual(str(context.exception), "Сервер не найден")

    # Тест успешного получения вакансий
    @patch.object(HeadHunterAPI, '_Vacancys__connect_API')
    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get, mock_connect):
        mock_connect.return_value = True
        mock_response = Mock()
        mock_response.json.return_value = {"items": [{"id": "1", "name": "Python Developer"}]}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.api.get_vacancies("Python")
        self.assertEqual(result, [{"id": "1", "name": "Python Developer"}])

    # Тест ошибки при получении вакансий
    @patch.object(HeadHunterAPI, '_Vacancys__connect_API')
    @patch('requests.get')
    def test_get_vacancies_http_error(self, mock_get, mock_connect):
        mock_connect.return_value = True
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = HTTPError("HTTP Error")
        mock_get.return_value = mock_response

        with self.assertRaises(HTTPError):
            self.api.get_vacancies("Python")

    # Тест возврата 'error' при неудачном подключении
    @patch.object(HeadHunterAPI, '_Vacancys__connect_API')
    def test_get_vacancies_connection_failed(self, mock_connect):
        mock_connect.return_value = False
        result = self.api.get_vacancies("Python")
        self.assertEqual(result, 'error')