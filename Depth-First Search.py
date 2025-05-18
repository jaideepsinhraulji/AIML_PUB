graph = {
  '6' : ['4','8'],
  '4' : ['3', '5'],
  '8' : ['9'],
  '3' : [],
  '5' : ['9'],
  '9' : []
}   #dictionary


visited = [] # List for visited nodes.
stack = []     #Initialize a stack
def dfs(visited, graph, node):
  stack.insert(0,node)
  while stack:          
    m = stack.pop(0)
    visited.append(m)
    for child in graph[m]:  #accessing child or successors and adding them to stack
      if child not in visited:
         stack.insert(0,child)
  print("Visited ",visited)#out of while loop
# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '6')    # 6 is start state
