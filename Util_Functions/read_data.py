

"""
Fonction permettant de lire les données des fichiers

"""
def read_data(file_name):
    file = open(file_name, 'r')
    count = 1
    dist = []
    for l in file:
        if count == 1:
            N = int(l)
            count += 1
            continue
        if count == 2:
            k = int(l)
            count += 1
            continue
        dist.append(list(map(int, l.rstrip().split('  '))))
    return N, k, dist

