from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(str,input())))
#graph = [['R', 'R', 'R', 'B', 'B'], ['G', 'G', 'B', 'B', 'B'], ['B', 'B', 'B', 'R', 'R'], ['B', 'B', 'R', 'R', 'R'], ['R', 'R', 'R', 'R', 'R']]
new_graph = [row[:] for row in graph]  # 원본 그래프를 복사

# 새로운 그래프에서 'G' 값을 'R'로 바꾸는 코드
for i in range(len(new_graph)):
    for j in range(len(new_graph[i])):
        if new_graph[i][j] == 'G':
            new_graph[i][j] = 'R'

def bfs(graph,x, y,color):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == color:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return True

count = 0
no_count = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] in ('R', 'G', 'B'):
            if bfs(graph, i, j, graph[i][j]):
                count += 1

for i in range(N):
    for j in range(N):
        if new_graph[i][j] in ('R', 'B'):
            if bfs(new_graph, i, j, new_graph[i][j]):
                no_count += 1
print(count)
print(no_count)