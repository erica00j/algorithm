import sys
from collections import defaultdict

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
#graph = [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
#print(graph)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False] * (N + 1)
result = 0
for i in range(1, N + 1):  # 1부터 N까지 순회
    if not visited[i]:
        dfs(graph, i, visited)
        result += 1

print(result)