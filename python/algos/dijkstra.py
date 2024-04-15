"""
Path finding algorith for values in
a weighted graph between fixed nodes

@pesudo
Info to Keep Track:
    - unvisited nodes []
    -  assign the first node to 0
    - assign all other nodes infinity
    - previous nodes

@iteration 1:
    - Distance between all unvisited neighbours to the start
    - save the previous node and the distance between the neightbours
    - add it to the visited arr
@iteration 2:
    - Choose the the distance with the least value then make it the current node
    - calculate the distance to its neightbours

"""

import heapq
from typing import List, Dict


def dijkstra(n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
    # convert edged to an adjacency list
    adj = {}
    for i in range(n):
        adj[i] = []

    for s, destination, weight in edges:
        adj[s].append([destination, weight])
    # vertex -> distance of shortest path
    result = {}
    min_heap = [[0, src]]

    while min_heap:
        w1, n1 = heapq.heappop(min_heap)
        if n1 in result:
            continue
        result[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in result:
                heapq.heappush(min_heap, [w1 + w2, n2])

    for i in range(n):
        if i not in result:
            result[i] = -1

    return result