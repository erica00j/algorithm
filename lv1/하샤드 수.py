def solution(x):
    sum=0
    num_list=list(map(int,str(x)))
    for i in num_list:
        sum+=i
    if x%sum==0:
        return True
    else:
        return False