graph = {
  '6' : ['4','8'],
  '4' : ['3', '5'],
  '8' : ['9'],
  '3' : [],
  '5' : ['9'],
  '9' : []
}   #dictionary

visited = []
def dfs(visited, graph, node):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
##########################################
if __name__=="__main__":
    print("Depth-First Search")
    dfs(visited, graph, '6')
    print(visited)
