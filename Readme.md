# Graph Algorithms Implementation

This repository contains Python implementations of three fundamental graph algorithms:

1. Topological Sort
2. Depth-First Search (DFS)
3. Kruskal's Algorithm (Minimum Spanning Tree)

## Overview

The code provides a single `Graph` class that implements all three algorithms using adjacency list representation. Each algorithm is optimized for efficiency and includes test cases.

## Algorithm Details

### Topological Sort

- Sorts vertices in a directed acyclic graph (DAG)
- Returns vertices in order where for each directed edge u→v, vertex u comes before v
- Includes cycle detection
- Time complexity: O(V + E)

### Depth-First Search (DFS)

- Traverses graph by exploring as far as possible along each branch before backtracking
- Returns vertices in order visited
- Time complexity: O(V + E)

### Kruskal's Algorithm

- Finds minimum spanning tree in weighted graph
- Uses Union-Find data structure with path compression
- Returns list of edges in minimum spanning tree
- Time complexity: O(E log E)

## Usage

```python
# Create a graph
g = Graph()

# Add edges (with optional weights for Kruskal's algorithm)
g.add_edge(u, v)           # For DFS/Topological Sort
g.add_edge(u, v, weight)   # For Kruskal's algorithm

# Run algorithms
topo_order = g.topological_sort()
dfs_order = g.dfs(start_vertex)
mst_edges = g.kruskal()
```

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Testing

The code includes test cases for each algorithm. Run tests using:

```bash
python graph_algorithms.py
```

## Implementation Notes

- Uses adjacency list representation for memory efficiency
- Implements recursive DFS for cleaner code
- Uses path compression in Union-Find for Kruskal's algorithm
- All algorithms handle disconnected graphs correctly

## Time Complexities

| Algorithm           | Time Complexity |
| ------------------- | --------------- |
| Topological Sort    | O(V + E)        |
| DFS                 | O(V + E)        |
| Kruskal's Algorithm | O(E log E)      |

where V is the number of vertices and E is the number of edges.

## Example Output

```python
# Topological Sort
Input: 5→2→3→1, 5→0, 4→0, 4→1
Output: [5, 4, 2, 3, 1, 0]

# DFS
Input: Tree with root 0 and edges to 1,2
Output: [0, 1, 3, 4, 2, 5]

# Kruskal
Input: Weighted graph with 5 vertices
Output: [(2,3,1), (1,2,2), (1,3,3), (0,1,4)]
```

## License

Feel free to use and modify this code for your own projects.
