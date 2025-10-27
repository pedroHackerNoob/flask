import random


class Sorteo:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def iniciarSorteo(self):

        res = random.randint(1, 100)
        # res = self.num1
        print("resultado final: ",res)

        if res == self.num1 or res == self.num2:
            return True

        else:
            return False