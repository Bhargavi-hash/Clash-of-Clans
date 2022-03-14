from colorama import Fore, Back, Style

class Fire:
    def __init__(self):
        self.tile = Back.GREEN + "🔥" + Style.RESET_ALL
        self._damagePower = 100

class tile:
    def __init__(self):
        self.tile = Back.GREEN + "  " + Style.RESET_ALL

class barbarian:
    def __init__(self):
        self.tile = Back.GREEN + "🥷" + " " + Style.RESET_ALL
        self._health = 100
        self._damagePower = 20
        self._speed  = 1    # One tile per motion

class king(barbarian):
    def __init__(self):
        self.row = 10
        self.col = 14
        self.tile = Back.GREEN + "👑" + Style.RESET_ALL
        self.shield = 5
        self._health = 100
        self._damagePower = 25
        self._axeAOE = 5   # Effects all buildings in the area of radius 10
        self._speed = 1     # Two tiles per motion

class Hut:
    def __init__(self):
        self.tile = Back.GREEN + "🏠" + Style.RESET_ALL
        self._health = 100
        # self._damageRate = 25

class colony(Hut):
    def __init__(self):
        self.tile = Back.GREEN + "🏘️" + " " + Style.RESET_ALL
        self._health = 100
        self._shield = 2
        self.shieldTile = Back.GREEN + "🛡" + " " + Style.RESET_ALL
        # self._damageRate = 10

class townHall(Hut):
    def __init__(self):
        self.tile = Back.GREEN + "🏛️" + " " +Style.RESET_ALL
        self.shieldTile = Back.GREEN + "🛡" + " " + Style.RESET_ALL
        self._health = 300
        self._shield = 4

class wall:
    def __init__(self):
        self.tile = Back.GREEN + "🧱" + Style.RESET_ALL
        self._health = 100
        
        # self._damageRate = 20

class bomb:
    def __init__(self):
        self.tile = Back.GREEN + "💣" + Style.RESET_ALL
        self._damageRange = 10
        self._damagePower = 30

class cannon_wall:
    def __init__(self):
        self.tile = Back.GREEN + "⬛" + Style.RESET_ALL


