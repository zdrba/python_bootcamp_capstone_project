from . import Vertex

from typing import Set, Any, Optional


class Graph:
    def __init__(self, vertices: Set[Vertex]) -> None:
        self._vertices = vertices
        self._check_is_graph_valid()

    @property
    def vertices(self) -> Set[Vertex]:
        return self._vertices

    def _check_is_graph_valid(self) -> None:
        for vertex in self._vertices:
            for edge_vertex in vertex.edge_vertices:
                if edge_vertex not in self._vertices:
                    raise ValueError(f"Edge vertex [{str(edge_vertex.vid)}] not in vertices")

    def find_vertex_by_vid(self, vid: Any) -> Optional[Vertex]:
        for vertex in self._vertices:
            if vertex.vid == vid:
                return vertex

        return None
