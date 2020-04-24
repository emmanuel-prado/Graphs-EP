# pylint: disable=no-member

# https://docs.python.org/3/library/typing.html
# Integer Types -  int, float, complex
# Sequence Types - list, tuple, range, strings
# Set Types - set, frozenset
# Mapping Types - dict (a mapping object maps hashable values to arbitrary objects)
from typing import List, Dict, Tuple, Set

AncestryList = List[Tuple(int, int)]
VisitedSet = Set[int]
Stack = List[int]


class Graph:
    def __init__(self):
        self.vertices = Dict[int, set]

    def build_graph(self, dataset: AncestryList) -> str:
        visited = VisitedSet
        for x in dataset:
            if x[0] and x[1] not in visited:
                visited.add(x[0])
                visited.add(x[1])
                self.vertices[x[0]].add(x[1])
                self.vertices[x[1]].add(x[0])

        return f"successfully compiled graph"

    def get_edges(self, dict_key: int) -> int:
        return self.vertices[dict_key]


def earliest_ancestor(ancestors: AncestryList, starting_node: int):
    graph = Graph()
    graph.build_graph(ancestors)

    s = Stack
    visited = VisitedSet
    # keep track of level, start at 0
    level = 0
    tree = List[tuple]

    s.push((starting_node, level))
    while len(s) > 0:
        v = s.pop()

        if v[0] not in visited:
            level += 1
            visited.add(v[0])
            tree.append((v[0], level))

            for edge in graph.vertices[v[0]]:
                if edge not in visited:
                    s.push((edge, level))

    if tree[-1][1] == tree[-2][1]:
        if tree[-1][1] > tree[-2][1]:
            return tree[-2][0]
        else:
            return tree[-1][0]

    return tree[-1][0]
