"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """
    Represent a graph as a dictionary of
    vertices mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, one, two):
        """
        Add a directed edge to the graph.
        """
        if one in self.vertices and two in self.vertices:
            self.vertices[one].add(two)
        else:
            raise Exception('Error: Vertices do not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        raise Exception('Error: Value does not exist')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()

        while queue.size():
            node = queue.dequeue()

            if node not in visited:
                visited.add(node)

                for neighbor in self.get_neighbors(node):
                    queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()

        while stack.size():
            node = stack.pop()

            if node not in visited:
                visited.add(node)

                for neighbor in self.get_neighbors(node):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if not visited:
            visited = set()

        if starting_vertex not in visited:

            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()

        while queue.size():
            path = queue.dequeue()
            last = path[-1]

            if last not in visited:
                visited.add(last)

                if last == destination_vertex:
                    return path

                for neighbor in self.get_neighbors(last):
                    queue.enqueue([*path, neighbor])

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()

        while stack.size() > 0:
            path = stack.pop()
            last = path[-1]

            if last not in visited:
                visited.add(last)

                if last == destination_vertex:
                    return path

                for neighbor in self.get_neighbors(last):
                    stack.push([*path, neighbor])

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """

        if not visited:
            visited = set()

        if starting_vertex in visited:
            return None

        visited.add(starting_vertex)

        if starting_vertex == destination_vertex:
            return [starting_vertex]

        for neighbor in self.get_neighbors(starting_vertex):
            path = self.dfs_recursive(neighbor, destination_vertex, visited)
            print('path', path)

            if path and destination_vertex in path:
                return [starting_vertex, *path]


if __name__ == '__main__':
    GRAPH = Graph()  # Instantiate your GRAPH
    GRAPH.add_vertex(1)
    GRAPH.add_vertex(2)
    GRAPH.add_vertex(3)
    GRAPH.add_vertex(4)
    GRAPH.add_vertex(5)
    GRAPH.add_vertex(6)
    GRAPH.add_vertex(7)
    GRAPH.add_edge(5, 3)
    GRAPH.add_edge(6, 3)
    GRAPH.add_edge(7, 1)
    GRAPH.add_edge(4, 7)
    GRAPH.add_edge(1, 2)
    GRAPH.add_edge(7, 6)
    GRAPH.add_edge(2, 4)
    GRAPH.add_edge(3, 5)
    GRAPH.add_edge(2, 3)
    GRAPH.add_edge(4, 6)

    # Should print:
    print(GRAPH.vertices)
    # print(GRAPH.vertices)

    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    GRAPH.bft(1)
    # GRAPH.bft(1)

    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    GRAPH.dft(1)
    # GRAPH.dft(1)
    GRAPH.dft_recursive(1)

    # Valid BFS path:
    #     [1, 2, 4, 6]
    print(GRAPH.bfs(1, 6))
    # print(GRAPH.bfs(1, 6))

    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    print(GRAPH.dfs(1, 6))
    print(GRAPH.dfs_recursive(1, 6))
    # print(GRAPH.dfs_recursive(1, 6))
