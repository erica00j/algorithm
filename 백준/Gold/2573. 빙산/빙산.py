from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]
N, M = map(int,input().split())
graph = []
year = 0
for i in range(N):
    graph.append(list(map(int,input().split())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    visited[x][y] += 1

                if visited[nx][ny] == 0 and graph[nx][ny] != 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1

while True:
    count = 0
    visited = [[0] * M for _ in range(N)]
    #탐색
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and graph[i][j] > 0:
                bfs(i,j)
                count += 1
    #녹이기
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                graph[i][j] -= (visited[i][j] - 1)
                if graph[i][j] < 0:
                    graph[i][j] = 0
    #덩어리 검사
    if count >= 2:
        print(year)
        break
    if count == 0:
        print(0)
        break
    year += 1