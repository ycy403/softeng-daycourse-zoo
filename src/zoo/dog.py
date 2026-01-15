# dog.py

from .animal import Animal


class dog(Animal):
    def __init__(self, name="doggy"):
        super().__init__(name, species="doggy")

    def sound(self):
        return "diu"

    def action(self):
        return "bite"