from Algorithms.objective_function import compute_objective_function

"""
    Fonction permettant d'afficher une solution
"""
def display_solution(A, k, dist_matrix):
    obj = compute_objective_function(A, k, dist_matrix)
    print('Z = ', obj[0])
    print('d(', obj[1][0] + 1, ',', obj[1][1] + 1, ') = ', obj[0])
    for j in range(1, k + 1):
        c = [m + 1 for m in range(len(A)) if A[m] == j]
        print('Cluster ', j, ' : ', c)
