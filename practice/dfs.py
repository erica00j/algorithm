N, M, V = map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

graph = [sorted(g) for g in graph]

print(graph)

visited=[False]*(N+1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph,V,visited)