import logging
from unittest import TestCase

class Runner:
    def __init__(self, name, speed=5):
        self.distance = 0
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
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

class RunnerTest(TestCase):
    def test_walk(self):
        try:
            Runner('Вося', -10)
            logging.info('"test_walk" completed successfully')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")

    def test_run(self):
        try:
            Runner(10, 5)
            logging.info('"test_run" completed successfully')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")

first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)

t = Tournament(101, first, second, third)
print(t.start())
logging.basicConfig(filename='runner_tests.log',
                    filemode='w',
                    level=logging.INFO,
                    encoding='utf-8',
                    format='%(levelname)s: %(message)s')
INFO: {f'"test_walk" completed successfully'}
WARNING: {f'Неверная скорость для Runner: invalid li'}
WARNING: {f'Неверный тип данных для объекта Runner: "int" object cannot be interpreted as an index'}
