# https://docs.python.org/3/library/typing.html
from typing import List, Dict, Tuple

AncestryList = List[Tuple(int, int)]


class Graph:
    def __init__(self):
        self.vertices = Dict[int, int]

    def build_tree(self, dataset: AncestryList) -> Dict:
        pass

    def add_vertex(self, v: int) -> str:
        pass

    def add_edge(self, v1: int, v2: int) -> str:
        pass

    def get_edge(self, vertex: int) -> int:
        pass


def earliest_ancestor(ancestors: AncestryList, starting_node: int):
    pass
