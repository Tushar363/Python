# Define a function to find the parent of a node
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Define a function to perform union of two sets
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Define Kruskal's algorithm
def kruskal(graph,result):
    i = 0
    e = 0

    # Sort all the edges in non-decreasing order of their weight
    graph = sorted(graph, key=lambda item: item[2])

    parent = {}
    rank = {}

    # Initialize parent and rank for each vertex
    for u, v, _ in graph:
        if u not in parent:
            parent[u] = u
            rank[u] = 0
        if v not in parent:
            parent[v] = v
            rank[v] = 0
    
    # Number of edges to be taken is equal to V-1
    while e < len(parent) - 1:
        u, v, w = graph[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e += 1
            result.append((u, v, w))
            union(parent, rank, x, y)

    # Print the constructed MST
    print("Edges in the constructed MST:")
    for u, v, weight in result:
        print(f"{u} -- {v} == {weight}")


# Example graph represented as an adjacency list with string vertices
graph = [
        ["A","B",3],["A","C",1],["A","D",4],["B","D",5],
    ["B","E",3],["C","D",5],["C","F",3],["D","F",6],["E","F",2]]
result = []
N = 6
kruskal(graph,result)
mini_sum = 0
for i in result:
    mini_sum += i[2]
print(f"minimun cost is : {mini_sum}")