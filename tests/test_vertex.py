from src.graph import Vertex


def test_vertex_init_with_vid():
    a_vertex_id = "A"
    b_vertex_id = 3

    a_vertex = Vertex(a_vertex_id)
    b_vertex = Vertex(b_vertex_id)

    assert a_vertex.vid == a_vertex_id
    assert b_vertex.vid == b_vertex_id


def test_vertex_empty_edges():
    vertex = Vertex("A")

    assert vertex.edges == []


def test_edge_init():
    vertex = Vertex("A")
    distance = 5
    edge = Vertex.Edge(vertex, distance)

    assert edge.vertex == vertex
    assert edge.distance == distance


def test_vertex_add_one_edge():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    distance = 5

    a_vertex.add_edge(b_vertex, distance)

    a_edge = a_vertex.edges[0]

    assert a_edge.vertex == b_vertex
    assert a_edge.distance == distance


def test_vertex_add_three_edges():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    c_vertex = Vertex("C")
    d_vertex = Vertex("D")

    ab_distance = 3
    ac_distance = 7
    ad_distance = 9

    a_vertex.add_edge(b_vertex, ab_distance)
    a_vertex.add_edge(c_vertex, ac_distance)
    a_vertex.add_edge(d_vertex, ad_distance)

    edges = a_vertex.edges

    assert len(edges) == 3

    assert edges[0].vertex == b_vertex
    assert edges[0].distance == ab_distance

    assert edges[1].vertex == c_vertex
    assert edges[1].distance == ac_distance

    assert edges[2].vertex == d_vertex
    assert edges[2].distance == ad_distance
