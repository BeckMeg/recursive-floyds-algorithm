# Number of vertices
V = 4
INF = 999


# Algorithm 
def floyd(g):
    dist = list(map(lambda i: list(map(lambda j: j, i)), g))

    # Adding vertices individually
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    sol(dist)


# Printing the output
def sol(dist):

    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end="  ")

        print(" ")


G = [[0, 5, INF, 10],
     [INF, 0, 3, INF],
     [INF, INF, 0, 1],
     [INF, INF, INF, 0]]
floyd(G)

