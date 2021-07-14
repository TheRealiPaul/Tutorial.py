#Écrire une fonction qui prend une liste de nombres et retourne la somme et la moyenne des nombres de la liste. Tester votre fonction. 

def sommeETmoyenne (liste):
    for i in range(len(liste)):
        somme = 0
        somme = somme + nb
        moyenne = somme / len(liste)
    return somme, moyenne

liste = []

X = int(input("Veuillez saisir le nombre de nombres que vous allez saisir : "))
for i in range(X):
    nb = int(input("Entrez les nombres : "))
    liste.append(nb)
    print(liste)

print(sommeETmoyenne(liste))
