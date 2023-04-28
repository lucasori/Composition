from deque import Deque
from railway_enum import RailwayEnum


class Composition(Deque):

    def __int__(self, size_max):
        super.__init__(size_max)

    def number_of_wagons(self):
        return self.get_size()

    def total_weight(self):
        locomotive = self.filter_locomotive()

        return sum(i.get_weight() for i in locomotive) + self.total_load() + self.weight_passenger()

    def total_length(self):
        locomotive = self.filter_locomotive()
        passenger_car = self.filter_passenger_car()
        freight_car = self.filter_freight_car()

        return sum(i.get_length() for i in locomotive) + sum(i.get_length() for i in passenger_car) + sum(
            i.get_length() for i in freight_car)

    def total_load(self):

        freight_car = self.filter_freight_car()

        if len(freight_car) == 0:
            return 0

        return sum(i.get_load() for i in freight_car)

    def weight_passenger(self):

        passenger_car = self.filter_passenger_car()

        if len(passenger_car) == 0:
            return 0

        return sum(i.get_weight_passenger() for i in passenger_car)

    def total_passengers(self):

        passenger_car = self.filter_passenger_car()

        if len(passenger_car) == 0:
            return 0

        return sum(i.get_quantity_passenger() for i in passenger_car)

    def diagnostic_composition(self):

        locomotive = self.filter_locomotive()

        power = sum(i.get_power() for i in locomotive)
        tonne = self.total_weight()

        hpt = tonne * 1.05

        if hpt > power:

            remainder = hpt - power

            return f"\nNúmero de vagões na composição: {self.number_of_wagons()}\nFalta {round(remainder, 2)} para atingir a potência mínima aceitável"

        else:

            return f"\nNúmero de vagões na composição: {self.number_of_wagons()}" \
                   f"\nPotência está aceitável para composição {round(hpt, 2)}"

    def filter_locomotive(self):
        list_locomotive = []

        for i in self.get_data():
            if i is not None:
                if i.get_name() == RailwayEnum.LOCOMOTIVE:
                    list_locomotive.append(i)

        return list_locomotive

    def filter_freight_car(self):
        list_freight_car = []

        for i in self.get_data():
            if i is not None:
                if i.get_name() == RailwayEnum.FREIGHT_CAR:
                    list_freight_car.append(i)

        return list_freight_car

    def filter_passenger_car(self):
        list_passenger_car = []

        for i in self.get_data():
            if i is not None:
                if i.get_name() == RailwayEnum.PASSENGER_CAR:
                    list_passenger_car.append(i)

        return list_passenger_car
