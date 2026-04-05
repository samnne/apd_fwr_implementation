import random

INF = float("inf")


def generate_adj_matrix(n: int):
    adj_matrix = []
    # initlize each row with INF except when i == j == 0.
    for i in range(n):
        row = []
        for j in range(n):
            if i != j:
                row.append(INF)
                continue
            row.append(0)
        adj_matrix.append(row)
    # give 3 immediate neighbours to a given vertex.
    for i in range(n):
        for j in range(3):
            temp = random.randint(0, n - 1)
            if temp == i:
                temp = (temp + i) % n
            adj_matrix[i][temp] = random.randint(0, 20)
    return adj_matrix
