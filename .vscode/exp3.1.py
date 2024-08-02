# Time Complexity O(V^3) and Space Complexity O(V^2)
def Warshall(graph):
    n = len(graph)
    dist = []
    # Initialize distance matrix with initial values
    for i in range(0,n):
        dist.append([float('inf')]*n)
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    # Compute shortest paths using dynamic programming
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    return dist
graph = [
    [0, 8, float('inf'), 1],
    [float('inf'), 0, 1, float('inf')],
    [4, float('inf'), 0, float('inf')],
    [float('inf'), 2,9, 0]
]
result = Warshall(graph)
for i in range(len(result)):
    for j in range(len(result)):
        print(result[i][j],end="  ")
    print()