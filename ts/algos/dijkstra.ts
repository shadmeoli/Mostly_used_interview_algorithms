/**
 * Path finding algorith for values in
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

 */
function dijkstra(
  n: number,
  edges: number[][],
  src: number
): { [vertex: number]: number } {
  // Convert edges to an adjacency list
  const adj: { [vertex: number]: [number, number][] } = {};
  for (let i = 0; i < n; i++) {
    adj[i] = [];
  }

  for (const [s, destination, weight] of edges) {
    adj[s].push([destination, weight]);
  }

  // Vertex -> distance of shortest path
  const result: { [vertex: number]: number } = {};
  const minHeap: [number, number][] = [[0, src]];

  while (minHeap.length) {
    const [w1, n1] = minHeap.shift()!;
    if (n1 in result) {
      continue;
    }
    result[n1] = w1;

    for (const [n2, w2] of adj[n1]) {
      if (!(n2 in result)) {
        minHeap.push([w1 + w2, n2]);
        minHeap.sort((a, b) => a[0] - b[0]); // Re-sort min heap (inefficient)
      }
    }
  }

  for (let i = 0; i < n; i++) {
    if (!(i in result)) {
      result[i] = -1;
    }
  }

  return result;
}
