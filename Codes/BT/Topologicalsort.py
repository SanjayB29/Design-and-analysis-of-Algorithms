class Graph:
    def __init__(self, vertices):
        self.graph = {}  # Dictionary to store graph
        self.V = vertices  # No. of vertices

        # Initialize graph with empty adjacency lists for each vertex
        for v in range(self.V):
            self.graph[v] = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        stack.insert(0, v)

    def allTopologicalSorts(self):
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function for all vertices not yet visited
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        print(stack)

# Example Usage
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("All Topological sorts")
g.allTopologicalSorts()
