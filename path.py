from mygraph import *
import Queue

def shortest_path(g, v_start, v_to_find):
    """Input: Graph, GraphVertex, GraphVertex -> [GraphVertex]
    Purpose: Determine the shortest path in the graph from v_start v_to_find.
    The method should return a list consisting of the shortest path from
    v_start to v_to_find. The first element of the returned list should
    be v_start and the last should be v_to_find. If there is no path
    between the start and end vertices, return an empty list.
    Example: path.shortest_path(g, v_start, v_to_find) -> [v_start, v1, v2, v_to_find]
    Throws: InvalidInputException if any input is None or either vertex
    is not in g.
    """
    # Raises InvalidInputException if either vertex is none or is not in the graph
    # or if the graph is none
    if v_start == None or v_to_find == None:
        raise InvalidInputException(g)
    if g == None:
        raise InvalidInputException(g)
    if not g.containsVertex(v_start) or not g.containsVertex(v_to_find):
        raise InvalidInputException(g)

    shortestPath = [] # List to be returned representing the shortest path
    pathExists = False # Boolean to keep track of whether path exists
    vertices = Queue.Queue() # Queue used for breadth first search
    vertices.put(v_start)

    # We assign the prev pointer for each vertex to be None
    for vertex in g.vertices():
        vertex.prev = None

    # Decorating the prev pointers with the previous vertex
    while not vertices.empty():
        vertex = vertices.get()
        # We stop if we've reached the vertex to be found
        if vertex == v_to_find:
            pathExists = True
            break
        for edge in g.incidentEdges(vertex):
            nextVertex = g.opposite(vertex, edge)
            # Only visit the vertex if it hasn't been visited yet
            if nextVertex.prev == None:
                nextVertex.prev = vertex
                vertices.put(nextVertex)

    # If no path exists, we return empty list
    if pathExists == False:
        return shortestPath

    # Once we've decorated the right vertices, we traverse the prev pointers
    # to determine the shortest path
    shortestPath.append(v_to_find)
    prevVertex = v_to_find
    while not prevVertex == v_start:
        shortestPath.insert(0, prevVertex.prev)
        prevVertex = prevVertex.prev

    return shortestPath
