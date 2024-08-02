data = {
"1":["0","2","3","4"],
"0":["1","2"], 
"2":["0","1","3"], 
"3":["1","2","4"], 
"4":[]
}
queue = []
visited = []
def BFS(data,Node):
  queue.append(Node)
  visited.append(Node)
  while len(queue)>0:
      n = queue.pop(0)
      print(n,end=" ")
      for i in data[n]:
        if i not in visited:
          queue.append(i)
          visited.append(i)
BFS(data,"0")
  visited.append(Node)
  while len(queue)>0:
      n = queue.pop(0)
      print(n,end=" ")
      for i in data[n]:
        if i not in visited: