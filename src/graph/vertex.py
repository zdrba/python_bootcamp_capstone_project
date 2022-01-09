from typing import Any, List, NamedTuple


class Vertex:
    class Edge(NamedTuple):
        vertex: 'Vertex'
        distance: int

    def __init__(self, vid: Any) -> None:
        self._vid = vid
        self._edges = []

    @property
    def vid(self) -> Any:
        return self._vid

    @property
    def edges(self) -> List[Edge]:
        return self._edges

    def add_edge(self, vertex: 'Vertex', distance: int) -> None:
        self._edges.append(self.Edge(vertex, distance))
