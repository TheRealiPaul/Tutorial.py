maListe = []
somme = 0
l = 0
#--------------------------- Programmes ------------------------------------#

nbNote = int(input("Veuillez saisir le nombre d'élève : "))

while l < nbNote:
    note = float(input("Veuillez saisir une note entre 0 et 100 : "))
    if note >= 0 and note <= 100:
        maListe.append(note)
else:
    print("Erreur!!!")
l = l + 1

print(maListe)

for note in maListe:
    if note >= 60 and note <= 100:
        print("Les meilleurs note de la classe : ",note)

somme = sum(maListe)
moyenne = somme/len(maListe)
print("La moyenne du groupe est : ", moyenne)

print("La meilleur note du groupe : ", max(maListe))

m = max(maListe)
i = 0
for note in maListe:
    if note == m:
        i += 1

print("Nombre d'élève ayant eu la meilleur note : ",i)
