"""Examples of Floyd-Warshall"""

INF = 999
# Example 1 using simple data:

G1 = [[0, 5, INF, 10],
      [INF, 0, 3, INF],
      [INF, INF, 0, 1],
      [INF, INF, INF, 0]]

output1 = [[0, 5, 8, 9],
           [INF, 0, 3, 4],
           [INF, INF, 0, 1],
           [INF, INF, INF, 0]]

# Example 2 using larger dataset:

G2 = [[0, 4, 6, 10, 2],
      [INF, 0, 7, 9, 5],
      [6, INF, 0, 7, INF],
      [INF, 2, INF, 0, 5],
      [3, INF, INF, 4, 0]]

output2 = [[0, 4, 6, 6, 2],  #
           [8, 0, 7, 9, 5],
           [6, 9, 0, 7, 8],
           [8, 2, 9, 0, 5],
           [3, 6, 9, 4, 0]]

# Example 3 with the addition of negative directed

G3 = [[0, INF, 5, INF],
      [INF, 0, 4, -1],
      [INF, INF, 0, 5],
      [1, -3, INF, 0]]

output3 = [[0, 7, 5, 6],
           [0, -4, 0, -5],
           [6, 2, 0, 1],
           [-3, -7, -3, -8]]