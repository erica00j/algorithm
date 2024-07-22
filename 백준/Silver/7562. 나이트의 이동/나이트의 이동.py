from collections import deque

n = int(input())
for i in range(n):
    l = int(input())
    graph = [[0]*l for _ in range(l)]
    i, j = map(int,input().split())
    r, c = map(int,input().split())
    graph[r][c] = -1

    dx = [1,2,-1,-2,-2,-1,1,2]
    dy = [2,1,2,1,-1,-2,-2,-1]

    def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            while queue:
                x, y = queue.popleft()
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < l and 0 <= ny < l:
                        if graph[nx][ny] == 0:
                            graph[nx][ny] = graph[x][y] + 1
                            queue.append((nx,ny))
                        if graph[nx][ny] == -1:
                            graph[nx][ny] = graph[x][y] + 1
                            return graph[r][c]
    if r==i and c==j:
        print(0)
    else:
        answer = bfs(i,j)
        print(answer)