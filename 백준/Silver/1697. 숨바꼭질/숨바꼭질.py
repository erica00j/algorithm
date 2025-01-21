from collections import deque

N, K = map(int,input().split())

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(dist[x])
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and not dist[i]:
                dist[i] = dist[x] + 1
                queue.append(i)

dist = [0] * 100001
bfs()