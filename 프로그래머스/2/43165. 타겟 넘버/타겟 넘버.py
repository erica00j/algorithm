answer = 0
def dfs(numbers, target, result, idx):
    global answer
    if idx == len(numbers):
        if result == target:
            answer+=1
            return
    else:
        dfs(numbers,target,result+numbers[idx],idx+1)
        dfs(numbers,target,result-numbers[idx],idx+1)
def solution(numbers, target):
    dfs(numbers,target,0,0)
    return answer