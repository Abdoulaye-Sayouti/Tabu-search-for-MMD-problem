import numpy as np
import random
from Util_Functions.array_in_ndarray import array_in_ndarray

"""
  - Pour cette méthode de voisinage, on choisit aléatoirement 
    deux noeuds dans deux clusters qu'on permute.

  - On doits générer NTS solutions différentes
"""
def swap_method(Ac, NTS, k):
    n = len(Ac)
    trials = []

    t = 0
    while t < NTS:
        trial = Ac.copy()
        node1 = random.randint(0, n - 1)
        node2 = random.randint(0, n - 1)

        while trial[node1] == trial[node2]:
            node1 = random.randint(0, n - 1)
            node2 = random.randint(0, n - 1)
        trial[node1] = trial[node1] + trial[node2]
        trial[node2] = trial[node1] - trial[node2]
        trial[node1] = trial[node1] - trial[node2]

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

