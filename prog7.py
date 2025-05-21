class Graph:
    def __init__(self, vertices, graph_type):
        self.vertices = vertices
        self.graph_type = graph_type
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        if self.graph_type == 1:  # Undirected
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)
        else:  # Directed
            self.adj_list[u].append(v)

    def is_complete(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and j not in self.adj_list[i]:
                    return False
        return True

    def get_list(self):
        return self.adj_list


if __name__ == "__main__":
    graph_type = int(input("Enter Your Graph Type (1. Undirected, 2. Directed): "))
    num_vertices = int(input("Enter number of vertices: "))
    g = Graph(num_vertices, graph_type)

    num_edges = int(input("Enter number of edges: "))
    for i in range(num_edges):
        a = int(input(f"Enter first vertex of edge {i + 1}: "))
        b = int(input("Enter second vertex of the same edge: "))
        g.add_edge(a, b)

    print("\nYour Adjacency List:")
    for i, neighbors in enumerate(g.get_list()):
        print(f"{i} -> {neighbors}")

    if g.is_complete():
        print("\nThe graph is a complete graph.")
    else:
        print("\nThe graph is not a complete graph.")
