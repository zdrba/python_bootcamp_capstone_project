from src.graph import Graph, Path, Vertex
from typing import Dict, List, Optional


class Dijkstra:
    def __init__(self, graph: Graph) -> None:
        self._graph = graph
        self._vertex_score: Dict[Vertex, int] = {}
        self._priority_list: List[Path] = []
        self._end_vertex: Optional[Vertex] = None

    @property
    def graph(self) -> Graph:
        return self._graph

    def find_shortest_path_from_to(self, start_vertex: Vertex, end_vertex: Vertex) -> Optional[Path]:
        self._prepare_shortest_path_search_from_to(start_vertex, end_vertex)

        while len(self._priority_list) > 0 and not self._is_shortest_path_found():
            explored_paths = self._discard_explored_paths_with_worse_score(self._explore())
            self._update_vertex_score(explored_paths)
            self._remove_top_from_priority_list()
            self._update_priority_list(explored_paths)

        if len(self._priority_list) > 0:
            return self._priority_list[0]
        else:
            return None

    def _prepare_shortest_path_search_from_to(self, start_vertex: Vertex, end_vertex: Vertex) -> None:
        start_path = Path([start_vertex])
        self._vertex_score = {start_vertex: 0}
        self._priority_list = [start_path]
        self._end_vertex = end_vertex

    def _explore(self) -> List[Path]:
        explored_paths = []
        start_path = self._priority_list[0]
        start_vertex = start_path.end_vertex

        for edge_vertex in start_vertex.edge_vertices:
            explored_paths.append(start_path + Path([start_vertex, edge_vertex]))

        return explored_paths

    def _update_vertex_score(self, explored_paths: List[Path]) -> None:
        for explored_path in explored_paths:
            if self._vertex_score.get(explored_path.end_vertex, explored_path.distance + 1) > explored_path.distance:
                self._vertex_score[explored_path.end_vertex] = explored_path.distance

    def _discard_explored_paths_with_worse_score(self, explored_paths: List[Path]) -> List[Path]:
        explored_paths_to_keep = []
        for explored_path in explored_paths:
            if explored_path.distance < self._vertex_score.get(explored_path.end_vertex, explored_path.distance + 1):
                explored_paths_to_keep.append(explored_path)

        return explored_paths_to_keep

    def _remove_top_from_priority_list(self) -> None:
        self._priority_list.pop(0)

    def _update_priority_list(self, paths: List[Path]) -> None:
        self._priority_list += paths
        self._priority_list.sort(key=lambda x: x.distance)

    def _is_shortest_path_found(self) -> bool:
        return self._priority_list[0].end_vertex == self._end_vertex
