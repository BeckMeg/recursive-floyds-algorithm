""" The recursive version of Floyd-Warshall algorithm """

def floyd(shortestPath):

    V = len(shortestPath)

    def recursive_floyd(i, j, k):

        # This is the base case
        if k == -1:
            return shortestPath((i, j))

        else:
            return min(recursive_floyd(i, j, k-1),
                       recursive_floyd(i, k, k-1)
                       + recursive_floyd(j, k, k-1))
    sol(shortestPath)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                shortestPath[i][j] = recursive_floyd(i, j, k-1)
    return shortestPath
