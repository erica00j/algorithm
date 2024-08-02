N, M = map(int,input().split())
graph = []
answer = []
for i in range(N):
    graph.append(list(map(str,input())))

for i in range(N-7):
    for j in range(M-7):
        count_1 = 0
        count_2 = 0
        
        #8x8 크기로 자르기
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 == 0:
                    if graph[a][b] != 'B':
                        count_1 += 1
                    if graph[a][b] != 'W':
                        count_2 += 1
                else:
                    if graph[a][b] != 'W':
                        count_1 += 1
                    if graph[a][b] != 'B':
                        count_2 += 1
        answer.append(count_1)
        answer.append(count_2)
print(min(answer))