from railway_enum import RailwayEnum


class Except(Exception):
    pass


class Deque:

    def __init__(self, size_max):
        self.__size_max = size_max
        self.__data = [None] * size_max
        self.__front = 0
        self.__top = 0
        self.__current_position = 0
        self.__size = 0

    def __str__(self):
        if self.is_empty():
            raise Except("Fila vazia")
        else:
            list_temp = []
            str_size = 0
            self.rewind()

            while str_size < self.__size:
                list_temp.append(self.next())
                str_size += 1

            return str(list_temp)

    def get_size(self):
        return self.__size

    def rewind(self):
        self.__current_position = self.__front

    def next(self):
        if self.is_empty():
            return None
        else:
            element = self.__data[self.__current_position]
            self.__current_position += 1

            if self.__current_position == self.__size_max:
                self.__current_position = 0

            return element

    def getVC(self):
        if self.is_empty():
            raise Except("Vetor vazio")

        return str(self.__data)

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__size_max

    def add_first(self, element):
        if self.is_full():
            raise Except("Fila cheia")

        if self.is_empty():
            self.__data[self.__front] = element
        else:
            self.__front -= 1

            if self.__front == -1:
                self.__front = self.__size_max - 1
                self.__data[self.__front] = element
            else:
                self.__data[self.__front] = element

        self.__size += 1

    def add_last(self, element):
        if self.is_full():
            raise Except("fila cheia")

        if self.is_empty():
            self.__data[self.__top] = element
            self.__size += 1
        else:
            self.__top += 1

            if self.__top == self.__size_max:
                self.__top = 0

            self.__data[self.__top] = element

            self.__size += 1

    def delete_first(self):
        if self.is_empty():
            raise Except("Fila vazia")

        first_element = self.__data[self.__front]

        self.__data[self.__front] = None
        self.__size -= 1
        self.__front += 1

        if self.__front == self.__size_max:
            self.__front = 0

        return first_element

    def delete_last(self):
        if self.is_empty():
            raise Except("Fila vazia")

        last_element = self.__data[self.__top]

        self.__data[self.__top] = None
        self.__size -= 1
        self.__top -= 1

        if self.__top == -1:
            self.__top = self.__size_max - 1

        return last_element

    def get_data(self):
        return self.__data

    def print_data(self):
        for i in self.get_data():
            if i is not None:
                print(i)

        return " "
