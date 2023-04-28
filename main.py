from passenger_car import PassengerCar
from freight_car import FreightCar
from locomotive import Locomotive
from composition import Composition
from railway_enum import RailwayEnum
import random

list_weight_passenger = [50, 50, 42, 50, 49, 42, 32, 42, 33, 39, 41, 47, 41, 44, 50, 32, 30, 42, 38, 49, 42, 50, 42,
                         33, 39, 41, 47, 41, 44, 36]
list_weight_freight = [98, 100, 84, 92, 82, 86, 90, 89, 99, 100, 100, 91, 88, 100, 92, 98, 89, 84, 92, 100, 86, 90, 89, 99,
                       92, 89, 91, 88, 100, 92]

locomotive1 = Locomotive(RailwayEnum.LOCOMOTIVE, 1.74, 150, 2000)
locomotive2 = Locomotive(RailwayEnum.LOCOMOTIVE, 1.74, 200, 1000)
locomotive3 = Locomotive(RailwayEnum.LOCOMOTIVE, 1.74, 150, 2000)
locomotive4 = Locomotive(RailwayEnum.LOCOMOTIVE, 1.74, 150, 3000)

if __name__ == '__main__':
    composition1 = Composition(100)
    composition2 = Composition(100)

    for i in range(16):
        passenger = random.randint(1, 30)

        passenger_car = PassengerCar(RailwayEnum.PASSENGER_CAR, 15, list_weight_passenger[i], passenger)
        composition1.add_first(passenger_car)
        composition2.add_first(passenger_car)

    for i in range(20):
        passenger = random.randint(1, 30)

        passenger_car = PassengerCar(RailwayEnum.PASSENGER_CAR, 15, list_weight_passenger[i], passenger)
        composition1.add_last(passenger_car)
        composition2.add_last(passenger_car)

    for i in range(30):
        freight_car = FreightCar(RailwayEnum.FREIGHT_CAR, 18, list_weight_freight[i])
        composition1.add_first(freight_car)
        composition2.add_first(freight_car)

    for i in range(30):
        freight_car = FreightCar(RailwayEnum.FREIGHT_CAR, 18, list_weight_freight[i])
        composition1.add_last(freight_car)
        composition2.add_last(freight_car)

    composition1.add_last(locomotive1)
    composition1.add_last(locomotive2)
    composition1.add_last(locomotive3)
    composition1.add_last(locomotive4)

    composition2.delete_last()
    composition2.delete_first()

    print("-------------Composição 1 potência aceitável-------------")
    print(composition1.print_data())
    print(f"Comprimento total composição 1: {composition1.total_length()}")
    print(f"Peso total composição 1: {composition1.total_weight()}")
    print(f"Total número de passageiros: {composition1.total_passengers()}")
    print(f"Total de carga: {composition1.total_load()}")
    print(composition1.diagnostic_composition())
    print("----------------------------------------------------------")
    print(" ")
    print("-----------Composição 2 potência não aceitável------------")
    print(composition2.print_data())
    print(f"Comprimento total composição 2: {composition2.total_length()}")
    print(f"Peso total composição 2: {composition2.total_weight()}")
    print(f"Total número de passageiros: {composition2.total_passengers()}")
    print(f"Total de carga: {composition2.total_load()}")
    print(composition2.diagnostic_composition())
    print("-----------------------------------------------------------")
