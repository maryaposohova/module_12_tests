import calk_11
import unittest
import random

# # проверка функции калькулятора
# print('проверка функции калькулятора')
#
#
# def test_add():
#     if calk_11.add(1, 2) == 3:
#         print('test add(a, b) is "Ok"')
#     else:
#         print('test add(a, b) is fail')
#
#
# test_add()
#
#
# def test_sub():
#     if calk_11.sub(5, 2) == 3:
#         print('test sub(a, b) is "Ok"')
#     else:
#         print('test sub(a, b) is fail')
#
#
# test_sub()
#
#
# def test_mul():
#     if calk_11.mul(5, 2) == 10:
#         print('test mul(a, b) is "Ok"')
#     else:
#         print('test mul(a, b) is fail')
#
#
# test_mul()
#
#
# def test_div():
#     if calk_11.div(15, 5) == 3:
#         print('test div(a, b) is "Ok"')
#     else:
#         print('test div(a, b) is fail')
#
#
# test_div()
#
#
# # проверка с помощью юниттеста
# print()
# print('проверка с помощью юниттеста')


# class CalkTest(unittest.TestCase):   # assertEqual - это проверка на равенство
#     def test_add(self):
#         """
#         тест для функции "+" калькулятора
#         """
#         self.assertEqual(calk_11.add(1, 2), 3)
#
#     def test_sub(self):
#         """
#         тест для функции "-" калькулятора
#         """
#         self.assertEqual(calk_11.sub(5, 3), 2)
#
#     def test_mul(self):
#         """
#         тест для функции "*" калькулятора
#         """
#         self.assertEqual(calk_11.mul(5, 3), 15)
#
#     def test_div(self):
#         """
#         тест для функции "/" калькулятора
#         """
#         self.assertEqual(calk_11.div(15, 3), 5)
#
#
# if __name__ == '__main__':
#     unittest.main()


# урок Методы Юнит-тестирования, def setUp()


class CalkTest(unittest.TestCase):   # assertEqual - это проверка на равенство
    # def setUp(self):
    #     print('setup')
    #
    # @classmethod
    # def setUpClass(cls):  # запуск перед тестами
    #     print('Megasetup')
    @unittest.skip('Не нравится')
    def test_add(self):
        """
        тест для функции "+" калькулятора
        """

        self.assertEqual(calk_11.add(1, 2), 3)

    # @unittest.skipIf(random.randint(0, 2), 'Не повезло')
    @unittest.skipIf(False, 'Не повезло')
    def test_sub(self):
        """
        тест для функции "-" калькулятора
        """
        self.assertEqual(calk_11.sub(5, 3), 2)

    def test_mul(self):
        """
        тест для функции "*" калькулятора
        """
        self.assertEqual(calk_11.mul(5, 3), 15)

    def test_div(self):
        """
        тест для функции "/" калькулятора
        """
        self.assertEqual(calk_11.div(15, 3), 5)

    def test_test(self):
        self.assertTrue(True)

    def test_test2(self):
        self.assertFalse((False))

    def t_(self):
        self.assertIn('a', 'abc')

    # @classmethod
    # def tearDown(self): # запуск после тестов
    #     print('teardown')


if __name__ == '__main__':
    unittest.main()
