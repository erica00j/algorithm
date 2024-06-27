from collections import deque

M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

# BFS 수행
bfs(graph)

# 결과 확인
days = 0
for row in graph:
    if 0 in row:  # 익지 않은 토마토가 남아있으면
        print(-1)
        break
    days = max(days, max(row))
else:
    # 처음 시작이 1이므로 1을 빼줘야 한다
    print(days - 1)
