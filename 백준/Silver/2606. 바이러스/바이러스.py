from collections import deque

N = int(input())
M  = int(input())
#graph = [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]

# 각 노드의 연결 리스트를 저장할 graph_ 초기화 (0번 인덱스를 비우기 위해 max_node + 1)
graph_ = [[] for _ in range(N + 1)]

# 그래프 변환 작업
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph_[node1].append(node2)
    graph_[node2].append(node1)

#graph_ = [[],[2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
virus = []

def bfs(graph_,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        virus.append(v)
        for i in graph_[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
visited = [False]*(N+1)
bfs(graph_,1,visited)
print(len(virus)-1)