import random
from fwr import floyd_warshall_roy
import time
from all_pairs_dijkstras import all_pairs_dijkstra
import generator

INF = float("inf")


def test_fwr(adj_matrix):
    result = floyd_warshall_roy(adj_matrix)


def test_apd(adj_matrix, k=[]):
    result = all_pairs_dijkstra(adj_matrix, k)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print(sys.argv)
        exit(1)
    v: int = int(sys.argv[1])
    k: int = int(sys.argv[2])
    adj_matrix = generator.generate_adj_matrix(v)

    k_source = set([random.randint(0, v - 1) for i in range(k)])
    start = time.perf_counter()

    test_apd(adj_matrix, k_source)

    end = time.perf_counter()
    total = end - start

    print(f"Dijkstras {total:.3f} seconds\n")

    start_two = time.perf_counter()
    test_fwr(adj_matrix)

    end_two = time.perf_counter()
    total_two = end_two - start_two

    print(f"FWR {total_two:.3f} seconds")

    print(
        f"\nIF NEGATIVE, FWR DID BETTER. OTHERWISE DIJKSTRAS DID BETTER\n{(total_two - total):.3f} s"
    )

    # print("\n")
    # test_fwr(adj_matrix)
