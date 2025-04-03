import unittest

# метод, начинающийся с test_ распознается как тест


class MathTest(unittest.TestCase):
    def test_addition(self):  # Этот метод будет запущен как тест
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):  # И этот тоже
        self.assertEqual(5 - 3, 2)

    def helper_method(self):  # А этот — нет (не начинается с test_)
        pass


"""
🔹 Методы setUp() и tearDown()
setUp() — выполняется перед каждым тестом (подготовка данных).

tearDown() — выполняется после каждого теста (очистка).
"""


def connect_to_database():
    pass


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.db = connect_to_database()  # Инициализация перед тестом

    def tearDown(self):
        self.db.close()  # Очистка после теста

    def test_query(self):
        result = self.db.query("SELECT 1")
        self.assertEqual(result, 1)


"""
🔹 Методы setUpClass() и tearDownClass()
setUpClass() — выполняется один раз перед всеми тестами в классе.

tearDownClass() — выполняется один раз после всех тестов.
"""


def initialize_expensive_resource():
    pass


class ExpensiveSetupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shared_resource = initialize_expensive_resource()  # 1 раз перед всеми тестами

    @classmethod
    def tearDownClass(cls):
        cls.shared_resource.release()  # 1 раз после всех тестов

    def test_feature1(self):
        self.assertTrue(self.shared_resource.is_ready())

    def test_feature2(self):
        self.assertEqual(self.shared_resource.get_value(), 42)


'''
Основные Assert-методы
TestCase предоставляет множество методов для проверок:

Метод	Проверяет	Пример
assertEqual(a, b)	a == b	self.assertEqual(2+2, 4)
assertNotEqual(a, b)	a != b	self.assertNotEqual(1, 2)
assertTrue(x)	bool(x) is True	self.assertTrue(5 < 10)
assertFalse(x)	bool(x) is False	self.assertFalse(10 < 5)
assertIs(a, b)	a is b	self.assertIs(x, None)
assertIsNone(x)	x is None	self.assertIsNone(result)
assertIn(a, b)	a in b	self.assertIn(3, [1, 2, 3])
assertRaises(Error, func, *args)	func(*args) вызывает ошибку	self.assertRaises(ValueError, int, "abc")
'''

'''Как запускать тесты?'''
'''Способ 1: Через unittest.main()'''

if __name__ == "__main__":
    unittest.main()  # Запуск всех тестов в файле

'''Способ 2: Через командную строку'''
# python -m unittest test_file.py  # Запуск конкретного файла
# python -m unittest discover     # Автопоиск всех тестов в проекте

''' Зачем вообще использовать TestCase?'''
# Структурированность — тесты организованы в классы.
# Гибкость — есть setUp/tearDown для подготовки данных.
# Много встроенных проверок (assertEqual, assertRaises и др.).
# Интеграция с CI/CD (например, GitHub Actions, Jenkins).

'''
Вывод
unittest.TestCase — это основа модульного тестирования в Python. Он позволяет:

- писать тесты в виде методов test_*,

- использовать setUp/tearDown для управления состоянием,

- применять разные assert-проверки.

Если пишешь тесты на Python — unittest.TestCase обязателен к изучению! 🚀
'''