import random
from random import randint

def rollstat(min_num , max_num, rollamount):
    numbers = []
    for i in range(rollamount):
        numbers.append(random.randint(min_num, max_num))
    numbers.remove(min(numbers))
    return sum(numbers)

class NPC:
    def __init__(self, nom, race, espece, profession):
        self.Force = rollstat(1,6,4)
        self.Agility = rollstat(1,6,4)
        self.Constitution = rollstat(1,6,4)
        self.Intelligence = rollstat(1,6,4)
        self.Sagesse = rollstat(1,6,4)
        self.Charisme = rollstat(1,6,4)

        self.ClasseArmure = random.randint(1,12)
        self.Nom = nom
        self.Race = race
        self.Espece = espece
        self.PointDeVie = random.randint(1,20)
        self.Profession = profession

    def afficher_characteristiques(self):
        print(vars(self))

class Kobold(NPC):
    def attaque(self, cible):
        print("Vous attaquer:", cible.Nom)
        cible.subir_dommage(random.randint(1,6))

    def subir_dommage(self, dmg):
        self.PointDeVie -= dmg

class Hero(NPC):
    def attaque(self, cible):
        pouvoir = random.randint(1,20)
        if pouvoir == 20:
            d8 = random.randint(1,8)
            cible.subir_dommage(d8)
            print("Attaque critique !, vous attaquez", cible.Nom, "Pour:", d8)
        elif pouvoir == 1:
            print("Vous avez rate votre attaque !")
        elif 2 <= pouvoir <= 19:
            if pouvoir > cible.ClasseArmure:
                d6 = random.randint(1,6)
                cible.subir_dommage(d6)
                print("Vous attaquez", cible.Nom, "Pour:", d6, "PV")
            else:
                print("Votre attaque est inferieure a la classe d'armure de votre cible, vous manquez")

    def subir_dommage(self, dmg):
        self.PointDeVie -= dmg

Joe = Hero("Joe", "Elf", "Humain", "Guerrier")
Goblino = Kobold("Goblino", "Kobold", "Goblin", "Magicien")

print(Goblino.PointDeVie)
Joe.attaque(Goblino)
print(Goblino.PointDeVie)