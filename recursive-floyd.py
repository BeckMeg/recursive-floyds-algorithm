""" The recursive version of Floyd-Warshall algorithm """

INF = 9999

def floyd(shortestPath):

    # This defines the vertices input of the graph
    V = len(shortestPath)

    def recursive_floyd(i, j, k):

        # This is the base case.
        # When there are no intermediary vertices in the path.
        if k == -1:
            return shortestPath((i, j))

        # When using k to calculate the shortestPath, the minimum distance is returned
        else:
            return min(recursive_floyd(i, j, k-1),
                       recursive_floyd(i, k, k-1)
                       + recursive_floyd(j, k, k-1))

    # The values used to find the shortestPath and keep it updated
    for k in range(V):
        for i in range(V):
            for j in range(V):
                shortestPath[i][j] = recursive_floyd(i, j, k-1)
    # Return the shortest path
    """This is the shortest path found using recursive_floyd"""
    return shortestPath


