
import random

class ant:

    def __init__(self, name):
        self.name = name


class fireant(ant):

    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
