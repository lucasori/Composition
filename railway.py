class Railway:

    def __init__(self, name, length, weight):
        self.__name = name
        self.__length = length
        self.__weight = weight

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_length(self):
        return self.__length + 2

