from src import Graph, Vertex

import pytest


def test_graph_init():
    no_vertices = set()
    one_vertex = {Vertex("A")}
    some_vertices = {Vertex("A"), Vertex("B"), Vertex("C")}

    empty_graph = Graph(no_vertices)
    graph_with_one_vertex = Graph(one_vertex)
    graph_with_some_vertices = Graph(some_vertices)

    assert empty_graph.vertices == no_vertices
    assert graph_with_one_vertex.vertices == one_vertex
    assert graph_with_some_vertices.vertices == some_vertices


def test_graph_edge_vertex_not_in_set_raises_value_error():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")

    a_vertex.add_edge(b_vertex, 74)

    Graph({a_vertex, b_vertex})

    with pytest.raises(ValueError):
        Graph({a_vertex})


def test_find_vertex_by_vid():
    av = Vertex("A")
    bv = Vertex("B")
    cv = Vertex("C")
    dv = Vertex("D")
    ev = Vertex("E")
    g = Graph({av, bv, cv, dv, ev})

    fav = g.find_vertex_by_vid("A")
    fcv = g.find_vertex_by_vid("C")
    fdv = g.find_vertex_by_vid("D")

    assert fav == av
    assert fcv == cv
    assert fdv == dv
