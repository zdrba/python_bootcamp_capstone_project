from typing import Any, List, Optional

Vertex_id = Any


class Vertex:
    def __init__(self, vid: Vertex_id) -> None:
        self._vid = vid
        self._edge_vertices_distances = dict()

    @property
    def vid(self) -> Vertex_id:
        return self._vid

    @property
    def edge_vertices(self) -> List['Vertex']:
        return list(self._edge_vertices_distances.keys())

    @property
    def edge_vertices_ids(self) -> List[Vertex_id]:
        return [vertex.vid for vertex in self._edge_vertices_distances.keys()]

    def add_edge(self, vertex: 'Vertex', distance: int) -> None:
        self._edge_vertices_distances[vertex] = distance

    def get_edge_vertex_distance(self, edge_vertex: 'Vertex') -> Optional[int]:
        return self._edge_vertices_distances.get(edge_vertex, None)

    def find_edge_vertex_by_vid(self, vid: Vertex_id) -> Optional['Vertex']:
        for vertex in self._edge_vertices_distances.keys():
            if vertex.vid == vid:
                return vertex
        return None

    def __eq__(self, other: 'Vertex') -> bool:
        return self._is_vid_equal_to(other.vid) \
               and self._is_amount_of_edges_equal_to(len(other.edge_vertices)) \
               and self._are_all_edge_vertices_vids_in(other.edge_vertices_ids) \
               and self._are_all_edge_vertices_distances_same_as_in(other)

    def _is_vid_equal_to(self, other_vid: Vertex_id) -> bool:
        return self._vid == other_vid

    def _is_amount_of_edges_equal_to(self, amount: int) -> bool:
        return len(self._edge_vertices_distances) == amount

    def _are_all_edge_vertices_vids_in(self, vids: List[Vertex_id]) -> bool:
        for edge_vertex in self.edge_vertices_ids:
            if edge_vertex not in vids:
                return False
        return True

    def _are_all_edge_vertices_distances_same_as_in(self, other_vertex: 'Vertex') -> bool:
        for edge_vertex in self.edge_vertices:
            if self.get_edge_vertex_distance(edge_vertex) != other_vertex.get_edge_vertex_distance(edge_vertex):
                return False
        return True

    def __hash__(self) -> int:
        return hash(self._vid)
