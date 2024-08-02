data = {
"A":["B", "E", "C"],
"B":["D", "E","A"],
"D":["B"],
"E":["B","A"],
"C":["A"]
}
visited = []
def DFS(data,Node):
    if Node not in visited:
        visited.append(Node)
        print(Node,end=" ")
        for i in data[Node]:
            DFS(data,i)
DFS(data,"A")