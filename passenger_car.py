from railway import Railway


class PassengerCar(Railway):

    def __init__(self, name, length, weight, quantity_passengers):
        super().__init__(name, length, weight)
        self.__quantity_passengers = quantity_passengers

    def get_quantity_passenger(self):
        return self.__quantity_passengers

    def get_weight_passenger(self):
        return self.get_weight() + self.get_quantity_passenger()

    def __str__(self):
        return f"Comprimento: {self.get_length()} Peso: {self.get_weight()} " \
               f"Quantidade passageiros: {self.__quantity_passengers}"


