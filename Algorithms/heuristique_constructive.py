import random

"""
 On choisit un noeud de manière aléatoir pour remplir les clusters
"""
def heuristique_constructive(n, k):
    A = []

    for j in range(n):
        c = random.randint(1, k)
        A.append(c)

    return A