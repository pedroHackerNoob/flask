import random


class Sorteo:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def iniciarSorteo(self):

        res = random.randint(1, 100)
        print("xdd: ",res)

        if res == self.num1:
            return True
        if  res == self.num2:
            return True

        else:
            return False