import random
import json
from enum import Enum
from packages.hero import Hero


class Position(Enum):
    VAINQUEUR = 0
    DEUXIEME = 1
    TROISIEME = 2


combattants = ["Ryan", "Mélina", "Marc", "Zeinab", "Anas",
               "Sophie", "Zackary", "Alex", "Axel", "Alain", "Tarek", "Yannis", "Marine", "Valérie", "Stéphanie", "Jérémy"]


def obtenir_medaille(position):
    if position == Position.VAINQUEUR:
        return "🥇"
    elif position == Position.DEUXIEME:
        return "🥈"
    elif position == Position.TROISIEME:
        return "🥉"
    else:
        return str(position + 1)


def repartir_combattants():
    combattants_melanges = random.sample(combattants, len(combattants))
    return [Hero(combattant) for combattant in combattants_melanges]


def executer_tournoi(num_combats):
    victoires = {}  # Dictionnaire pour stocker les victoires de chaque joueur
    for partie in range(num_combats):
        print(f"\n -- PARTIE N° {partie+1} -- \n")
        heros = repartir_combattants()
        numero_tour = 1
        while len(heros) > 1:
            print(f"Tour {numero_tour} :")
            numero_tour += 1
            nouveau_tour = []
            for i in range(0, len(heros), 2):
                heros1 = heros[i]
                heros2 = heros[i+1] if i+1 < len(heros) else None
                if heros2:
                    print(
                        f" + Combat : {heros1.get_nom()} VS {heros2.get_nom()}")
                    vainqueur = heros1.fight(heros2)
                    perdant = heros2 if vainqueur == heros1 else heros1
                    nouveau_tour.append(vainqueur)
                    # Mettre à jour les victoires du vainqueur
                    if vainqueur.get_nom() not in victoires:
                        victoires[vainqueur.get_nom()] = 0
                    victoires[vainqueur.get_nom()] += 1
                else:
                    nouveau_tour.append(heros1)
            heros = nouveau_tour
        print(f"\nVainqueur de la partie n° {partie+1}:")
        for i, heros in enumerate(heros[-3:]):
            position = Position(i)
            print(f"{obtenir_medaille(position)} : {heros.get_nom()}")

        # Calculer le grand vainqueur
    max_victoires = max(victoires.values())
    grands_gagnants = [heros for heros, num_victoires in victoires.items(
    ) if num_victoires == max_victoires]

    print("\nTableau final des médailles :")
    classement_victoires = sorted(
        victoires.items(), key=lambda x: x[1], reverse=True)

    for position, (heros, num_victoires) in enumerate(classement_victoires[:3]):
        position_medaille = Position(position)
        print(
            f"{obtenir_medaille(position_medaille)} : {heros} ({num_victoires} victoires)")

    if len(classement_victoires) > 3:
        print("Autres participants :")
        for position, (heros, num_victoires) in enumerate(classement_victoires[3:], start=4):
            print(f"{position}ème : {heros} ({num_victoires} victoires)")

    print(
        f"\nLe grand vainqueur est {', '.join(grands_gagnants)} avec {max_victoires} victoires !")
    print("Il obtient le plus grand trophée de tous les temps : 🏆")


executer_tournoi(100)
