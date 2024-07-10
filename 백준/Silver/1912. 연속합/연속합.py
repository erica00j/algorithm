n = int(input())
number = list(map(int,input().split()))
#number = [10, -4, 3, 1, 5, 6, -35, 12, 21, -1]

dp = [-10000]*(n+1)
dp[0] = number[0]
for i in range(1,len(number)):
    dp[i] = max(dp[i-1]+number[i],number[i])
print(max(dp))