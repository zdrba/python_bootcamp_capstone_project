from src import Dijkstra
from src.graph import Graph, Vertex, Path

import pytest


@pytest.fixture()
def dummy_graph():
    va = Vertex("A")
    vb = Vertex("B")
    vc = Vertex("C")
    vd = Vertex("D")
    ve = Vertex("E")
    vf = Vertex("F")

    va.add_edge(vb, 2)
    va.add_edge(vc, 4)
    va.add_edge(vd, 7)

    vb.add_edge(va, 2)
    vb.add_edge(vc, 7)
    vb.add_edge(ve, 6)

    vc.add_edge(va, 4)
    vc.add_edge(vb, 7)
    vc.add_edge(ve, 5)
    vc.add_edge(vd, 8)

    vd.add_edge(va, 7)
    vd.add_edge(vc, 8)
    vd.add_edge(vf, 3)

    ve.add_edge(vb, 6)
    ve.add_edge(vc, 5)
    ve.add_edge(vf, 1)

    vf.add_edge(vd, 3)
    vf.add_edge(vf, 1)

    return Graph({va, vb, vc, vd, ve, vf})


def test_dijkstra_init(dummy_graph):
    d = Dijkstra(dummy_graph)
    assert d.graph == dummy_graph
    assert d._vertex_score == {}
    assert d._priority_list == []


def test_dijkstra_prepare_shortest_path_search_from_to(dummy_graph):
    d = Dijkstra(dummy_graph)
    a_vertex = dummy_graph.find_vertex_by_vid("A")

    d._prepare_shortest_path_search_from_to(a_vertex, a_vertex)

    start_path = Path([a_vertex])

    assert d._vertex_score == {a_vertex: 0}
    assert d._priority_list == [start_path]


def test_dijkstra_explore_no_edges():
    a_vertex = Vertex("A")
    d = Dijkstra(Graph({a_vertex}))

    d._prepare_shortest_path_search_from_to(a_vertex, a_vertex)
    explored_paths = d._explore()

    assert len(explored_paths) == 0


def test_dijkstra_explore_one_edge():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")

    a_vertex.add_edge(b_vertex, 1)

    d = Dijkstra(Graph({a_vertex, b_vertex}))
    d._prepare_shortest_path_search_from_to(a_vertex, b_vertex)

    explored_paths = d._explore()

    assert Path([a_vertex, b_vertex]) in explored_paths


def test_dijkstra_explore_with_paths_already_in_priority_list(dummy_graph):
    a_vertex = dummy_graph.find_vertex_by_vid("A")
    b_vertex = dummy_graph.find_vertex_by_vid("B")
    c_vertex = dummy_graph.find_vertex_by_vid("C")
    d_vertex = dummy_graph.find_vertex_by_vid("D")
    e_vertex = dummy_graph.find_vertex_by_vid("E")
    ab = Path([a_vertex, b_vertex])
    ac = Path([a_vertex, c_vertex])
    ad = Path([a_vertex, d_vertex])

    d = Dijkstra(dummy_graph)
    d._priority_list = [ab, ac, ad]

    explored_paths = d._explore()

    aba = Path([a_vertex, b_vertex, a_vertex])
    abc = Path([a_vertex, b_vertex, c_vertex])
    abe = Path([a_vertex, b_vertex, e_vertex])

    assert len(explored_paths) == 3
    assert aba in explored_paths
    assert abc in explored_paths
    assert abe in explored_paths


def test_dijkstra_update_vertex_score_with_explored_paths_add_one_new_vertex():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")

    a_vertex.add_edge(b_vertex, 1)

    d = Dijkstra(Graph({a_vertex, b_vertex}))
    d._prepare_shortest_path_search_from_to(a_vertex, b_vertex)

    explored_paths = d._explore()
    d._update_vertex_score(explored_paths)

    assert d._vertex_score == {a_vertex: 0, b_vertex: 1}


def test_dijkstra_update_vertex_score_with_explored_paths_add_multiple_new_vertices(dummy_graph):
    a_vertex = dummy_graph.find_vertex_by_vid("A")
    b_vertex = dummy_graph.find_vertex_by_vid("B")
    c_vertex = dummy_graph.find_vertex_by_vid("C")
    d_vertex = dummy_graph.find_vertex_by_vid("D")
    d = Dijkstra(dummy_graph)

    d._prepare_shortest_path_search_from_to(a_vertex, d_vertex)
    explored_paths = d._explore()
    d._update_vertex_score(explored_paths)

    assert d._vertex_score[a_vertex] == 0
    assert d._vertex_score[b_vertex] == 2
    assert d._vertex_score[c_vertex] == 4
    assert d._vertex_score[d_vertex] == 7


def test_dijkstra_update_vertex_score_with_explored_paths_keep_smaller_score(dummy_graph):
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    c_vertex = Vertex("C")

    a_vertex.add_edge(b_vertex, 3)
    a_vertex.add_edge(c_vertex, 6)
    b_vertex.add_edge(c_vertex, 4)

    d = Dijkstra(Graph({a_vertex, b_vertex, c_vertex}))
    d._vertex_score = {a_vertex: 0, b_vertex: 3, c_vertex: 6}
    d._priority_list = [Path([a_vertex, b_vertex])]
    explored_paths = d._explore()
    d._update_vertex_score(explored_paths)

    assert d._vertex_score[c_vertex] == 6


def test_dijkstra_discard_explored_paths_on_one_edge_with_worse_score():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")

    a_vertex.add_edge(b_vertex, 3)
    b_vertex.add_edge(a_vertex, 3)

    d = Dijkstra(Graph({a_vertex, b_vertex}))
    d._vertex_score = {a_vertex: 0, b_vertex: 3}
    d._priority_list = [Path([a_vertex, b_vertex])]
    explored_paths = d._explore()

    explored_paths_to_keep = d._discard_explored_paths_with_worse_score(explored_paths)

    assert len(explored_paths_to_keep) == 0


def test_dijkstra_discard_explored_paths_on_two_edges_with_worse_score_keeping_one():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    c_vertex = Vertex("C")

    a_vertex.add_edge(b_vertex, 3)
    a_vertex.add_edge(c_vertex, 7)
    b_vertex.add_edge(a_vertex, 3)
    b_vertex.add_edge(c_vertex, 3)
    c_vertex.add_edge(a_vertex, 7)
    c_vertex.add_edge(b_vertex, 3)

    d = Dijkstra(Graph({a_vertex, b_vertex, c_vertex}))
    d._vertex_score = {a_vertex: 0, b_vertex: 3, c_vertex: 7}
    d._priority_list = [Path([a_vertex, b_vertex])]
    explored_paths = d._explore()

    explored_paths_to_keep = d._discard_explored_paths_with_worse_score(explored_paths)

    assert len(explored_paths_to_keep) == 1
    assert Path([a_vertex, b_vertex, c_vertex]) in explored_paths_to_keep


def test_dijkstra_discard_explored_paths_on_two_edges_with_worse_score_keeping_none():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    c_vertex = Vertex("C")

    a_vertex.add_edge(b_vertex, 3)
    a_vertex.add_edge(c_vertex, 7)
    b_vertex.add_edge(a_vertex, 3)
    b_vertex.add_edge(c_vertex, 5)
    c_vertex.add_edge(a_vertex, 7)
    c_vertex.add_edge(b_vertex, 5)

    d = Dijkstra(Graph({a_vertex, b_vertex, c_vertex}))
    d._vertex_score = {a_vertex: 0, b_vertex: 3, c_vertex: 7}
    d._priority_list = [Path([a_vertex, b_vertex])]
    explored_paths = d._explore()

    explored_paths_to_keep = d._discard_explored_paths_with_worse_score(explored_paths)

    assert len(explored_paths_to_keep) == 0


def test_dijkstra_remove_first_element_in_priority_list(dummy_graph):
    a_vertex = dummy_graph.find_vertex_by_vid("A")
    b_vertex = dummy_graph.find_vertex_by_vid("B")
    d = Dijkstra(dummy_graph)

    d._priority_list = [Path([a_vertex]), Path([b_vertex])]
    d._remove_top_from_priority_list()

    assert len(d._priority_list) == 1
    assert Path([b_vertex]) in d._priority_list


def test_dijkstra_update_priority_score_add_paths(dummy_graph):
    a_vertex = dummy_graph.find_vertex_by_vid("A")
    b_vertex = dummy_graph.find_vertex_by_vid("B")
    d = Dijkstra(dummy_graph)

    first_paths = [Path([a_vertex])]
    second_paths = [Path([a_vertex, b_vertex])]

    d._update_priority_list(first_paths)

    assert len(d._priority_list) == 1
    assert first_paths[0] in d._priority_list

    d._update_priority_list(second_paths)

    assert len(d._priority_list) == 2
    assert second_paths[0] in d._priority_list

    d._priority_list = []
    d._update_priority_list(first_paths + second_paths)
    assert len(d._priority_list) == 2
    assert first_paths[0] in d._priority_list
    assert second_paths[0] in d._priority_list


def test_dijkstra_update_priority_score_is_sorted_by_distance(dummy_graph):
    a_vertex = dummy_graph.find_vertex_by_vid("A")
    b_vertex = dummy_graph.find_vertex_by_vid("B")
    c_vertex = dummy_graph.find_vertex_by_vid("C")
    d_vertex = dummy_graph.find_vertex_by_vid("D")

    ab = Path([a_vertex, b_vertex])
    ac = Path([a_vertex, c_vertex])
    ad = Path([a_vertex, d_vertex])

    d = Dijkstra(dummy_graph)
    d._priority_list = [ac]
    d._update_priority_list([ad, ab])

    assert d._priority_list[0] == ab
    assert d._priority_list[1] == ac
    assert d._priority_list[2] == ad


def test_is_shortest_path_found_when_end_vertex_is_reached(dummy_graph):
    a_vertex = dummy_graph.find_vertex_by_vid("A")
    b_vertex = dummy_graph.find_vertex_by_vid("B")
    c_vertex = dummy_graph.find_vertex_by_vid("C")
    d_vertex = dummy_graph.find_vertex_by_vid("D")

    ab = Path([a_vertex, b_vertex])
    ac = Path([a_vertex, c_vertex])
    ad = Path([a_vertex, d_vertex])

    d = Dijkstra(dummy_graph)
    d._prepare_shortest_path_search_from_to(a_vertex, d_vertex)
    assert d._end_vertex == d_vertex

    assert not d._is_shortest_path_found()
    d._remove_top_from_priority_list()

    d._update_priority_list([ab])
    assert not d._is_shortest_path_found()

    d._remove_top_from_priority_list()

    d._update_priority_list([ad])
    assert d._is_shortest_path_found()

    d._remove_top_from_priority_list()

    d._update_priority_list([ac])
    assert not d._is_shortest_path_found()


def test_dijkstra_find_shortest_path_from_to(dummy_graph):
    d = Dijkstra(dummy_graph)
    a_vertex = d.graph.find_vertex_by_vid("A")
    b_vertex = d.graph.find_vertex_by_vid("B")
    e_vertex = d.graph.find_vertex_by_vid("E")
    d_vertex = d.graph.find_vertex_by_vid("D")
    f_vertex = d.graph.find_vertex_by_vid("F")

    assert d.find_shortest_path_from_to(a_vertex, d_vertex) == Path([a_vertex, d_vertex])
    assert d.find_shortest_path_from_to(a_vertex, f_vertex) == Path([a_vertex, b_vertex, e_vertex, f_vertex])
