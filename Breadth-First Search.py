graph = {
  '6' : ['4','8'],
  '4' : ['3', '5'],
  '8' : ['9'],
  '3' : [],
  '5' : ['9'],
  '9' : []
}
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  queue.append(node)
  visited.append(node)
  while queue:        
    m = queue.pop(0) 
    for child in graph[m]:  #accessing child or successors
      if child not in visited: #take care about duplicate entries from multiple paths in a graph
        queue.append(child)
        visited.append(child)
        #print("child+m:",child+m)
    
  print("Visited ",visited)#out of while loop
# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '6')    # 6 is start state
