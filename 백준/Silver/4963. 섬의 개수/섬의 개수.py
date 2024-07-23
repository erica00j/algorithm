from collections import deque

while True:
    count = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int,input().split())))

    dx = [0,0,1,-1,-1,-1,1,1]
    dy = [1,-1,0,0,-1,1,-1,1]

    def bfs(x,y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        queue.append((nx, ny))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)