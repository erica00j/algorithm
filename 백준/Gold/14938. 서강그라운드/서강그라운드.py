import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost =dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
t = list(map(int,input().split()))
for i in range(r):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a, l))

result = []
for x in range(1,n+1):
    distance = [INF] * (n + 1)
    dijkstra(x)
    answer = 0
    for i in range(len(distance)):
        if distance[i] <= m:
            answer += t[i-1]
    result.append(answer)
print(max(result))