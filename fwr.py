def floyd_warshall_roy(matrix):
    v = len(matrix)
    dist = [list(row) for row in matrix]

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
