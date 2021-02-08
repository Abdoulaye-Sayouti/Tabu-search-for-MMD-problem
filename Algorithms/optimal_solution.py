
"""
On peut déterminer la solution optimale avec la modélisation de Louis

"""

def get_optimal_solution(distance_matrix, k):
    n = len(distance_matrix)
    A = []
    for k in range(n):
        A.append(0)
    c = 1
    for node in range(n):
        if A[node] == 0:
            A[node] = c
            for j in range(node + 1, n):
                if distance_matrix[node][j] <= 1000:
                    A[j] = c
            c += 1

    return A
