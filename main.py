from Util_Functions.read_data import read_data
from Util_Functions.display_solution import display_solution
from Algorithms.optimal_solution import get_optimal_solution
from Algorithms.heuristique_constructive import heuristique_constructive
from Algorithms.objective_function import compute_objective_function
from Algorithms.tabu_search import tabu_search


if __name__ == '__main__':
    #
    # Lecture des données
    #
    file_name = 'data/50_nodes_10_clusters_v2.txt'
    n, k, dist_matrix = read_data(file_name)

    #
    # La solution optimale
    #
    A_opt = get_optimal_solution(dist_matrix, k)

    #
    # Solution initiale fournie par l'heuristique constructive
    #
    Ac = heuristique_constructive(n, k)
    Zc = compute_objective_function(Ac, k, dist_matrix)[0]

    #
    # Solution fournie par la Recherche Taboue
    #

    # Nombre de solution de voisinage à générer
    NTS = 20

    # Taille maximale de la liste tabou
    MTLS = 20

    # Nombre maximale d'itération
    ITMAX = 300

    # Seuil de probabilité
    p = 0.95
    Ab = tabu_search(Ac, Zc, NTS, MTLS, ITMAX, p, k, dist_matrix)

    # Affichage des solutions
    print()
    print('*' * 80)
    print('*' * 10, ' Solution Optimale ', '*' * 10)
    print('*' * 80)
    display_solution(A_opt, k, dist_matrix)

    print()
    print('*' * 80)
    print('*' * 10, ' Solution Initiale avec l\'Heuristique constructive ', '*' * 10)
    print('*' * 80)
    display_solution(Ac, k, dist_matrix)

    print()
    print('*' * 80)
    print('*' * 10, ' Solution Obtenue avec la Recherche Taboue ', '*' * 10)
    print('*' * 80)
    display_solution(Ab, k, dist_matrix)
