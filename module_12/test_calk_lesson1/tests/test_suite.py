'''Прежде всего, необходимо импортировать сам модуль «unittest» и импортировать наши файлы с тестами.
В нашем случае это файлы '''

import unittest
from lessons0.module_12.test_calk_lesson1.tests import test_new_calc, test_calk

# calkST = unittest.TestSuite()

'''
Мы получили объект «test_suite». Однако нужно добавить в него наши тесты. Это делается достаточно просто: 
«calcST.addTest(unittest.makeSuite(test_calc.CalcTest))» (Рис. 5). Здесь используется функция «unittest.makeSuite»,
после чего мы обращаемся к нашему файлу с тестами и подгружаем нужный класс с тестами. 
Ранее этот метод использовался часто, но сейчас он устаревает.
'''
# calkST.addTest(unittest.makeSuite(test_calk.CalkTest))  # ф «makeSuite» вычеркнута, в 3.13 она перестанет работать

'''
Существует более современный метод, который позволит нам решить эту проблему (Рис. 7). Он также добавляет тесты, 
но уже с помощью метода «TestLoader» и функции «loadTestsFromTestCase». Далее указываем путь к нашему «TestCase», 
то есть модуль, откуда мы его берём, и название класса.
'''

# calkST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calk.CalkTest))

'''
Затем мы можем настроить запуск тестов. Можно создать отдельный файл «runner», но также можно сделать это прямо здесь: 
мы обращаемся к «unittest» и используем «TextTestRunner»V
'''
# runner = unittest.TextTestRunner()

'''
Мы также можем запустить тесты прямо здесь. Необходимо указать, по какому «TestSuite» будет производиться запуск. 
В нашем случае это «calcST». Если мы запустим тесты, то увидим, что все они пройдены, и всё работает прекрасно
'''

# runner.run(calkST)

'''
Существует также параметр «verbosity». В нашем случае он позволяет изменять уровень детализации вывода тестов. 
Например, как видно, показываются конкретные тесты, которые мы прошли. При установке данного параметра на уровень 2 
он выводит необходимые нам сведения о том, какие конкретно тесты были пройдены
'''
# runner = unittest.TextTestRunner(verbosity=2)
# runner.run(calkST)

# добавление новых тестов другого разработчика
# import test_new_calc
# calkST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.NewCalcTest))



calkST = unittest.TestSuite()
calkST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calk.CalkTest))
calkST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.NewCalcTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(calkST)