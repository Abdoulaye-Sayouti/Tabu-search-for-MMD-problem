import random
import numpy as np
from Util_Functions.array_in_ndarray import array_in_ndarray


"""
  - Pour cette méthode de voisinage, pour chaque noeud on choisit 
    un nombre aléatoire "prop" compris entre 0 et 1. Si (prob > p)
    alors on transfert le noeud dans un autre cluster aléatoirement.
    Si (prob <= p), le noeud reste dans le mêm cluster.

  - On doits générer NTS solutions différentes
"""

def threshold_method(Ac, NTS, p, k):
    n = len(Ac)
    trials = []

    t = 0
    while t < NTS:
        trial = Ac.copy()
        for j in range(n):
            s = [m for m in range(n) if trial[m] == trial[j]]
            if len(s) > 2:
                prob = random.random()
                if prob > p:
                    l = random.randint(1, k)
                    while l == trial[j]:
                        l = random.randint(1, k)
                    trial[j] = l

        if array_in_ndarray(trial, trials) == False and not np.array_equal(trial, Ac):
            trials.append(trial)
            t += 1

    return trials

