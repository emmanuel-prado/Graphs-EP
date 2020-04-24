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
        pass


def earliest_ancestor(ancestors: AncestryList, starting_node: int):
    pass
