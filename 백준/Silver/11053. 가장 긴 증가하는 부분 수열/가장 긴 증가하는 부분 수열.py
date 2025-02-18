N=int(input())
arr=list(map(int,input().split()))
dp=[1]*N ## 초반 모든길이 1로 세팅
for i in range(1,N):
    for j in range(i):
        if arr[i]>arr[j]: 
            dp[i]=max(dp[i],dp[j]+1) ## 1씩 증가시켜서 갱신한다.
print(max(dp))