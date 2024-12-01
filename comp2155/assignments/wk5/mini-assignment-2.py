class Vehicle:
    def __init__(self, colour, doors, gas_powered):
        self.__colour = colour
        self.__doors = doors
        self.__gas_powered = gas_powered

    @property
    def colour(self):
        return self.__colour
    @colour.setter
    def colour(self, name):
        if isinstance(name, str) and name in ["red", "purple", "green", "white", "grey"]:
            self.__colour = name
        else:
            raise ValueError(f"{name} is not a string or {name} is not one of the 5 colours")

    @property
    def doors(self):
        return self.__doors
    @doors.setter
    def doors(self, value):
        if isinstance(value, int) and value in [2, 4, 5]:
            self.__doors = value
        else:
            raise ValueError(f"{value} is not a integer or {value} is neither 2, 4, and 5")

    @property
    def gas_powered(self):
        return self.__gas_powered
    @gas_powered.setter
    def gas_powered(self, name):
        if isinstance(name, bool):
            self.__gas_powered = name
        else:
            raise ValueError(f"{name} is not a boolean")

    def __str__(self):
        return f"Vehicle colour: {self.__colour}, doors: {self.__doors}, gas_powered: {self.__gas_powered}"

    def is_eco_friendly(self):
        if self.__gas_powered is False and self.__doors >= 2:
            return True
        else:
            return False

class Truck:
    def __init__(self, colour, doors, gas_powered, seats, trunk_space):
        self.__seats = seats
        self.__trunk_space = trunk_space
        super().__init__(colour, doors, gas_powered)

    @property
    def seats(self):
        return self.__seats
    @seats.setter
    def seats(self, value):
        if isinstance(value, int) and value > 0:
            self.__seats = value
        else:
            raise ValueError(f"{value} is not whole number and greater than zero")

    @property
    def trunk_space(self):
        return self.__trunk_space
    @trunk_space.setter
    def trunk_space(self, value):
        if isinstance(value, int) and value > 0 and value != 0:
            self.__trunk_space = value
        else:
            raise ValueError(f"Trunk space is not integer and greater than zero")

    def __str__(self):
        return f"Vehicle colour: {super().__str__()}, seats: {self.__seats}, trunk_space: {self.__trunk_space}"

    def is_eco_friendly(self):
        if Vehicle.is_eco_friendly is True and self.__seats >= 2 and self.__trunk_space >= 1:
            return True
        else:
            return False
