import unittest
import calk_11

'''
создадим класс «NewCalcTest», который будет наследоваться от «unittest.TestCase
'''
'''
    создадим для него набор тестов, например, добавим тест для функции корня с именем «test_sqrt».
    Этот тест будет проверять равенство с помощью «self.assertEqual»
    '''
class NewCalcTest(unittest.TestCase):
    '''
    проверим функцию «sqrt» из калькулятора, передав ей значение 4. В результате мы получим 2
    '''
    def test_sqrt(self):
        self.assertEqual(calk_11.sqrt(4), 2)
    '''
    добавим тест для возведения в степень, назовем его «test_pow». Для проверки воспользуемся «self.assertEqual» 
    и обратимся к функции «pow» из калькулятора. Проверим, что 3 в третьей степени дает 27
    '''
    def test_pow(self):
        self.assertEqual(calk_11.pow(3,3), 27)

'''
Ваш друг создал эти замечательные тесты и загрузил их на Git. Если бы мы действовали как раньше, нам пришлось бы 
добавлять каждый файл по отдельности. Теперь же нам нужно просто интегрировать новый блок тестов. 
Давайте импортируем и подключим его  в тест_сюите
'''
