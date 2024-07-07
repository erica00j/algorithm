N = int(input())
A = list(map(int,input().split()))
A.reverse()
#A = [4, 2, 5, 8, 4, 11, 15]

dp = [1] * N

for i in range(1,N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))
#dp = [1, 1, 2, 3, 2, 4, 5]