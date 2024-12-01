# print ("ready, set, fight!")

"""

player 1 :batman, health 25, attack 5
player 2: superman health = 20 attack = 4

batman attaccks upserman
    supermans health decreases to 15
super man attacks batman
    batmans health decrease.

player class
    3 attributes: name, health, atacck
        limit: 3 characters, health at least 20, attack 3-8.

game class
    a list of two players
    a method that starts fight
    a method that outlines what happens when 1 player
    hits/strikes/attack another player

"""


class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str):
            raise ValueError("this is not a string")
        if len(value) < 3:
            raise ValueError("Name is too short")
        self.__name=value

    @property
    def health(self) -> int:
        return self.__health
    @health.setter
    def health(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Health Value is not an int")
        elif value < 20:
            raise ValueError("Health is not lesser than 20")
        self.__health = value

    @property
    def attack(self) -> int:
        return self.__attack
    @attack.setter
    def attack(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("attack Value is not an int")
        elif value < 20:
            raise ValueError("attack is not lesser than 20")
        self.__attack = value

    def strike(self, power: int):
        self.__health -= power
    def has_health(self):
        return self.__health > 0

    def __str__(self):
        return f"Name={self.__name}, Health={self.__health}, Attack={self.__attack}"

class Game:
    def __init__(self, player1: Player, player2: Player) -> None:
        if isinstance(player, Player) and isinstance(player2, Player):
            self.__players = [Players]