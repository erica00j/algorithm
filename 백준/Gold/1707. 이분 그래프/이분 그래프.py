from collections import deque
import sys
input = sys.stdin.readline

K = int(input())
for i in range(K):
    V, E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    color = [0]*(V+1)
    for j in range(E):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    flag = 1

    def bfs(start):
        global flag
        queue = deque()
        queue.append(start)
        color[start] = 1
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if color[i] == 0:
                    queue.append(i)
                    if color[v] == 1:
                        color[i] = 2
                    elif color[v] == 2:
                        color[i] = 1
                elif color[v] == color[i]:
                    flag = 0

    for k in range(1,V+1):
        if color[k] == 0:
            bfs(k)
    if flag:
        print("YES")
    else:
        print("NO")