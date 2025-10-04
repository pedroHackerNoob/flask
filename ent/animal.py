class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @classmethod
    def get(cls):
        animals = [
            cls("aguila","blanco"),
            cls("cristian","azul"),
            cls("perro","rojo"),
            cls("gato","gris")
        ]
        return animals