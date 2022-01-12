from . import Vertex

from typing import List


class Path:
    def __init__(self, vertices: List[Vertex]) -> None:
        self._vertices = vertices
        self._check_is_path_valid()

    @property
    def vertices(self) -> List[Vertex]:
        return self._vertices

    @property
    def distance(self) -> int:
        distance = 0
        if len(self._vertices) > 0:
            previous_vertex = self._vertices[0]
            for i in range(1, len(self._vertices)):
                next_vertex = self._vertices[i]
                distance += previous_vertex.get_edge_vertex_distance(next_vertex)
                previous_vertex = next_vertex
        return distance

    @property
    def start_vertex(self) -> Vertex:
        return self._vertices[0]

    @property
    def end_vertex(self) -> Vertex:
        return self._vertices[-1]

    def concat(self, other: 'Path') -> 'Path':
        self._check_is_concatenating_path_valid(other)
        return Path(self.vertices + other.vertices[1:])

    def _check_is_concatenating_path_valid(self, other: 'Path') -> None:
        if not self._ends_the_same_as_other_starts(other):
            raise ValueError("Concatenating path does not start with the same vertex as this path ends")

    def _ends_the_same_as_other_starts(self, other: 'Path') -> bool:
        return self.end_vertex == other.start_vertex

    def _check_is_path_valid(self) -> None:
        if not self._is_path_valid():
            raise ValueError("Path broken")

    def _is_path_valid(self) -> bool:
        if len(self._vertices) > 0:
            previous_vertex = self._vertices[0]
            for i in range(1, len(self._vertices)):
                next_vertex = self._vertices[i]
                if next_vertex not in previous_vertex.edge_vertices:
                    return False
                previous_vertex = next_vertex
        return True

    def __eq__(self, other: 'Path') -> bool:
        return self._are_vertices_in_same_order_as(other.vertices) \
               and self._is_amount_of_vertices_equal_to(len(other.vertices))

    def _are_vertices_in_same_order_as(self, other_vertices: List[Vertex]) -> bool:
        for i in range(len(self._vertices)):
            if self.vertices[i] != other_vertices[i]:
                return False

        return True

    def _is_amount_of_vertices_equal_to(self, amount: int) -> bool:
        return len(self.vertices) == amount

    def __add__(self, other: 'Path') -> 'Path':
        return self.concat(other)
