from random import *

class Personnage:
    _nom: str
    _pv_max: int
    _pv_start_hero: list = [25, 50, 75, 100, 125, 150]
    _pv_start_enemy: range = range(5, 500)

    def __init__(self, nom: str) -> None:
        self._nom = nom
        if self.__class__.__name__ == "Hero":
            self._pv_max = self.initialisation_point_de_vie()
        elif self.__class__.__name__ == "Enemy": 
            self._pv_max = self.initialisation_point_de_vie()
        
    def initialisation_point_de_vie(self) -> int:
        if self.__class__.__name__ == "Hero": 
            return choice(self._pv_start_hero)
        elif self.__class__.__name__ == "Enemy":
            return randint(self._pv_start_enemy.start, self._pv_start_enemy.stop - 1)
