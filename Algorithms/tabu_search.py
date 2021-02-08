import random
import numpy as np
from Util_Functions.array_in_ndarray import array_in_ndarray
from Neighbors_Methods.generate_trials import generate_trials
from Algorithms.objective_function import compute_objective_function


def tabu_search(A, Z, NTS, MTLS, ITMAX, p, k, dist_matrix):

    # Les trois méthodes de voisinage utilisées
    NeiMethods = ['single', 'threshold', 'swap']

    # La taille de la liste taboue des méthodes de voisinage
    # 2 car nous avons  3 méthodes
    NTLS = 2

    #
    # Etape 1 (Initialisation)
    #

    # Nombre d'instances
    n = len(A)

    # Initialisation de la meilleure solution
    # avec la solution obtenue par heuristique constructive
    Ab = A.copy()
    Ac = A.copy()
    Zb = Z

    # Taill actuel de la liste tabou
    TLL = 0

    # Listes contenant les solutions tabou et
    tabu_list = []
    nei_tabu_list = []

    # Itérateur permettant de changer la méthode voisinage
    # après 10 sitérations sans nouvelle solution
    count = 0

    #
    # Etape 2
    #

    # Initialiisatiion de la méthode de voisinage à utiliser
    method = random.randint(0, 2)

    # Boucle for jusqu'au nombre maximum d'itération
    for m in range(ITMAX):

        # Changer de méthode de voisinage après 10 itérations sans succssès
        if count == 10:
            count = 0

            if len(nei_tabu_list) == NTLS:
                del nei_tabu_list[0]

            nei_tabu_list.append(method)

            method = random.randint(0, 2)
            while method in nei_tabu_list:
                method = random.randint(0, 2)

        #
        # Etape 3
        #

        # Générer les solutions voisine et calculer leurs coûts
        trials = generate_trials(NeiMethods[method], Ac, NTS, p, k)
        Ztrials = []
        for j in range(len(trials)):
            Ztrials.append(compute_objective_function(trials[j], k, dist_matrix)[0])

        #
        # Etape 4
        #

        # Trier les solutions par ordre croissant des coûts
        Ztrials = np.array(Ztrials)
        indexes = np.argsort(Ztrials)
        Ztrials = Ztrials[indexes]
        Ztrials = list(Ztrials)

        trials = np.array(trials)
        trials = list(trials[indexes])

        # Vérifier si la première solution est non tabou,
        # ou tabou et respectant le critère d'aspiration
        if array_in_ndarray(trials[0], tabu_list) == False or Ztrials[0] < Zb:
            Ac = trials[0].copy()
            Zc = Ztrials[0]
        else:
            # Sinon chercher une solution parmis les solutions suivante
            # une qui n'est pas tabou
            find = False
            for j in range(1, NTS):
                if array_in_ndarray(trials[j], tabu_list) == False :
                    find = True
                    Ac = trials[j].copy()
                    Zc = Ztrials[j]
                    break
            # Si toute les autres solutions sont tabou, retourné à l'Etape 2
            if not find:
                continue

        #
        # Etape 5
        #

        # Ajout de la solution courante dans la liste tabou
        if array_in_ndarray(Ac, tabu_list) == False:
            tabu_list.append(Ac)
            TLL += 1
            if TLL == MTLS + 1:
                del tabu_list[0]
                TLL -= 1

        # Vérifier si la solution courante est inférieur que la meilleur solution
        if Zb > Zc:
            Ab = Ac.copy()
            Zb = Zc
        else:
            count += 1

    return Ab
