class Home:
    def __init__(self, address, floor, price):
        self.__address = address
        self.__floor = floor
        self.__price = price

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, var):
        self.__address = var


    @property
    def floor(self):
        return self.__floor
    @floor.setter
    def floor(self, var):
        self.__floor = var

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, var):
        self.__price = var