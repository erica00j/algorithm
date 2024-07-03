from collections import deque

N, L, R = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))
#graph = [[50, 30], [20, 40]]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

people = []
def bfs(x,y,index):
    united = []
    united.append((x,y))
    queue = deque()
    queue.append((x,y))
    summary = graph[x][y]
    visited[x][y] = index
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    queue.append((nx, ny))
                    visited[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
    for i,j in united:
        graph[i][j] = summary // count
    return count

total_count = 0
while True:
    visited = [[-1]*N for _ in range(N)]
    index = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                bfs(i,j,index)
                index += 1
    if index == N*N:
        break
    total_count += 1

print(total_count)