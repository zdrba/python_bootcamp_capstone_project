from src.graph import Graph
from src.graph import Vertex

import pytest

def test_graph_init():
    graph = Graph()
    vertices = graph.vertices

    assert vertices == set()


def test_add_vertex():
    g = Graph()
    v = Vertex("A")

    g.add_vertex(v)
    vertices = g.vertices

    assert len(vertices) == 1
    assert vertices.pop() == v


def test_add_vertex_with_same_vid_throws_value_error():
    with pytest.raises(ValueError):
        g = Graph()
        v1 = Vertex("A")
        v2 = Vertex("A")
        g.add_vertex(v1)
        g.add_vertex(v2)


def test_find_vertex_by_vid():
    g = Graph()
    av = Vertex("A")
    bv = Vertex("B")
    cv = Vertex("C")
    dv = Vertex("D")
    ev = Vertex("E")

    g.add_vertex(av)
    g.add_vertex(bv)
    g.add_vertex(cv)
    g.add_vertex(dv)
    g.add_vertex(ev)

    fav = g.find_vertex_by_vid("A")
    fcv = g.find_vertex_by_vid("C")
    fdv = g.find_vertex_by_vid("D")

    assert fav == av
    assert fcv == cv
    assert fdv == dv
