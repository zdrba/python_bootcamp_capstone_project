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

    assert vertex.edge_vertices == []


def test_vertex_add_one_edge():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    distance = 5

    a_vertex.add_edge(b_vertex, distance)

    a_edge_vertex = a_vertex.edge_vertices[0]

    assert a_edge_vertex == b_vertex


def test_distance_to_edge_vertex():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    distance = 5

    a_vertex.add_edge(b_vertex, distance)
    ab_distance = a_vertex.get_edge_vertex_distance(a_vertex.edge_vertices[0])

    assert ab_distance == 5


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

    a_edge_vertices = a_vertex.edge_vertices

    assert len(a_edge_vertices) == 3

    assert a_edge_vertices[0] == b_vertex
    assert a_vertex.get_edge_vertex_distance(b_vertex) == ab_distance

    assert a_edge_vertices[1] == c_vertex
    assert a_vertex.get_edge_vertex_distance(c_vertex) == ac_distance

    assert a_edge_vertices[2] == d_vertex
    assert a_vertex.get_edge_vertex_distance(d_vertex) == ad_distance


def test_edge_vertices():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    c_vertex = Vertex("C")

    assert a_vertex.edge_vertices == []
    a_vertex.add_edge(b_vertex, 3)

    assert a_vertex.edge_vertices == [b_vertex]

    a_vertex.add_edge(c_vertex, 5)
    assert len(a_vertex.edge_vertices) == 2
    assert b_vertex in a_vertex.edge_vertices
    assert c_vertex in a_vertex.edge_vertices


def test_edge_vertices_ids():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    c_vertex = Vertex("C")

    assert a_vertex.edge_vertices_ids == []

    a_vertex.add_edge(b_vertex, 3)

    assert a_vertex.edge_vertices_ids == ["B"]

    a_vertex.add_edge(c_vertex, 5)
    assert len(a_vertex.edge_vertices_ids) == 2
    assert "B" in a_vertex.edge_vertices_ids
    assert "C" in a_vertex.edge_vertices_ids


def test_vertex_find_edge_vertex_by_vid():
    a_vertex = Vertex("A")
    b_vertex = Vertex("B")
    c_vertex = Vertex("C")

    assert a_vertex.find_edge_vertex_by_vid("B") is None

    a_vertex.add_edge(b_vertex, 1)
    assert a_vertex.find_edge_vertex_by_vid("B") == b_vertex

    a_vertex.add_edge(c_vertex, 2)
    assert a_vertex.find_edge_vertex_by_vid("C") == c_vertex


def test_vertex_equality_by_vid():
    a_vertex1 = Vertex("A")
    a_vertex2 = Vertex("A")
    b_vertex = Vertex(3)

    assert a_vertex1 == a_vertex2
    assert a_vertex1 != b_vertex


def test_vertex_equality_by_amount_of_edges():
    a_vertex1 = Vertex("A")
    a_vertex2 = Vertex("A")
    b_vertex = Vertex("B")
    c_vertex = Vertex("C")

    a_vertex1.add_edge(b_vertex, 3)
    a_vertex2.add_edge(b_vertex, 3)

    assert a_vertex1 == a_vertex2

    a_vertex1.add_edge(c_vertex, 5)
    assert a_vertex1 != b_vertex


def test_vertex_equality_by_edge_vertices_vids():
    a_vertex1 = Vertex("A")
    a_vertex2 = Vertex("A")
    b_vertex = Vertex("B")
    c_vertex = Vertex("C")

    a_vertex1.add_edge(b_vertex, 3)
    a_vertex2.add_edge(c_vertex, 3)

    assert a_vertex1 != a_vertex2


def test_vertex_equality_by_edge_vertices_distances():
    a_vertex1 = Vertex("A")
    a_vertex2 = Vertex("A")
    b_vertex = Vertex("B")

    a_vertex1.add_edge(b_vertex, 3)
    a_vertex2.add_edge(b_vertex, 7)

    assert a_vertex1 != a_vertex2
