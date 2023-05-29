#!/usr/bin/env python3

from packages.personnage import Personnage
from packages.experience import Experience
import random

class Hero(Personnage):
    """
    Hero au grand coeur
    Cet être est venu d'une lointaine contrée pour éradiquer tous être qui chercherait à le nuire.
    """
    _experience: int
    _niveau: int
    _exp_table: list
    _force: int
    
    def __init__(self, nom: str) -> None:
        super().__init__(nom)
        self._experience = 0
        self._niveau = 1
        self._exp_table = Experience.creation_table_experience(100, 1000000, 60)
        
    def fight(self, other_hero):
        """Fait combattre ce héros avec un autre héros. 
        Le héros avec le plus grand niveau gagne. 
        En cas d'égalité, le vainqueur est choisi au hasard."""
        
        if self._niveau > other_hero._niveau:
            return self
        elif self._niveau < other_hero._niveau:
            return other_hero
        else:
            # Si les deux héros ont le même niveau, on choisit le vainqueur au hasard
            return random.choice([self, other_hero])
        
        
    def afficher_table_experience(self):
        """Affiche ma table d'expérience au complet
        """
        print("\n")
        for i, exp in enumerate(self._exp_table):
            print(f" Niveau {i+1} :\t {exp}")
        print("\n")
    
    def afficher_experience_actuel(self):
        print(f" ☑ - Tu as {self._experience} points d'expérience.")
    
    def cheatcode_set_experience(self, experience: int):
        self._experience = experience
        for i in range(1, len(self._exp_table)):
            if self._exp_table[i] > experience:
                self._niveau = i
                break

    def afficher_exp_niveau_suivant(self)-> str :
        niveau_actuel = self._niveau
        if niveau_actuel >= len(self._exp_table):
            return None
        exp_niveau_suivant = self._exp_table[niveau_actuel]
        exp_restante = exp_niveau_suivant - self._experience
        return print(f"\n ☑ - Expérience requise pour passer au niveau suivant : {str(max(0, exp_restante))}")

    def get_nom(self):
        return self._nom