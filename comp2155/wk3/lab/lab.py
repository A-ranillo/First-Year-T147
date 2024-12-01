class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self.__name = value
        else:
            raise ValueError(f"{value} is not valid")

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):#feet
        if isinstance(value, int) and value >= 5:
            self.__age = value
        else:
            raise ValueError(f"{value} is not an integer or less than 5")

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):#inches
        if isinstance(value, int) and value >= 32:
            self.__height = value
        else:
            raise ValueError(f"{value} is not greater than 32 inches")

    def __str__(self):
        return f"{self.name} is {self.age} years old and is {self.height} inches tall"

    def run(self):
        return f"{self.name} is running"
    def jump(self):
        return f"{self.name} is jumping {self.height/4} inches high"
class SuperHero(Person):
    def __init__(self, name, age, height, superhero_name, super_power, planet):
        Person.__init__(self, name=name, age=age, height=height) #actual value
        super().__init__(name, age, height) #nickname
        self.superhero_name = superhero_name
        self.super_power = super_power
        self.planet = planet

    # overriding a method aka replacing the bahaviour of a method
    def jump(self):return self.superhero_name + super().jump().split(self.name)[1]

    def run(self, enemy):
        return f"{self.superhero_name} is running towards {enemy}"

    def fight(self, enemy):
        return f"{self.superhero_name} is fighting {enemy}"

    def __str__(self):
        return (f"{super().__str__()}. SuperHero Name is {self.superhero_name} "
                f"with the super power of {self.super_power} and "
                f"was born on {self.planet}")

batman = SuperHero("Bruce Wayne", 50, 70,
                   "Batman", "Wealth",
                   "Earth")

bruce = Person("Bruce Wayne", 50, 70)
print(batman.jump())
print(bruce.jump())
print(batman.run("Joker"))
print(batman)