N, S = map(int,input().split())
array = list(map(int,input().split()))

cnt = 0
def backtrack_comb(idx, arr):
    global cnt

    if sum(arr) == S and len(arr) > 0:
        cnt += 1

    for i in range(idx + 1, N):
        backtrack_comb(i, arr + [array[i]])

backtrack_comb(-1, [])
print(cnt)