from railway import Railway


class FreightCar(Railway):

    def __init__(self, name, length, weight):
        super().__init__(name, length, weight)

    def get_load(self):
        return self.get_weight() * 0.75

    def __str__(self):
        return f"Comprimento: {self.get_length()} Peso: {self.get_weight()} Carga: {self.get_load()}"
