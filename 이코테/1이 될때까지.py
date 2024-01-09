def solution(N,K):
    cnt=0
    while N!=1:
        if N%K==0:
            N = N/K
            cnt+=1
        else:
            N = N-1
            cnt+=1
    return cnt
print(solution(25,5))