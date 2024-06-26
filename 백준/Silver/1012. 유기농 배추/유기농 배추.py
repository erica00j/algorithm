from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

T = int(input())
for _ in range(T):
    count = 0
    M, N, K = map(int,input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        i,j = map(int,input().split())
        graph[i][j] = 1
    #graph = [[1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 1, 1, 1, 0]]

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)