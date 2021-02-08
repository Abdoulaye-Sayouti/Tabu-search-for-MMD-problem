import numpy as np
import random
from Util_Functions.array_in_ndarray import array_in_ndarray

"""
  - Pour cette méthode de voisinage, on choisit aléatoirement 
    un noeud dans un cluster qu'on transfert dans un autre cluster
    
  - On doits générer NTS solutions différentes
"""
def single_method(Ac, NTS, k):
    n = len(Ac)
    trials = []

    t = 0
    while t < NTS:
        trial = Ac.copy()
        node = random.randint(0, n - 1)
        c = random.randint(1, k)
        while c == trial[node]:
            c = random.randint(1, k)
        trial[node] = c
        temp = trial.copy()
        temp = np.array(temp)
        min_cluster = len(temp[temp == 1])
        for j in range(2, k + 1):
            if min_cluster > len(temp[temp == j]):
                min_cluster = len(temp[temp == j])
        if min_cluster > 1 and array_in_ndarray(trial, trials) == False and not np.array_equal(trial, Ac):
            trials.append(trial)
            t += 1
        else:
            continue

    return trials

