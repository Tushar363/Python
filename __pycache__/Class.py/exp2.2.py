function calculateDistance(graph, startingVertex):
    distance = {}  
    for each vertex v in graph:
        distance[v] = infinity 
    distance[startingVertex] = 0  
    pq = priority_queue()
    pq.push((0, startingVertex))  
    
    while pq is not empty:
        currentDistance, currentVertex = pq.pop() 
        if currentDistance > distance[currentVertex]:
            continue 
        for each neighbor, weight in graph[currentVertex]:
            newDistance = currentDistance + weight  
            if newDistance < distance[neighbor]:
                distance[neighbor] = newDistance 
                pq.push((newDistance, neighbor))  
                
    return distance 

graph = { ... }  
result = calculateDistance(graph, startingVertex) 
for each vertex v, distance d in result:
    print(v, ":", d)