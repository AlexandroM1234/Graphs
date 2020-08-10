"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex doesnt exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a an empty queue and enqueue a starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            vertex = q.dequeue()
            # if vertex has not been visited
            if vertex not in visited:
                # mark the vertex as visited
                visited.add(vertex)
                # print the marked vertex
                print(vertex)
                # add all of its neighbors to the back of the queue
                for next_vertex in self.get_neighbors(vertex):
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        # create a set to store the visited vertices
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop the first vertex
            vertex = s.pop()
            # if vertex has not been visited
            if vertex not in visited:
                # mark the vertex as visited
                visited.add(vertex)
                # print the marked vertex
                print(vertex)
                # add all of its neighbors to the top of the stack
                for next_vertex in self.get_neighbors(vertex):
                    s.push(next_vertex)


    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue PATH to the starting Vertex ID
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)
        # create a set of visited vertices
        visited = set()

        # while the queue is not empty 
        while q.size() > 0:
            # dequeue the first PATH
            # Grab the last vertex from the path
            last_path = q.dequeue()
            if last_path[-1] not in visited:
                # check if the vertex is the target
                if last_path[-1] == destination_vertex:
                    # if it is return the path
                    return last_path
                # mark the path as visited
                visited.add(last_path[-1])
                # then add a path to its neighbors to the back of the queue 
                for neighbors in self.get_neighbors(last_path[-1]):
                    # make a copy of the path
                    # append the neighbor to the back of the path 
                    neighbors_path=list(last_path) + [neighbors]
                    q.enqueue(neighbors_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty queue and enqueue PATH to the starting Vertex ID
        s = Stack()
        path = [starting_vertex]
        s.push(path)
        # create a set of visited vertices
        visited = set()

        # while the queue is not empty 
        while s.size() > 0:
            # dequeue the first PATH
            # Grab the last vertex from the path
            last_path = s.pop()
            if last_path[-1] not in visited:
                # check if the vertex is the target
                if last_path[-1] == destination_vertex:
                    # if it is return the path
                    return last_path
                # mark the path as visited
                visited.add(last_path[-1])
                # then add a path to its neighbors to the back of the queue 
                for neighbors in self.get_neighbors(last_path[-1]):
                    # make a copy of the path
                    # append the neighbor to the back of the path 
                    neighbors_path=list(last_path) + [neighbors]
                    s.push(neighbors_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
