import numpy as np
import copy

f = open("./data/problem_83.txt", 'r')
map = []
for line in f:
    line = line.split("\n")[0].split(",")
    line = [int(e) for e in line]
    map.append(line)
map = np.array(map)
f.close()


def all_paths(n, i, j, parent):
    paths = []

    # up

    if i - 1 >= 0:
        if (i - 1, j) not in parent:
            results = all_paths(n, i - 1, j, parent + [(i - 1, j)])
            paths = paths + [[(i - 1, j)] + sub for sub in results]
    # down
    if i + 1 < n:
        if (i + 1, j) not in parent:
            results = all_paths(n, i + 1, j, parent + [(i + 1, j)])
            paths = paths + [[(i + 1, j)] + sub for sub in results]
    # right
    if j + 1 < n:
        if (i, j + 1) not in parent:
            results = all_paths(n, i, j + 1, parent + [(i, j + 1)])
            paths = paths + [[(i, j + 1)] + sub for sub in results]

    """
    # right
    if j - 1 >= 0 :
        if (i, j - 1) not in parent:
            results = all_paths(n, i, j - 1, parent + [(i, j - 1)])
            paths = paths + [[(i, j - 1)] + sub for sub in results]
    """
    if j == n - 1:
        if i == n - 1:
            paths = paths + [[]]

    return paths


def get_table_voisin(map):
    table_voisins = []
    map_i = map.shape[0]
    map_j = map.shape[1]
    for i in range(map_i):
        for j in range(map_j):
            voisins = []

            # top
            if i - 1 >= 0:
                voisins.append([map_j * (i - 1) + j, map[i - 1, j]])
            # bottom
            if i + 1 < map_i:
                voisins.append([map_j * (i + 1) + j, map[i + 1, j]])
            # right
            if j + 1 < map_j:
                voisins.append([map_j * i + j + 1, map[i, j + 1]])
            # left
            if j-1 >= 0 :
                voisins.append([map_j*i+j-1,map[i,j-1]])
            table_voisins.append(voisins)
    return table_voisins


def dijsktra(id, id_w, table_voisins):
    distances = [np.inf for v in table_voisins]
    min_distances = [-1 for v in table_voisins]
    distances[id] = np.inf
    min_distances[id] = id_w
    last_min_id = id
    nb_min_dist = 1

    while nb_min_dist != len(table_voisins):

        for (voisin_id, voisin_w) in table_voisins[last_min_id]:
            if min_distances[voisin_id] == -1:
                distances[voisin_id] = min(distances[voisin_id], min_distances[last_min_id] + voisin_w)

        last_min_id = np.argmin(distances)
        min_distances[last_min_id] = copy.copy(distances[last_min_id])
        distances[last_min_id] = np.inf
        nb_min_dist += 1
    return min_distances


table_voisins = get_table_voisin(map)

min_left = np.inf
result = dijsktra(0, map[0,0], table_voisins)
print(result[-1])
