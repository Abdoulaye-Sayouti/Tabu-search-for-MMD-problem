import numpy as np

"""
 Une fonction qui permet de facilement vérifier si une solution 
 se trouve dans la liste tabou
"""
def array_in_ndarray(array, ndarray):
    find = False
    for j in ndarray:
        if np.array_equal(j, array):
            find = True
            break
    return find
