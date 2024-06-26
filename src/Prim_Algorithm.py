import sys

class Graph:
    def __init__(self, vertice):
        self.V = vertice
        self.graph = [[0 for _ in range(vertice)] for _ in range(vertice)]

    def edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def prim(self):
        parent = [-1] * self.V
        key = [sys.maxsize] * self.V
        min_span_tree_set = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, min_span_tree_set)
            min_span_tree_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not min_span_tree_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

    def min_key(self, key, min_span_tree_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if key[v] < min_val and not min_span_tree_set[v]:
                min_val = key[v]
                min_index = v
        return min_index

def print_min_span_tree(parent, graph):
    print("\n\tEdge   Weight")
    for i in range(1, len(parent)):
        print("\t",parent[i], "-", i, "  ", graph[i][parent[i]])

def main():
    x = int(0)
    y = int(0)
    z = int(0)
    g = Graph(5)
    v = int(input("Enter the number of edges: "))
    print("\nEnter the edges and vertices in this format \"x y z\"")
    for i in range(0, v):
        input_tuple = tuple(map(int, input().split()))
        x, y, z = input_tuple
        g.edge(x, y, z)
    
    parent = g.prim()
    print_min_span_tree(parent, g.graph)

if __name__ == "__main__":
    print("Minimal Spanning Tree using Prim's Algorithm\n")
    main()