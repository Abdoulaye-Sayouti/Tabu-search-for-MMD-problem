
"""
En fonction de la solution A, on caclcule son coût

"""
def compute_objective_function(A, k, dist_matrix):
    n = len(A)
    c = 1
    z = 0
    nodes = [0, 0]

    while c <= k:
        l1 = 0
        while l1 < n:
            if A[l1] == c:
                l2 = l1 + 1
                while l2 < n:
                    if A[l2] == c and z < dist_matrix[l1][l2]:
                        z = dist_matrix[l1][l2]
                        nodes[0] = l1
                        nodes[1] = l2
                    l2 += 1
            l1 += 1
        c += 1

    return z, nodes

