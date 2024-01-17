from collections import deque

N, M, V = map(int,input().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    num1,num2 = map(int,input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

graph = [sorted(g) for g in graph]
visited = [False]*(N+1)
graph2 = graph.copy()
visited2 = visited.copy()

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v= queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph2,V,visited2)
print()
bfs(graph,V,visited)