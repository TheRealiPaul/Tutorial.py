# FONCTION
def fonction(liste):
    # POUR ITEMS DE LA LISTE
    compteur = 0
    for texte in liste:
        # IF the string length …
        if len(texte)>=2:
            if texte[0] == texte[len(texte)-1]:
                # COMPTEUR = COMPTEUR + 1
                compteur = compteur + 1 
    return compteur

print(fonction( ['abc', 'xyz', 'aba', '1221']))
