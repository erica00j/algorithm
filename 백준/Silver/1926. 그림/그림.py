from collections import deque

graph = []
n, m = map(int,input().split())
for i in range(n):
    graph.append(list(map(int,input().split())))
#graph = [[1, 1, 0, 1, 1], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    graph[x][y] = 0
    queue = deque()
    queue.append((x, y))
    result = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < m:
                if graph[nx][ny]==1:
                    queue.append((nx,ny))
                    graph[nx][ny] = 0
                    result += 1
    return result

count = 0
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            count += 1
            answer = max(bfs(i,j),answer)
print(count)
print(answer)