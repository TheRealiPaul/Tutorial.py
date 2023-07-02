liste2 = [[24,5,9,6],[55,61,32]]


liste3 = [123,"groupe", 45,56,"eleve",70]
print(liste3)
for a in liste3:
    if str(a).isnumeric():
        print("resultat :", a * 2)

liste4 = [["salon",5,3],["chambre1",5,3],["chambre2",5,3]]
print(liste4)
for i in liste4:
    print(i,"surface :", liste4[2])
liste5 = []   
for x in range(3):
    sousliste = []
    sousliste.append(input("nom piece : "))
    sousliste.append(float(input("dimension : ")))
    sousliste.append(float(input("dimension 2: ")))
    liste5.append(sousliste)
print(liste5)
    
