#
# import rt_with_exceptions
# import unittest
#
# class RunnerTest(unittest.TestCase):
#     def test_walk(self):
#         # w = rt_with_exceptions.Runner.walk('Linas')
#         self.assertEqual(rt_with_exceptions.Runner.walk(50))
#
import unittest

# Пример определения класса Runner
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner("Test Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

# Запуск тестов
if __name__ == '__main__':
    unittest.main()