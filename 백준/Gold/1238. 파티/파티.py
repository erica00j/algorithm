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

N, M, X = map(int,input().split())

answer = []
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

#연결 정보 입력
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

dijkstra(X)

#오는 길 최단경로값 정보 리스트
for i in range(1,N+1):
    answer.append(distance[i])
for i in range(1,N+1):
    distance = [INF] * (N + 1)
    dijkstra(i)
    answer[i-1] += distance[X]
print(max(answer))