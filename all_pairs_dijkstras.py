import heapq


def dijkstra(matrix, start_node):
    v = len(matrix)

    distances = [float("inf")] * v
    distances[start_node] = 0

    pq = [(0, start_node)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > distances[u]:
            continue

        for v_idx in range(v):
            weight = matrix[u][v_idx]

            if weight != float("inf") and weight != 0:
                distance = current_dist + weight

                if distance < distances[v_idx]:
                    distances[v_idx] = distance
                    heapq.heappush(pq, (distance, v_idx))

    return distances


def all_pairs_dijkstra(matrix, start=set([0])):
    if start:
        return [dijkstra(matrix, k) for k in start]
    else:
        return [dijkstra(matrix, k) for k in range(matrix)]
