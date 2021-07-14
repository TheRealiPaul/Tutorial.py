"""
def clone():
    liste = [1,2,3,4]
    liste1 = liste * 2
    return  liste1

print(clone())
"""

def clone2(liste):
    liste1 = liste + liste
    return(liste1)

print(clone2([1,2,3,4,5,6]))