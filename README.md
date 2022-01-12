# Python bootcamp capstone project

Dijkstra’s Algorithm - A program that finds the shortest path through a graph using its edges.

The `demo.py` script shows the shortest path between two vertices in a graph.

## Graph implementation

For graph manipulation and representation 3 classes have been created:
 * `Vertex`, which holds its edges to other vertices and their distance
 * `Path`, which is a list of vertices connected over their edges
 * `Graph`, which holds a set of vertices

## Dijkstra shortest path algorithm
The algorithm is implemented in the `Dijkstra` class, which holds a graph and returns the shortest path given two vertices.

## Testing
Testing was done using the `pytest` library.