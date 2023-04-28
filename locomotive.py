from railway import Railway


class Locomotive(Railway):

    def __init__(self, name, length, weight, power):
        super().__init__(name, length, weight)
        self.__power = power

    def get_power(self):
        return self.__power

    def __str__(self):
        return f"Comprimento: {self.get_length()} Peso: {self.get_weight()} Potência: {self.get_power()}"
