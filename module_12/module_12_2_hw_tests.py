# тестируемый код


class Runner:
    '''
    Изменения в классе Runner:
    1. Появился атрибут speed для определения скорости бегуна.
    2. Метод __eq__ для сравнивания имён бегунов.
    3. Переопределены методы run и walk, теперь изменение дистанции
    зависит от скорости.
    '''


    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

#  Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):  # сравнение имен бегунов
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    '''
    Класс Tournament представляет собой класс соревнований, где есть
    дистанция, которую нужно пробежать и список участников. Также
    присутствует метод start, который реализует логику бега по
    предложенной дистанции.
    '''
    def __init__(self, distance, *participants):   # турнир, *участники
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


'''
Задание:
Напишите класс TournamentTest, наследованный от TestCase. В нём
реализуйте следующие методы:
setUpClass - метод, где создаётся атрибут класса all_results. Это
словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:

1. Бегун по имени Усэйн, со скоростью 10.
2. Бегун по имени Андрей, со скоростью 9.
3. Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.
Так же методы тестирования забегов, в которых создаётся
объект Tournament на дистанцию 90. У объекта
класса Tournament запускается метод start, который возвращает
словарь в переменную all_results. В конце вызывается
метод assertTrue, в котором сравниваются последний объект

из all_results (брать по наибольшему ключу) и предполагаемое имя
последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в
объект Tournament соблюсти):

1. Усэйн и Ник
2. Андрей и Ник
3. Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена
логическая ошибка. В результате его работы бегун с меньшей скоростью
может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными
тестами.

Пример результата выполнения тестов:
Вывод на консоль:
{1: Усэйн, 2: Ник}
{1: Андрей, 2: Ник}
{1: Андрей, 2: Усэйн, 3: Ник}
Ran 3 tests in 0.001s
OK

Примечания:
1. Ваш код может отличаться от строгой последовательности
описанной в задании. Главное - схожая логика работы тестов и
наличие всех перечисленных переопределённых методов из
класса TestCase.
'''
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = Runner('Усейн', 10)
        self.second = Runner('Андрей', 9)
        self.third = Runner('Ник', 5)

    # @classmethod
    # def tearDownClass(cls):
    #     for result in cls.all_results.values():
    #         print(result)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            formatted_result = {k: str(v) for k, v in result.items()} # Преобразуем объекты Runner в строки (имена)
            print(formatted_result)



# Тест забегов

# Тест забега Усейна и Ника
    def test_1_3(self): # Усейн и Ник
        tournament = Tournament(90, self.first, self.third)
        result = tournament.start()
        self.all_results['Тест забега Усейна и Ника'] = result
        last_ = max(result.keys())
        self.assertTrue(result[last_] == 'Ник')

# Тест забега Андрея и Ника
    def test_2_3(self):  # Андрей и Ник
        tournament = Tournament(90, self.second, self.third)
        result = tournament.start()
        self.all_results['Тест забега Андрея и Ника'] = result
        # проверка, что Ник последний
        last_ = max(result.keys())
        self.assertTrue(result[last_] == 'Ник')

# Тест забега Усейна, Андрея и Ника
    def test_1_2_3(self):  # Усейн, Андрей и Ник
        tournament = Tournament(90, self.first, self.second, self.third)
        result = tournament.start()
        self.all_results['Тест забега Усейна, Андрея и Ника'] = result
        # проверка, что Ник последний
        last_ = max(result.keys())
        self.assertTrue(result[last_] == 'Ник')

if __name__ == '__main__':
    unittest.main()
