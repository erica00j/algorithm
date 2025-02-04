N, M = map(int,input().split())
rec = []
for i in range(N):
    rec.append(list(map(int,input())))

side = 0
for i in range(min(N, M), 0 , -1):
    for j in range(N - i):
        for k in range(M - i):
            if rec[j][k] == rec[j][k+i] == rec[j+i][k] == rec[j+i][k+i]:
                side = max(side,i+1)
if side != 0:
    print((side)**2)
else:
    print(1)