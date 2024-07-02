from collections import deque

N, K = map(int,input().split())
graph = []
data = []
for i in range(N):
    graph.append(list(map(int,input().split())))
    # graph = [[1, 0, 2], [0, 0, 0], [3, 0, 0]]
    for j in range(N):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))
S, X, Y = map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

data.sort()
#data = [(1, 0, 0, 0), (2, 0, 0, 2), (3, 0, 2, 0)]
q = deque(data)

while q:
    num,s,x,y = q.popleft()
    if s == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < N and 0 <= ny and ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = num
                q.append((num,s+1,nx,ny))
#graph = [[1, 1, 2], [1, 1, 2], [3, 3, 2]]
print(graph[X-1][Y-1])