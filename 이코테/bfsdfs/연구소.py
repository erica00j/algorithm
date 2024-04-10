n, m =map(int, input().split())
graph = []
new_graph = [[0]*m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

#graph = [[2, 0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 2, 0], [0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]


dx = [-1,0,1,0]
dy = [0,1,0,-1]


result = 0

#바이러스 퍼뜨리기
def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<m:
            if new_graph[nx][ny]==0:
                new_graph[nx][ny]=2
                virus(nx,ny)
                
#최종 크기 구하기
def count():
    count = 0
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 0:
                count += 1
    return count

#울타리 설치
def dfs(wall):
    global result
    #울타리 3개 설치된 경우
    if wall==3:
        #울타리 설치된 맵으로 바꾸기
        for i in range(n):
            for j in range(m):
                new_graph[i][j] = graph[i][j]
        #바이러스 퍼뜨리기
        for i in range(n):
            for j in range(m):
                if new_graph[i][j]==2:
                    virus(i,j)
        
        #안전 영역 계산
        result = max(result,count())
        return result
    
    #울타리 설치하기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall += 1
                dfs(wall)
                graph[i][j] = 0
                wall -= 1
                
dfs(0)
print(result)
