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
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if self.vertices[vertex_id]:
            return self.vertices[vertex_id]
        else:
            raise IndexError("That vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit Stack and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit stack is not Empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex on the stack
            current_vertex = plan_to_visit.pop()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited neighbors to the Stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)

        def recursive_handler(stack, visited):
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
                recursive_handler(stack, visited)
            return

        recursive_handler(s, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            # v stands for vertex
            path = q.dequeue()
            # if the last v in the path is the destination_vertex return the path
            if path[-1] == destination_vertex:
                return path
            for neighbor in self.get_neighbors(path[-1]):
                if neighbor not in visited:
                    # clone the path
                    new_path = path[:]
                    # append the new neighbor to the end
                    new_path.append(neighbor)
                    # add the new_path to the queue
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        s.push([starting_vertex])

        while s.size() > 0:
            path = s.pop()

            if path[-1] == destination_vertex:
                return path
            for neighbor in self.get_neighbors(path[-1]):
                if neighbor not in visited:
                    new_path = path[:]
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        def recursive_handler(stack, visited):
            path = s.pop()
            if path[-1] == destination_vertex:
                return path
            if path[-1] not in visited:
                visited.add(path[-1])
                for neighbor in self.get_neighbors(path[-1]):
                    if neighbor not in visited:
                        path_clone = path[:]
                        path_clone.append(neighbor)
                        s.push(path_clone)
            return recursive_handler(s, visited)

        return recursive_handler(s, visited)


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
    print("bft")
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft")
    graph.dft(1)
    print("dft recursive")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bfs")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("dfs")
    print(graph.dfs(1, 6))
    print("dfs_recursive")
    print(graph.dfs_recursive(1, 6))
