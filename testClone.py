def clone():
    liste = [1, 2, 3, 4]
    liste1 = liste * 3
    return liste1


def clone2(liste):
    liste1 = liste + liste + liste
    return liste1


print("clone: ", clone())

print("clone2: ", clone2([1, 2, 3, 4]))

# I notice that it is the same result
