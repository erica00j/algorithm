from collections import deque

N = int(input())
M  = int(input())

graph = [[] for _ in range(N + 1)]

# 그래프 변환 작업
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

#graph = [[],[2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
virus = []

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        virus.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False]*(N+1)
bfs(graph,1,visited)
print(len(virus)-1)
