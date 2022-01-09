from src.graph import Vertex

from typing import Set, Any, Optional


class Graph:
    def __init__(self) -> None:
        self._vertices = set()

    @property
    def vertices(self) -> Set[Vertex]:
        return self._vertices

    def add_vertex(self, vertex: Vertex) -> None:
        if not self._does_vertex_with_vid_exists(vertex.vid):
            self._vertices.add(vertex)
        else:
            raise ValueError(f"Vertex with vid: {str(vertex.vid)} already exists.")

    def find_vertex_by_vid(self, vid: Any) -> Optional[Vertex]:
        for vertex in self._vertices:
            if vertex.vid == vid:
                return vertex

        return None

    def _does_vertex_with_vid_exists(self, vid: Any) -> bool:
        return len(set(filter(lambda v: v.vid == vid, self._vertices))) > 0
