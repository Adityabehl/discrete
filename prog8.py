#Write a Program to accept a directed graph G and compute the in-degree and outdegree of each vertex.
class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def compute_degrees(self):
        in_degrees = [0] * self.vertices
        out_degrees = [0] * self.vertices

        for u in range(self.vertices):
            out_degrees[u] = len(self.adj_list[u])
            for v in self.adj_list[u]:
                in_degrees[v] += 1

        return in_degrees, out_degrees


if __name__ == "__main__":
    num_vertices = int(input("Enter number of vertices: "))
    g = DirectedGraph(num_vertices)

    num_edges = int(input("Enter number of edges: "))
    for i in range(num_edges):
        a = int(input(f"Enter first vertex of edge {i + 1}: ")) - 1
        b = int(input("Enter second vertex of the same edge: ")) - 1
        g.add_edge(a, b)

    in_degrees, out_degrees = g.compute_degrees()

    print("\nVertex\tin-Degree\tOut-Degree")
    for v in range(num_vertices):
        print(f"{v}\t{in_degrees[v]}\t\t{out_degrees[v]}")
