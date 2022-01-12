from src import Path, Vertex
import pytest


def test_path_init():
    v1 = Vertex("A")
    v2 = Vertex("B")

    v1.add_edge(v2, 3)

    vertices = [v1, v2]

    p = Path(vertices)

    assert p.vertices == vertices
    assert p.distance == 3


def test_path_not_connected_raises_value_error():
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")

    with pytest.raises(ValueError):
        Path([v1, v2])

    with pytest.raises(ValueError):
        v1.add_edge(v2, 3)
        Path([v1, v2, v3])


def test_path_distance():
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")

    v1.add_edge(v2, 42)
    v2.add_edge(v3, 99)

    assert Path([v1]).distance == 0
    assert Path([v1, v2]).distance == 42
    assert Path([v1, v2, v3]).distance == 141


def test_path_start_vertex():
    v1 = Vertex("A")
    v2 = Vertex("B")

    v1.add_edge(v2, 42)

    assert Path([v1, v2]).start_vertex == v1


def test_path_end_vertex():
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")

    v1.add_edge(v2, 42)
    v2.add_edge(v3, 99)

    assert Path([v1, v2, v3]).end_vertex == v3


def test_path_equality():
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")

    v1.add_edge(v2, 42)
    v2.add_edge(v3, 99)

    p1 = Path([v1, v2, v3])
    p2 = Path([v1, v2, v3])
    p3 = Path([v1, v2])

    assert p1 == p2
    assert p3 != p2


def test_path_concatenate_first_ends_the_same_as_second_starts():
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")

    v1.add_edge(v2, 123)
    v2.add_edge(v3, 456)

    p1 = Path([v1, v2])
    p2 = Path([v2, v3])

    p1.concat(p2)

    with pytest.raises(ValueError):
        p2.concat(p1)


def test_path_concatenate_returns_concatenated_path():
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")

    v1.add_edge(v2, 123)
    v2.add_edge(v3, 456)

    p1 = Path([v1, v2])
    p2 = Path([v2, v3])

    assert p1.concat(p2) == Path([v1, v2, v3])


def test_path_plus_operator_concatenates_paths():
    v1 = Vertex("A")
    v2 = Vertex("B")
    v3 = Vertex("C")
    v4 = Vertex("D")

    v1.add_edge(v2, 123)
    v2.add_edge(v3, 456)
    v3.add_edge(v4, 789)

    p1 = Path([v1, v2])
    p2 = Path([v2, v3])
    p3 = Path([v3, v4])

    assert p1 + p2 == Path([v1, v2, v3])
    assert p1 + p2 + p3 == Path([v1, v2, v3, v4])
