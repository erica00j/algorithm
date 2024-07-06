def solution(triangle):
    dp = triangle
    dp[1][0] = dp[0][0] + dp[1][0]
    dp[1][1] = dp[0][0] + dp[1][1]
    #dp =[[7], [10, 15], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

    for i in range(2,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] = dp[i][j] + dp[i-1][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = dp[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j] + dp[i-1][j], dp[i][j] + dp[i-1][j-1])
    return max(dp[-1])