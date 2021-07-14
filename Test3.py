liste=[]
for i in range(10):
    import random
    nbr=random.randint(3,17)
    liste.append(nbr)
print(liste)
liste2=[]
for nbr in liste:
    code=chr(nbr)
    liste2.append(code)
print("la 1ere liste est :",liste)
print("la 2e liste est :",liste2)