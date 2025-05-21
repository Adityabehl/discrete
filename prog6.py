#Write a Program to check if a given graph is a complete graph. Represent the graph using 
#the Adjacency Matrix representation.
class Graph:
    def __init__(self, vertices, graph_type):
        self.vertices = vertices
        self.graph_type = graph_type
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        if self.graph_type == 1:  # Undirected graph
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
        else:  # Directed graph
            self.adj_matrix[u][v] = 1

    def is_complete(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and self.adj_matrix[i][j] == 0:
                    return False
        return True

    def get_matrix(self):
        return self.adj_matrix


if __name__ == "__main__":
    graph_type = int(input("Enter Your Graph Type (1. Undirected, 2. Directed): "))
    num_vertices = int(input("Enter number of vertices: "))

    g = Graph(num_vertices, graph_type)

    num_edges = int(input("Enter number of edges: "))

    for i in range(num_edges):
        a = int(input(f"Enter first vertex of edge {i+1}: ")) - 1
        b = int(input("Enter second vertex of the same edge: ")) - 1
        g.add_edge(a, b)

    print("\nAdjacency Matrix:")
    matrix = g.get_matrix()
    for row in matrix:
        print(row)

    if g.is_complete():
        print("\nThe graph is a complete graph.")
    else:
        print("\nThe graph is not a complete graph.")
