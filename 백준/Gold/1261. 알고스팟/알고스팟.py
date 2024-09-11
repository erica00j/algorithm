from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
                if graph[nx][ny]==0:
                    queue.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited
graph = []
m, n = map(int,input().split())
for i in range(n):
    graph.append(list(map(int,input())))

visited = bfs(0,0)
print(visited[n-1][m-1])