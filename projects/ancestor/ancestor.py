class Graph:
    def __init__(self):
        self.vertices = {}

    def build_graph(self, dataset):
        # x1 is child, x0 is parent, this graph only adds parents to the tree as values for quicker earliest ancestry lookup
        for x in dataset:
            if x[1] not in self.vertices:
                self.vertices[x[1]] = set()
                self.vertices[x[1]].add(x[0])
                if x[0] not in self.vertices:
                    self.vertices[x[0]] = set()
            else:
                self.vertices[x[1]].add(x[0])
                if x[0] not in self.vertices:
                    self.vertices[x[0]] = set()

    def get_edges(self, dict_key):
        return self.vertices[dict_key]


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    graph.build_graph(ancestors)
    s = []
    visited = set()
    # keep track of level, start at 0
    level = 0
    tree = []

    if graph.vertices[starting_node] == set():
        return -1

    s.append((starting_node, level))
    while len(s) > 0:
        v = s.pop()

        if v[0] not in visited:
            visited.add(v[0])
            tree.append((v[0], level))
            for edge in graph.vertices[v[0]]:
                if edge not in visited:
                    level += 1
                    s.append((edge, level))

    if tree[-1][1] == tree[-2][1]:
        if tree[-1][0] > tree[-2][0]:
            return tree[-2][0]
        else:
            return tree[-1][0]
    else:
        return tree[-1][0]
