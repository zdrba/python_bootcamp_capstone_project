#!/usr/bin/env python3
from src.graph import Graph, Vertex
from src import Dijkstra

demo_graph_visual = """
          [B]---8---[D]---7---[G]
         /|         | \\       | \\
        4 |         2  \\      |  9
      /   |         |   \\     |   \\
    [A]   11      [E]    4   14   [I]
      \\   |     /   |     \\   |   /
       8  |   7     6      \\  |  10
        \\ | /       |       \\ | /
         [C]---1---[F]---2---[H]
"""

from_vertex = "A"
to_vertex = "I"


def main() -> None:
    global demo_graph_visual, from_vertex, to_vertex

    print("Visual representation of the graph:")
    print(demo_graph_visual)
    print()
    print(f"Shortest path from vertex [{from_vertex}] to [{to_vertex}] is: {find_shortest_path_as_str()}")


def find_shortest_path_as_str() -> str:
    global from_vertex, to_vertex

    d = Dijkstra(create_demo_graph())
    start_vertex = d.graph.find_vertex_by_vid(from_vertex)
    end_vertex = d.graph.find_vertex_by_vid(to_vertex)
    shortest_path = d.find_shortest_path_from_to(start_vertex, end_vertex)
    path_vertex_ids = [f"[{vertex.vid}]" for vertex in shortest_path.vertices if shortest_path is not None]
    if len(path_vertex_ids) > 0:
        return " -> ".join(path_vertex_ids)
    else:
        return str(None)


def create_demo_graph() -> Graph:
    """
    Creates a graph to demonstrate dijkstra algorithm to find the shortest path.

    Visual representation of the graph:

          [B]---8---[D]---7---[G]
         /|         | \\       | \\
        4 |         2  \\      |  9
      /   |         |   \\     |   \\
    [A]   11      [E]    4   14   [I]
      \\   |     /   |     \\   |   /
       8  |   7     6      \\  |  10
        \\ | /       |       \\ | /
         [C]---1---[F]---2---[H]
    :return: Demonstration graph
    """
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")
    h = Vertex("H")
    i = Vertex("I")

    a.add_edge(b, 4)
    a.add_edge(c, 8)

    b.add_edge(a, 4)
    b.add_edge(c, 11)
    b.add_edge(d, 8)

    c.add_edge(a, 8)
    c.add_edge(b, 11)
    c.add_edge(e, 7)
    c.add_edge(f, 1)

    d.add_edge(b, 8)
    d.add_edge(e, 2)
    d.add_edge(g, 7)
    d.add_edge(h, 4)

    e.add_edge(c, 7)
    e.add_edge(d, 2)
    e.add_edge(f, 6)

    f.add_edge(c, 1)
    f.add_edge(e, 6)
    f.add_edge(h, 2)

    g.add_edge(d, 7)
    g.add_edge(h, 14)
    g.add_edge(i, 9)

    h.add_edge(d, 4)
    h.add_edge(f, 2)
    h.add_edge(g, 14)
    h.add_edge(i, 10)

    i.add_edge(g, 9)
    i.add_edge(h, 10)

    return Graph({a, b, c, d, e, f, g, h, i})


if __name__ == "__main__":
    main()
