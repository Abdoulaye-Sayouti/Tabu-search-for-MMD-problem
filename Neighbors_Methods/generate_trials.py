from Neighbors_Methods.single_method import single_method
from Neighbors_Methods.swap_method import swap_method
from Neighbors_Methods.threshold_method import threshold_method

"""
On fait appel à la méthode de voisinage désirer pour générer les solutions
"""
def generate_trials(methode, Ac, NTS, p, k):
    if methode == 'single':
        trials = single_method(Ac, NTS, k)
    elif methode == 'threshold':
        trials = threshold_method(Ac, NTS, p, k)
    else:
        trials = swap_method(Ac, NTS, k)

    return trials
