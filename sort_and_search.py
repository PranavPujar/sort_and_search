from collections import defaultdict
from typing import List, Set, Dict, Tuple
import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.weights = {}

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        self.graph[u].append(v)
        self.weights[(u, v)] = weight

    def topological_sort(self) -> List[int]:
        visited = set()
        temp = set()
        order = []
        
        def dfs(vertex: int) -> None:
            if vertex in temp:
                raise ValueError("Graph has a cycle")
            if vertex in visited:
                return
            
            temp.add(vertex)
            
            for neighbor in self.graph[vertex]:
                dfs(neighbor)
                
            temp.remove(vertex)
            visited.add(vertex)
            order.append(vertex)
        
        for vertex in list(self.graph):
            if vertex not in visited:
                dfs(vertex)
                
        return order[::-1]

    def dfs(self, start: int) -> List[int]:
        visited = set()
        result = []
        
        def dfs_recursive(vertex: int) -> None:
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return result

    def kruskal(self) -> List[Tuple[int, int, int]]:
        parent = {}
        rank = {}
        
        def find(vertex: int) -> int:
            if vertex not in parent:
                parent[vertex] = vertex
                rank[vertex] = 0
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]
        
        def union(u: int, v: int) -> None:
            root_u, root_v = find(u), find(v)
            if root_u != root_v:
                if rank[root_u] < rank[root_v]:
                    root_u, root_v = root_v, root_u
                parent[root_v] = root_u
                if rank[root_u] == rank[root_v]:
                    rank[root_u] += 1
        
        edges = [(w, u, v) for (u, v), w in self.weights.items()]
        edges.sort()
        
        mst = []
        for weight, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                mst.append((u, v, weight))
        
        return mst

def test_topological_sort():
    g = Graph()
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    
    result = g.topological_sort()
    print("Topological Sort Test:")
    print(f"Expected: [5, 4, 2, 3, 1, 0] or similar valid ordering")
    print(f"Got: {result}")

def test_dfs():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    
    result = g.dfs(0)
    print("\nDFS Test:")
    print(f"Expected: [0, 1, 3, 4, 2, 5] or similar valid DFS ordering")
    print(f"Got: {result}")

def test_kruskal():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 3)
    g.add_edge(2, 3, 1)
    g.add_edge(2, 4, 5)
    g.add_edge(3, 4, 7)
    
    result = g.kruskal()
    print("\nKruskal's Algorithm Test:")
    print("Expected: [(2, 3, 1), (1, 2, 2), (1, 3, 3), (0, 1, 4)] or similar valid MST")
    print(f"Got: {result}")

if __name__ == "__main__":
    test_topological_sort()
    test_dfs()
    test_kruskal()