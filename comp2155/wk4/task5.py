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

    def __str__(self):
        return(f"address:{self.address}, floors:{self.floor}, price:{self.price}")

class Apartment(Home):
    def __init__(self, address, floor, price, bathrooms, bedrooms):
        super().__init__(address, floor, price)
        self.__bathrooms = bathrooms
        self.__bedrooms = bedrooms

    @property
    def bathrooms(self):
        return self.__bathrooms
    @bathrooms.setter
    def bathrooms(self, var):
        self.__bathrooms = var

    @property
    def bedrooms(self):
        return self.__bedrooms

    @bedrooms.setter
    def bedrooms(self, var):
        self.__bedrooms = var

    def __str__(self):
        return (f"{super.__str__()}, bathrooms:{self.bathrooms}, bedrooms:{self.bedrooms}")