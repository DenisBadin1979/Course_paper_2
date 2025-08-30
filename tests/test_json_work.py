import unittest

from src.json_work import Json_file

# Ваш исходный код здесь (классы Json_work и Json_file)...


class TestJsonFileGetDict(unittest.TestCase):
    def setUp(self):
        self.json_file = Json_file()

    def test_regular_attributes(self):
        """Тест на получение обычных атрибутов"""

        class TestVacancy:
            def __init__(self):
                self.title = "Python Developer"
                self.salary = 100000
                self.description = "Develop cool stuff"

        vac = TestVacancy()
        result = self.json_file.get_dict(vac)

        self.assertEqual(result["title"], "Python Developer")
        self.assertEqual(result["salary"], 100000)
        self.assertEqual(result["description"], "Develop cool stuff")
        self.assertEqual(len(result), 3)

    def test_protected_attributes(self):
        """Тест на получение защищенных атрибутов"""

        class TestVacancy:
            def __init__(self):
                self._protected_attr = "protected"
                self.title = "Python Developer"

        vac = TestVacancy()
        result = self.json_file.get_dict(vac)

        self.assertIn("_protected_attr", result)
        self.assertEqual(result["_protected_attr"], "protected")
        self.assertEqual(result["title"], "Python Developer")

    def test_private_attributes_excluded(self):
        """Тест на исключение приватных атрибутов"""

        class TestVacancy:
            def __init__(self):
                self.__private_attr = "private"
                self.title = "Python Developer"

        vac = TestVacancy()
        result = self.json_file.get_dict(vac)

        # Приватные атрибуты не должны попасть в результат
        self.assertNotIn("__private_attr", result)
        self.assertIn("title", result)
        self.assertEqual(result["title"], "Python Developer")

    def test_methods_excluded(self):
        """Тест на исключение методов"""

        class TestVacancy:
            def __init__(self):
                self.title = "Python Developer"

            def some_method(self):
                return "method result"

        vac = TestVacancy()
        result = self.json_file.get_dict(vac)

        self.assertNotIn("some_method", result)
        self.assertIn("title", result)
        self.assertEqual(result["title"], "Python Developer")

    def test_callable_attributes_excluded(self):
        """Тест на исключение callable-атрибутов"""

        class TestVacancy:
            def __init__(self):
                self.title = "Python Developer"
                self.lambda_attr = lambda x: x + 1

        vac = TestVacancy()
        result = self.json_file.get_dict(vac)

        self.assertNotIn("lambda_attr", result)
        self.assertIn("title", result)
        self.assertEqual(result["title"], "Python Developer")

    def test_properties_included(self):
        """Тест на включение свойств (properties)"""

        class TestVacancy:
            def __init__(self):
                self._title = "Python Developer"

            @property
            def title(self):
                return self._title

            @property
            def upper_title(self):
                return self._title.upper()

        vac = TestVacancy()
        result = self.json_file.get_dict(vac)

        # Properties должны быть включены, так как они не callable
        self.assertIn("title", result)
        self.assertIn("upper_title", result)
        self.assertEqual(result["title"], "Python Developer")
        self.assertEqual(result["upper_title"], "PYTHON DEVELOPER")

    def test_class_attributes_excluded(self):
        """Тест на исключение атрибутов класса"""

        class TestVacancy:
            class_attr = "class value"

            def __init__(self):
                self.instance_attr = "instance value"

        vac = TestVacancy()
        result = self.json_file.get_dict(vac)

        # Атрибуты класса не должны попасть в результат
        self.assertNotIn("class_atttr", result)
        self.assertIn("instance_attr", result)
        self.assertEqual(result["instance_attr"], "instance value")
