randomListe = []
nouvelleListe = []
i = 0
#-------------------------------------------- Programmes ---------------------------------------------------#
#importation du module random
from random import randint
#décompte et affichage des deux listes randomListe et nouvelleListe
while i < 10:
    r = randint(0,255)
    randomListe.append(r)
    nouvelleListe.append(chr(r))
    i += 1
#end while
print(randomListe)
print(nouvelleListe)
